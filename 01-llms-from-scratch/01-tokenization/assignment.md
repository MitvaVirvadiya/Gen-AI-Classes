# Assignment 1.1 — Tokenization

Do this after you have run `01` through `04`. `05` is extra credit if
`tiktoken` / `transformers` installed.

Write your answers under **My answers**. This file is the record.

## A. From memory

1. In one sentence, what is a tokenizer?
2. Why do word-level tokenizers fail on real text? Give two reasons.
3. Why not just use bytes and skip BPE?
4. Why must a model and its tokenizer stay paired?

## B. Run and record

Run:

```bash
python 01-llms-from-scratch/01-tokenization/code/03_bpe_from_scratch.py
python 01-llms-from-scratch/01-tokenization/code/04_use_trained_bpe.py
```

5. How many merges did you train? What was the first merge? Why that pair?
6. Encode `low lower newest widest` (already in the script). Paste the
   token pieces, not just the IDs.
7. Encode a word the corpus barely prepared for, e.g. `lowesting`.
   What happened? Is that a bug?

## C. Think like a bill

8. Which of these would you expect to use *more* tokens in a GPT-style
   English BPE tokenizer? Guess first, then check with `05` if you can.

   - `hello`
   - `antidisestablishmentarianism`
   - `你好`
   - `def foo(x):`
   - `😀`
9. A page of English is often ~500–800 tokens, not ~300 words. Why are
   those numbers different?

## D. Contrast with your old code

10. Take the corpus from `tokenization/text-tokens.py`:

    `Python is amazing. I have been learning NLP for 2 months!`

    - How many spaCy tokens?
    - How many BPE tokens from *your* trained toy BPE?
    - How many tiktoken tokens (`cl100k_base` or `o200k_base`) if you ran `05`?

    Why do the three numbers disagree? Which number would you use to
    budget a context window?

## E. Stretch (optional, do not block Lesson 1.2)

11. Change `NUM_MERGES` in `03_bpe_from_scratch.py` to 5 and to 80.
    Encode the same sentence. What happens to sequence length?
12. Name one production bug you now expect to see if someone strips
    leading spaces from every user message before tokenizing.

## Done when

- [ ] A–D answered in this file
- [ ] You can explain BPE to a friend without opening the notes
- [ ] `PROGRESS.md` 1.1 is ticked

## My answers

1. converts words, sentences into tokens
2. first - more tokens in use, second - same meaning words counted as seprate token
3. bytes can make tokens library size huge
4. as tokens are models vocabulary it must be synced
5. 40 merges trained, first is l + 0, dont knwo why it was paired
6. ['low</w>', 'lower</w>', 'new', 'est</w>', 'wid', 'est</w>']
7. it had a lot of token IDs for a single word its bug
8. ​​😀
9. becuase words count doesn't mean token count 
10. the one with cl100k_base or o200k_base
11. vocab size increase and decearse with change in num merge

<!-- write below -->
