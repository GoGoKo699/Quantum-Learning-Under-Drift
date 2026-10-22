#!/usr/bin/env python3
"""Generate a reproducible SVG and CSV from stable finite moment sums."""

from __future__ import annotations

import argparse
import csv
import math
import os
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "quantum-drift-matplotlib"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from cache_checks import stable_bias


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--preview-png", type=Path, help="Optional path for a raster preview.")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    d = 256
    rates = np.geomspace(1e-4, 0.99, 160)
    rows = []
    for rate in rates:
        r = float(rate)
        q = 1 - r
        length = math.floor(min(d, 1 / r))
        swap = (1 - 1 / d) * q / (8 * (2 - q))
        classical_upper = (1 - 1 / d) * q / (2 * (r * d + q))
        cache = stable_bias(d, length, r)
        if not (0 <= cache <= classical_upper + 1e-12):
            raise ArithmeticError("The computed cache advantage violates its analytic upper bound.")
        rows.append(
            {
                "dimension": d,
                "refresh_probability": r,
                "dimension_times_refresh": d * r,
                "cache_length": length,
                "swap_advantage": swap,
                "classical_advantage_upper_bound": classical_upper,
                "cache_advantage": cache,
            }
        )

    with (args.output_dir / "frontier.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 11,
            "svg.hashsalt": "quantum-learning-under-drift-frontier-v1",
            "svg.fonttype": "none",
        }
    )
    figure, axis = plt.subplots(figsize=(8.8, 5.7), constrained_layout=True)
    x = np.array([row["dimension_times_refresh"] for row in rows])
    q = 1 - rates
    swap = np.array([row["swap_advantage"] for row in rows]) / q
    upper = np.array([row["classical_advantage_upper_bound"] for row in rows]) / q
    cache = np.array([row["cache_advantage"] for row in rows]) / q
    axis.fill_between(x, cache, upper, color="#657482", alpha=0.10)
    axis.plot(x, swap, color="#0b6b9a", linewidth=2.5, label="Rolling SWAP: exact formula")
    axis.plot(x, upper, color="#555f69", linewidth=2, linestyle="--", label="All classical strategies: upper bound")
    axis.plot(x, cache, color="#b85b16", linewidth=2.2, label="Cache classifier: achieved advantage")
    axis.axvline(1, color="#9aa3ab", linewidth=1, linestyle=":")
    axis.set_xscale("log")
    axis.set_yscale("log")
    axis.set_xlabel(r"Dimension × refresh probability, $rd$")
    axis.set_ylabel(r"Prediction advantage divided by retention, $(p-1/2)/q$")
    axis.set_title("Predictive accuracy under refresh", loc="left", fontsize=16, pad=25)
    axis.text(
        0,
        1.025,
        r"$d=256$; cache length $L=\lfloor\min(d,1/r)\rfloor$. Shading bounds the classical optimum.",
        transform=axis.transAxes,
        fontsize=10,
        color="#47515a",
    )
    axis.grid(which="major", color="#dfe4e8", linewidth=0.7)
    axis.grid(which="minor", visible=False)
    axis.set_xlim(float(x.min()), float(x.max()))
    axis.set_ylim(4e-4, 0.8)
    axis.legend(loc="lower left", frameon=True, framealpha=0.96, fontsize=10)
    for spine in ("top", "right"):
        axis.spines[spine].set_visible(False)
    svg_path = args.output_dir / "frontier.svg"
    figure.savefig(
        svg_path,
        metadata={"Date": None, "Creator": "verification/plot_frontier.py"},
    )
    # Normalize exporter whitespace for stable text diffs.
    svg_path.write_text(
        "\n".join(line.rstrip() for line in svg_path.read_text(encoding="utf-8").splitlines())
        + "\n",
        encoding="utf-8",
    )
    if args.preview_png is not None:
        args.preview_png.parent.mkdir(parents=True, exist_ok=True)
        figure.savefig(args.preview_png, dpi=150)
    plt.close(figure)
    print(f"Wrote {args.output_dir / 'frontier.svg'} and {args.output_dir / 'frontier.csv'}")


if __name__ == "__main__":
    main()
