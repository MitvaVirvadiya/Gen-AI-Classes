"""02 — Cosine similarity and nearest neighbors on toy 2-D vectors.

    python 01-llms-from-scratch/02-embeddings/code/02_cosine_neighbors.py
"""

from __future__ import annotations

import json
import math
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "toy_vectors.json"


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(a: list[float]) -> float:
    return math.sqrt(dot(a, a))


def cosine(a: list[float], b: list[float]) -> float:
    denom = norm(a) * norm(b)
    if denom == 0:
        return 0.0
    return dot(a, b) / denom


def nearest(query: str, table: dict[str, list[float]], k: int = 3) -> list[tuple[str, float]]:
    q = table[query]
    scored = [(name, cosine(q, vec)) for name, vec in table.items() if name != query]
    scored.sort(key=lambda kv: kv[1], reverse=True)
    return scored[:k]


def main() -> None:
    raw = json.loads(DATA.read_text(encoding="utf-8"))
    table = {k: v for k, v in raw.items() if not k.startswith("_")}

    print("2-D toy space (draw this on paper):\n")
    print("  animals around +x, royalty around +y, vehicles around -x\n")
    for name, vec in table.items():
        print(f"  {name:8} {vec}")

    for query in ("cat", "king", "car"):
        print(f"\nnearest to {query!r}:")
        for name, score in nearest(query, table, k=3):
            print(f"  {name:8} cos={score:.3f}")

    print(
        "\nThese positions were drawn by a human, not learned.\n"
        "A real E is thousands of dimensions and the neighbors fall out of training."
    )


if __name__ == "__main__":
    main()
