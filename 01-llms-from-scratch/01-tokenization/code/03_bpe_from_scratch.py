"""03 — Train a character-level BPE on the tiny corpus.

This is a teaching BPE, not GPT-2. Base units are unicode characters
(not bytes) so you can read every merge.

Run:
    python 01-llms-from-scratch/01-tokenization/code/03_bpe_from_scratch.py

Writes:
    ../artifacts/vocab.json
    ../artifacts/merges.txt
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data" / "tiny_corpus.txt"
ART = HERE.parent / "artifacts"
NUM_MERGES = 40


def word_freqs(text: str) -> Counter[str]:
    # Pretokenize on whitespace. Real GPT-2 uses a regex; this is the idea.
    freqs: Counter[str] = Counter()
    for word in text.split():
        freqs[word] += 1
    return freqs


def to_symbols(freqs: Counter[str]) -> dict[tuple[str, ...], int]:
    # End-of-word marker so "low" and "lowest" can share "low" but not glue
    # across the word boundary.
    return {tuple(list(word) + ["</w>"]): n for word, n in freqs.items()}


def pair_counts(corpus: dict[tuple[str, ...], int]) -> Counter[tuple[str, str]]:
    pairs: Counter[tuple[str, str]] = Counter()
    for symbols, n in corpus.items():
        for a, b in zip(symbols, symbols[1:]):
            pairs[(a, b)] += n
    return pairs


def merge_pair(
    corpus: dict[tuple[str, ...], int], pair: tuple[str, str]
) -> dict[tuple[str, ...], int]:
    a, b = pair
    glued = a + b
    out: dict[tuple[str, ...], int] = {}
    for symbols, n in corpus.items():
        merged: list[str] = []
        i = 0
        while i < len(symbols):
            if i < len(symbols) - 1 and symbols[i] == a and symbols[i + 1] == b:
                merged.append(glued)
                i += 2
            else:
                merged.append(symbols[i])
                i += 1
        out[tuple(merged)] = n
    return out


def train_bpe(text: str, num_merges: int) -> tuple[list[str], list[tuple[str, str]]]:
    corpus = to_symbols(word_freqs(text))
    merges: list[tuple[str, str]] = []

    # Base vocab: every character we actually saw + the end-of-word mark.
    vocab: set[str] = {"</w>"}
    for symbols in corpus:
        vocab.update(symbols)

    print(f"starting pieces: {len(corpus)} word types")
    print(f"base vocab size: {len(vocab)}")

    for step in range(1, num_merges + 1):
        pairs = pair_counts(corpus)
        if not pairs:
            print("no pairs left, stopping")
            break
        best, count = pairs.most_common(1)[0]
        corpus = merge_pair(corpus, best)
        merges.append(best)
        vocab.add(best[0] + best[1])
        print(f"  merge {step:02d}: {best[0]!r} + {best[1]!r}  (count={count})")

    # Stable id order: specials, then sorted tokens.
    vocab_list = ["<pad>", "<unk>", "<bos>", "<eos>", *sorted(vocab)]
    return vocab_list, merges


def main() -> None:
    text = DATA.read_text(encoding="utf-8")
    vocab, merges = train_bpe(text, NUM_MERGES)

    ART.mkdir(parents=True, exist_ok=True)
    (ART / "vocab.json").write_text(
        json.dumps({tok: i for i, tok in enumerate(vocab)}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (ART / "merges.txt").write_text(
        "\n".join(f"{a} {b}" for a, b in merges) + "\n",
        encoding="utf-8",
    )

    print(f"\nvocab size: {len(vocab)}")
    print(f"wrote {ART / 'vocab.json'}")
    print(f"wrote {ART / 'merges.txt'}")
    print("next: 04_use_trained_bpe.py")


if __name__ == "__main__":
    main()
