"""04 — Encode and decode with the BPE you just trained.

Run 03 first so artifacts/ exists.

    python 01-llms-from-scratch/01-tokenization/code/04_use_trained_bpe.py
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE.parent / "artifacts"


def load() -> tuple[dict[str, int], dict[int, str], list[tuple[str, str]]]:
    vocab = json.loads((ART / "vocab.json").read_text(encoding="utf-8"))
    id_to_tok = {i: t for t, i in vocab.items()}
    merges: list[tuple[str, str]] = []
    for line in (ART / "merges.txt").read_text(encoding="utf-8").splitlines():
        a, b = line.split(" ", 1)
        merges.append((a, b))
    return vocab, id_to_tok, merges


def apply_merges(symbols: list[str], merges: list[tuple[str, str]]) -> list[str]:
    for a, b in merges:
        glued = a + b
        i = 0
        out: list[str] = []
        while i < len(symbols):
            if i < len(symbols) - 1 and symbols[i] == a and symbols[i + 1] == b:
                out.append(glued)
                i += 2
            else:
                out.append(symbols[i])
                i += 1
        symbols = out
    return symbols


def encode_word(word: str, vocab: dict[str, int], merges: list[tuple[str, str]]) -> list[int]:
    symbols = apply_merges(list(word) + ["</w>"], merges)
    unk = vocab["<unk>"]
    return [vocab.get(s, unk) for s in symbols]


def encode(text: str, vocab: dict[str, int], merges: list[tuple[str, str]]) -> list[int]:
    ids: list[int] = []
    for word in text.split():
        ids.extend(encode_word(word, vocab, merges))
    return ids


def decode(ids: list[int], id_to_tok: dict[int, str]) -> str:
    pieces = [id_to_tok[i] for i in ids]
    text = "".join(pieces).replace("</w>", " ")
    return text.strip()


def show(label: str, text: str, vocab: dict[str, int], id_to_tok: dict[int, str], merges) -> None:
    ids = encode(text, vocab, merges)
    pieces = [id_to_tok[i] for i in ids]
    print(f"\n--- {label} ---")
    print("text   :", repr(text))
    print("pieces :", pieces)
    print("ids    :", ids)
    print("decode :", repr(decode(ids, id_to_tok)))


def main() -> None:
    if not (ART / "vocab.json").exists():
        raise SystemExit("Run 03_bpe_from_scratch.py first.")

    vocab, id_to_tok, merges = load()
    show("in-corpus words", "low lower newest widest", vocab, id_to_tok, merges)
    show("hello world", "hello world", vocab, id_to_tok, merges)
    show("unseen-ish", "lowesting", vocab, id_to_tok, merges)
    show("your old corpus", "Python is amazing. I have been learning NLP for 2 months!", vocab, id_to_tok, merges)

    print(
        "\nIf decode ≈ input (minus punctuation quirks), the map is reversible.\n"
        "'lowesting' should still encode: BPE falls back to smaller pieces."
    )


if __name__ == "__main__":
    main()
