"""01 — The first layer of an LLM is a table lookup.

No PyTorch required. Random E, then x = E[ids].

    python 01-llms-from-scratch/02-embeddings/code/01_lookup_table.py
"""

from __future__ import annotations

import random

VOCAB = ["<pad>", "the", "cat", "sat", "on", "mat", "dog"]
TOKEN_TO_ID = {t: i for i, t in enumerate(VOCAB)}
D_MODEL = 8
SEED = 0


def make_embedding_matrix(vocab_size: int, d_model: int, seed: int) -> list[list[float]]:
    rng = random.Random(seed)
    # Small random numbers, like a freshly initialized nn.Embedding.
    return [[rng.uniform(-0.1, 0.1) for _ in range(d_model)] for _ in range(vocab_size)]


def lookup(E: list[list[float]], ids: list[int]) -> list[list[float]]:
    return [E[i] for i in ids]


def encode(words: list[str]) -> list[int]:
    return [TOKEN_TO_ID[w] for w in words]


def main() -> None:
    E = make_embedding_matrix(len(VOCAB), D_MODEL, SEED)
    print(f"E shape: ({len(E)}, {len(E[0])})  = (vocab, d_model)")
    print(f"row for 'cat' (id={TOKEN_TO_ID['cat']}): {[round(x, 3) for x in E[TOKEN_TO_ID['cat']]]}")

    sentence = ["the", "cat", "sat", "on"]
    ids = encode(sentence)
    x = lookup(E, ids)
    print(f"\nsentence: {sentence}")
    print(f"ids:      {ids}")
    print(f"x shape:  ({len(x)}, {len(x[0])})  = (seq, d_model)")

    batch = [
        encode(["the", "cat", "sat", "on"]),
        encode(["the", "dog", "sat", "on"]),
    ]
    batch_x = [lookup(E, ids) for ids in batch]
    print(f"\nbatch ids: {batch}")
    print(f"batch x shape: ({len(batch_x)}, {len(batch_x[0])}, {len(batch_x[0][0])})  = (batch, seq, d_model)")
    print(
        "\nThese numbers are random. Training (Lesson 1.9) will move the rows\n"
        "so that tokens used alike become geometrically alike."
    )


if __name__ == "__main__":
    main()
