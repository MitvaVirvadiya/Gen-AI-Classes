"""02 — spaCy is linguistic tokenization, not LLM tokenization.

This is the idea from tokenization/text-tokens.py, kept here so the
lesson is self-contained. spaCy answers 'what are the words?'.
An LLM tokenizer answers 'what IDs did this model train on?'.

Optional:
    pip install spacy
    python -m spacy download en_core_web_sm

If spaCy is missing we fall back to a regex splitter and still make the point.
"""

from __future__ import annotations

import re

CORPUS = "Python is amazing. I have been learning NLP for 2 months!"


def spacy_tokens(text: str) -> list[tuple]:
    import spacy

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [(t.text, t.is_alpha, t.is_digit, t.is_punct) for t in doc]


def naive_word_tokens(text: str) -> list[str]:
    return re.findall(r"\w+|[^\w\s]", text, flags=re.UNICODE)


def main() -> None:
    print("CORPUS:", CORPUS)
    try:
        tokens = spacy_tokens(CORPUS)
        print(f"\nspaCy produced {len(tokens)} tokens:")
        for row in tokens:
            print(" ", row)
        source = "spaCy"
    except Exception as exc:  # noqa: BLE001 — demo should still run
        tokens = naive_word_tokens(CORPUS)
        print(f"\nspaCy not available ({exc}). Regex fallback, {len(tokens)} tokens:")
        print(" ", tokens)
        source = "regex-words"

    print(
        f"\n{source} is useful for linguistics (words, punct, POS).\n"
        "It is the wrong budget for an LLM context window and the wrong\n"
        "IDs for any pretrained model. Script 03 trains the right kind."
    )


if __name__ == "__main__":
    main()
