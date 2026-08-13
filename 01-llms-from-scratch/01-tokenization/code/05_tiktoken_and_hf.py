"""05 — How production tokenizers count the same strings.

Optional extras:
    pip install tiktoken transformers

Run:
    python 01-llms-from-scratch/01-tokenization/code/05_tiktoken_and_hf.py
"""

from __future__ import annotations

SAMPLES = [
    "hello",
    "antidisestablishmentarianism",
    "你好",
    "def foo(x):",
    "😀",
    "Python is amazing. I have been learning NLP for 2 months!",
]


def try_tiktoken() -> None:
    try:
        import tiktoken
    except ImportError:
        print("tiktoken not installed — skip. pip install tiktoken")
        return

    # cl100k_base ≈ GPT-3.5/4. o200k_base ≈ GPT-4o family.
    for name in ("cl100k_base", "o200k_base"):
        try:
            enc = tiktoken.get_encoding(name)
        except Exception as exc:  # noqa: BLE001
            print(f"tiktoken {name} unavailable: {exc}")
            continue
        print(f"\n=== tiktoken {name} ===")
        for s in SAMPLES:
            ids = enc.encode(s)
            print(f"  {s!r:55} → {len(ids):3d}  {ids}")


def try_hf() -> None:
    try:
        from transformers import AutoTokenizer
    except ImportError:
        print("\ntransformers not installed — skip. pip install transformers")
        return

    model_id = "gpt2"  # tiny download, famous BPE
    print(f"\n=== Hugging Face {model_id} ===")
    tok = AutoTokenizer.from_pretrained(model_id)
    for s in SAMPLES:
        ids = tok.encode(s)
        print(f"  {s!r:55} → {len(ids):3d}  {ids}")


def main() -> None:
    print("Same strings. Different vocabularies. Different bills.")
    try_tiktoken()
    try_hf()
    print(
        "\nTakeaway: 'how many tokens is this?' is not a property of English.\n"
        "It is a property of (text, tokenizer)."
    )


if __name__ == "__main__":
    main()
