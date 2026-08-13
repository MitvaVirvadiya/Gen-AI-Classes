"""01 — Why tokenize?

A model cannot multiply letters. Compare three naive splits of the same
string: raw bytes, unicode characters, whitespace words.

Run:
    python 01-llms-from-scratch/01-tokenization/code/01_why_tokenize.py
"""

TEXT = "Python is amazing. I have been learning NLP for 2 months! 你好 😀"


def show(title: str, pieces: list) -> None:
    print(f"\n=== {title} ({len(pieces)} pieces) ===")
    print(pieces[:24], "..." if len(pieces) > 24 else "")


def main() -> None:
    print("INPUT:", repr(TEXT))

    show("utf-8 bytes", list(TEXT.encode("utf-8")))
    show("unicode characters", list(TEXT))
    show("whitespace words", TEXT.split())

    print(
        "\nNotice:\n"
        "- bytes always work (256 symbols) but sequences get long\n"
        "- characters still explode on '你好' and the emoji (multi-byte)\n"
        "- words look nice until a new word, a typo, or 'NLP' vs 'nlp'\n"
        "BPE (script 03) sits between these extremes."
    )


if __name__ == "__main__":
    main()
