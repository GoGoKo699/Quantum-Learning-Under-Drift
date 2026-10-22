"""Independent exact enumeration and stable evaluation of the cache classifier."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb, exp, factorial, fsum, log1p, prod


def rising(value: int, length: int) -> int:
    return prod(value + offset for offset in range(length))


def exact_moments(d: int, length: int) -> tuple[Fraction, Fraction]:
    """Return h_l=E(1-z)^l and Delta_l=h_l-d E[p(1-z)^l]."""
    alpha = Fraction(2 * d - 1, 2 * d)
    h = sum(
        Fraction(comb(length, j) * factorial(j), rising(d, j))
        * alpha ** (length - j)
        * Fraction(-1, 2) ** j
        for j in range(length + 1)
    )
    p_times_h = sum(
        Fraction(comb(length, j) * factorial(j + 1), rising(d, j + 1))
        * alpha ** (length - j)
        * Fraction(-1, 2) ** j
        for j in range(length + 1)
    )
    return h, h - d * p_times_h


def exact_bias(d: int, length: int, refresh: Fraction) -> Fraction:
    q = 1 - refresh
    moments = [exact_moments(d, k) for k in range(length + 1)]
    avoidance = [Fraction(1)]
    for m in range(1, length + 1):
        avoidance.append(
            q ** (m - 1) * moments[m][0]
            + refresh
            * sum(
                q ** (k - 1) * moments[k][0] * avoidance[m - k]
                for k in range(1, m)
            )
        )
    difference = q**length * moments[length][1] + refresh * sum(
        q**age * avoidance[length - age] * moments[age][1]
        for age in range(1, length)
    )
    return difference / 2


def dirichlet_moment(counts: list[int]) -> Fraction:
    return Fraction(prod(factorial(count) for count in counts), rising(len(counts), sum(counts)))


def brute_prediction_probability(
    d: int, length: int, refresh: Fraction, current_label: int
) -> Fraction:
    """Enumerate resets, all raw outcomes, and all preceding true labels.

    This calculation does not use the cache moment or renewal recurrence.
    Independent Haar epochs are integrated through Dirichlet monomial moments.
    """
    q = 1 - refresh
    total = Fraction(0)
    for resets in product((0, 1), repeat=length):
        epochs = [0]
        for reset in resets:
            epochs.append(epochs[-1] + reset)
        reset_weight = refresh ** sum(resets) * q ** (length - sum(resets))
        for outcomes in product(range(d), repeat=length + 1):
            if outcomes[-1] not in outcomes[:-1]:
                continue
            for preceding_labels in product((0, 1), repeat=length):
                labels = preceding_labels + (current_label,)
                counts = [[0] * d for _ in range(epochs[-1] + 1)]
                backgrounds = 0
                for epoch, outcome, label in zip(epochs, outcomes, labels):
                    if label:
                        counts[epoch][outcome] += 1
                    else:
                        backgrounds += 1
                probability = Fraction(1, 2**length * d**backgrounds)
                for epoch_counts in counts:
                    probability *= dirichlet_moment(epoch_counts)
                total += reset_weight * probability
    return total


def beta_bernstein_mean(
    degree: int, a: int, b: int, alpha: float, beta: float
) -> float:
    """E[(alpha*(1-p)+beta*p)^degree], p~Beta(a,b), by positive terms.

    The Bernstein expansion has beta-binomial weights. This avoids the
    alternating subtraction in exact_moments when using floating point.
    """
    initial_weight = exp(fsum(log1p(-a / (a + b + j)) for j in range(degree)))
    term = initial_weight * alpha**degree
    terms = [term]
    for j in range(degree):
        term *= (
            (degree - j) / (j + 1) * (a + j) / (b + degree - j - 1) * beta / alpha
        )
        terms.append(term)
    return fsum(terms)


def stable_moments(d: int, length: int) -> tuple[float, float]:
    alpha = (2 * d - 1) / (2 * d)
    beta = (d - 1) / (2 * d)
    h = beta_bernstein_mean(length, 1, d - 1, alpha, beta)
    if length == 0:
        return h, 0.0
    # The Beta integration-by-parts formula reweights p by p(1-p).
    difference = (
        length
        * (d - 1)
        / (2 * d * (d + 1))
        * beta_bernstein_mean(length - 1, 2, d, alpha, beta)
    )
    return h, difference


def stable_bias(d: int, length: int, refresh: float) -> float:
    if d < 2 or length < 1 or not 0 <= refresh <= 1:
        raise ValueError("Require d>=2, cache length>=1, and 0<=refresh<=1.")
    q = 1 - refresh
    moments = [stable_moments(d, k) for k in range(length + 1)]
    avoidance = [1.0]
    q_powers = [q**k for k in range(length + 1)]
    for m in range(1, length + 1):
        avoidance.append(
            q_powers[m - 1] * moments[m][0]
            + refresh
            * fsum(
                q_powers[k - 1] * moments[k][0] * avoidance[m - k]
                for k in range(1, m)
            )
        )
    difference = q_powers[length] * moments[length][1] + refresh * fsum(
        q_powers[age] * avoidance[length - age] * moments[age][1]
        for age in range(1, length)
    )
    return difference / 2


def run() -> dict:
    brute_cases = []
    for d, length, refresh in (
        (2, 1, Fraction(1, 4)),
        (2, 3, Fraction(1, 3)),
        (3, 3, Fraction(2, 5)),
    ):
        recurrence = exact_bias(d, length, refresh)
        enumerated = (
            brute_prediction_probability(d, length, refresh, 1)
            - brute_prediction_probability(d, length, refresh, 0)
        ) / 2
        assert recurrence == enumerated
        brute_cases.append(
            {
                "dimension": d,
                "cache_length": length,
                "refresh_probability": str(refresh),
                "exact_accuracy_advantage": str(enumerated),
                "enumeration_equals_recurrence": True,
            }
        )

    stable_cases = []
    for d in (2, 3, 8, 16):
        for refresh in (Fraction(1, 10), Fraction(1, 2), Fraction(9, 10)):
            length = min(d, refresh.denominator // refresh.numerator)
            exact = exact_bias(d, length, refresh)
            numerical = stable_bias(d, length, float(refresh))
            assert abs(numerical - float(exact)) < 1e-12
            q = 1 - refresh
            upper = Fraction(d - 1, 2 * d) * q / (refresh * d + q)
            assert 0 <= exact <= upper
            stable_cases.append(
                {
                    "dimension": d,
                    "cache_length": length,
                    "refresh_probability": str(refresh),
                    "positive_sum_matches_rational_result": True,
                    "below_universal_classical_bound": True,
                }
            )
    return {
        "brute_force_cases": brute_cases,
        "positive_sum_cases": stable_cases,
        "floating_comparison_tolerance": 1e-12,
    }
