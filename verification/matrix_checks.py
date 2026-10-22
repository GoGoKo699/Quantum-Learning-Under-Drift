"""Finite matrix checks of the posterior and retained-memory instrument.

Haar moments are represented by symmetric projectors, not Monte Carlo draws.
The randomly generated positive effects and input states use a fixed seed.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


SEED = 20261022
TOLERANCE = 1e-12


def symmetric_projector(d: int, copies: int) -> np.ndarray:
    dimension = d**copies
    result = np.zeros((dimension, dimension), dtype=complex)
    shape = (d,) * copies
    for permutation in itertools.permutations(range(copies)):
        for coordinates in itertools.product(range(d), repeat=copies):
            permuted = tuple(coordinates[j] for j in permutation)
            source = np.ravel_multi_index(coordinates, shape)
            target = np.ravel_multi_index(permuted, shape)
            result[target, source] += 1
    return result / math.factorial(copies)


def random_density(d: int, rng: np.random.Generator) -> np.ndarray:
    matrix = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    positive = matrix @ matrix.conj().T
    return positive / np.trace(positive)


def random_pure_state(d: int, rng: np.random.Generator) -> np.ndarray:
    vector = rng.normal(size=d) + 1j * rng.normal(size=d)
    vector /= np.linalg.norm(vector)
    return np.outer(vector, vector.conj())


def trace_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


def discard_second(matrix: np.ndarray, d: int) -> np.ndarray:
    return np.einsum("abcb->ac", matrix.reshape(d, d, d, d))


def swap_matrix(d: int) -> np.ndarray:
    result = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for j in range(d):
            result[j * d + i, i * d + j] = 1
    return result


def controlled_pair_swap(qubits: int, pair: int) -> np.ndarray:
    """Fredkin on ancilla, M[pair], X[pair]; register order is ancilla,M,X."""
    width = 1 + 2 * qubits
    dimension = 2**width
    result = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        bits = [(source >> (width - 1 - j)) & 1 for j in range(width)]
        if bits[0]:
            left, right = 1 + pair, 1 + qubits + pair
            bits[left], bits[right] = bits[right], bits[left]
        target = sum(bit << (width - 1 - j) for j, bit in enumerate(bits))
        result[target, source] = 1
    return result


def local_pair_swap(qubits: int, pair: int) -> np.ndarray:
    width = 2 * qubits
    dimension = 2**width
    result = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        bits = [(source >> (width - 1 - j)) & 1 for j in range(width)]
        bits[pair], bits[qubits + pair] = bits[qubits + pair], bits[pair]
        target = sum(bit << (width - 1 - j) for j, bit in enumerate(bits))
        result[target, source] = 1
    return result


def check_posterior(rng: np.random.Generator) -> list[dict]:
    results = []
    for d in (2, 3):
        for copies in (1, 2):
            sym = symmetric_projector(d, copies)
            sym_next = symmetric_projector(d, copies + 1)
            dim_sym = math.comb(d + copies - 1, copies)
            dim_next = math.comb(d + copies, copies + 1)
            identity_errors = []
            bound_excesses = []
            for _ in range(8):
                size = d**copies
                matrix = rng.normal(size=(size, size)) + 1j * rng.normal(
                    size=(size, size)
                )
                effect = sym @ matrix @ matrix.conj().T @ sym
                effect /= np.linalg.eigvalsh(effect).max()
                effect_trace = np.trace(effect)
                outcome_probability = effect_trace / dim_sym

                # Direct contraction of the (m+1)-copy Haar moment.
                joint = np.kron(effect, np.eye(d)) @ sym_next / dim_next
                posterior = np.einsum(
                    "iaib->ab", joint.reshape(size, d, size, d)
                ) / outcome_probability
                marginal = np.einsum(
                    "aibi->ab",
                    effect.reshape(d, d ** (copies - 1), d, d ** (copies - 1)),
                ) / effect_trace
                predicted = (np.eye(d) + copies * marginal) / (d + copies)
                identity_errors.append(float(np.linalg.norm(posterior - predicted)))

                success = 0.5 + trace_norm(posterior - np.eye(d) / d) / 4
                bound = 0.5 + copies * (d - 1) / (2 * d * (d + copies))
                bound_excesses.append(success - bound)

            # Highest-weight effects saturate the conditional success bound.
            pure = random_pure_state(d, rng)
            effect = np.array([[1.0 + 0j]])
            for _ in range(copies):
                effect = np.kron(effect, pure)
            joint = np.kron(effect, np.eye(d)) @ sym_next / dim_next
            posterior = np.einsum(
                "iaib->ab", joint.reshape(d**copies, d, d**copies, d)
            ) / (np.trace(effect) / dim_sym)
            success = 0.5 + trace_norm(posterior - np.eye(d) / d) / 4
            bound = 0.5 + copies * (d - 1) / (2 * d * (d + copies))
            assert max(identity_errors) < TOLERANCE
            assert max(bound_excesses) < TOLERANCE
            assert abs(success - bound) < TOLERANCE
            results.append(
                {
                    "dimension": d,
                    "training_copies": copies,
                    "positive_effects": 8,
                    "posterior_identity": "passed",
                    "conditional_bound": "passed",
                    "highest_weight_saturation": "passed",
                    "saturating_success": round(success, 12),
                }
            )
    return results


def check_instrument(rng: np.random.Generator) -> list[dict]:
    results = []
    for d in (2, 3):
        swap = swap_matrix(d)
        plus = (np.eye(d * d) + swap) / 2
        minus = (np.eye(d * d) - swap) / 2
        for _ in range(10):
            sigma = random_density(d, rng)
            other_memory = random_density(d, rng)
            rho = random_density(d, rng)
            joint = np.kron(sigma, rho)
            positive = plus @ joint @ plus
            negative = minus @ joint @ minus
            memory = discard_second(positive + negative, d)
            assert np.linalg.norm(memory - (sigma + rho) / 2) < TOLERANCE
            plus_probability = float(np.trace(positive).real)
            expected_plus = (1 + np.trace(sigma @ rho).real) / 2
            assert abs(plus_probability - expected_plus) < TOLERANCE

            other_joint = np.kron(other_memory, rho)
            other_output = discard_second(
                plus @ other_joint @ plus + minus @ other_joint @ minus, d
            )
            assert abs(
                trace_norm(memory - other_output)
                - trace_norm(sigma - other_memory) / 2
            ) < TOLERANCE

            pure = random_pure_state(d, rng)
            signal_success = float(
                np.trace(plus @ np.kron(sigma, pure) @ plus).real
            )
            background_success = float(
                np.trace(minus @ np.kron(sigma, np.eye(d) / d) @ minus).real
            )
            actual = (signal_success + background_success) / 2
            predicted = 0.5 + (np.trace(sigma @ pure).real - 1 / d) / 4
            assert abs(actual - predicted) < TOLERANCE
        results.append(
            {
                "dimension": d,
                "density_matrix_cases": 10,
                "retained_memory_update": "passed",
                "outcome_probability": "passed",
                "balanced_label_accuracy": "passed",
                "trace_distance_contraction": "passed",
            }
        )
    return results


def check_circuit() -> list[dict]:
    results = []
    hadamard = np.array([[1, 1], [1, -1]], dtype=complex) / math.sqrt(2)
    for qubits in (1, 2):
        d = 2**qubits
        joint_dimension = d * d
        controlled = np.eye(2 * joint_dimension, dtype=complex)
        for pair in range(qubits):
            controlled = controlled_pair_swap(qubits, pair) @ controlled
        expected = np.zeros_like(controlled)
        expected[:joint_dimension, :joint_dimension] = np.eye(joint_dimension)
        expected[joint_dimension:, joint_dimension:] = swap_matrix(d)
        assert np.linalg.norm(controlled - expected) < TOLERANCE

        full_hadamard = np.kron(hadamard, np.eye(joint_dimension))
        unitary = full_hadamard @ controlled @ full_hadamard
        kraus_plus = unitary[:joint_dimension, :joint_dimension]
        kraus_minus = unitary[joint_dimension:, :joint_dimension]
        assert np.linalg.norm(
            kraus_plus - (np.eye(joint_dimension) + swap_matrix(d)) / 2
        ) < TOLERANCE
        assert np.linalg.norm(
            kraus_minus - (np.eye(joint_dimension) - swap_matrix(d)) / 2
        ) < TOLERANCE
        results.append(
            {
                "qubits_per_register": qubits,
                "controlled_pair_swaps": qubits,
                "global_controlled_swap": "passed",
                "luders_kraus_operators": "passed",
            }
        )
    return results


def check_local_refinement_counterexample() -> dict:
    d = 4
    memory = np.diag([1.0, 0.0, 0.0, 0.0]).astype(complex)
    incoming = np.diag([0.0, 0.0, 0.0, 1.0]).astype(complex)
    joint = np.kron(memory, incoming)
    swap = swap_matrix(d)
    plus = (np.eye(d * d) + swap) / 2
    minus = (np.eye(d * d) - swap) / 2
    global_output = discard_second(plus @ joint @ plus + minus @ joint @ minus, d)
    local_swaps = [local_pair_swap(2, pair) for pair in range(2)]
    refined_output = np.zeros((d, d), dtype=complex)
    even_effect = np.zeros((d * d, d * d), dtype=complex)
    for signs in itertools.product((-1, 1), repeat=2):
        projector = np.eye(d * d, dtype=complex)
        for sign, local_swap in zip(signs, local_swaps):
            projector = projector @ (np.eye(d * d) + sign * local_swap) / 2
        refined_output += discard_second(projector @ joint @ projector, d)
        if math.prod(signs) == 1:
            even_effect += projector
    assert np.linalg.norm(even_effect - plus) < TOLERANCE
    assert np.linalg.norm(global_output - (memory + incoming) / 2) < TOLERANCE
    assert np.linalg.norm(refined_output - np.eye(d) / d) < TOLERANCE
    distance = trace_norm(global_output - refined_output) / 2
    assert abs(distance - 0.5) < TOLERANCE
    return {
        "qubits_per_register": 2,
        "parity_povm_matches_global_swap": True,
        "retained_memory_trace_distance": round(distance, 12),
        "global_memory_diagonal": [0.5, 0.0, 0.0, 0.5],
        "local_refinement_memory_diagonal": [0.25, 0.25, 0.25, 0.25],
    }


def run() -> dict:
    rng = np.random.default_rng(SEED)
    return {
        "seed": SEED,
        "absolute_error_tolerance": TOLERANCE,
        "posterior_cases": check_posterior(rng),
        "instrument_cases": check_instrument(rng),
        "ancilla_circuit_cases": check_circuit(),
        "local_refinement_counterexample": check_local_refinement_counterexample(),
    }
