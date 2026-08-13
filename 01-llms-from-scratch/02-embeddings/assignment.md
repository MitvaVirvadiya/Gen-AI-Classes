# Assignment 1.2 — Embeddings

Run `01_lookup_table.py` and `02_cosine_neighbors.py` first.

## A. From memory

1. What is the shape of the embedding matrix, and what does each axis mean?
2. Why can't the model just use token IDs as numbers?
3. What is the difference between a token embedding and a contextual embedding?
4. Why is cosine usually preferred over Euclidean distance here?

## B. Run and record

5. In `01_lookup_table.py`, what shape do you get for a batch of 2 sentences
   with 4 tokens each, `d_model=8`? Write the shape.
6. Change `d_model` to 2 and print one row of `E`. Are the numbers
   meaningful yet? Why / why not?
7. From `02_cosine_neighbors.py`, which toy word is nearest to `cat`?
   Which is nearest to `king`? Does that match the 2-D sketch in the data?

## C. Think

8. A 128_000 vocab, `d_model = 4096`, float32. Roughly how many
   **parameters** and **megabytes** is the embedding table alone?
   (4 bytes per float32.)
9. You average the token embeddings of a sentence to retrieve documents.
   Name one query where that will fail.

## D. Stretch

10. Implement `nearest(query, table, k=3)` yourself in five lines
    without looking at `02`. Paste it here.

## Done when

- [ ] A–C answered
- [ ] You can write `x = E[ids]` and a cosine function on a blank file
- [ ] `PROGRESS.md` 1.2 is ticked

## My answers

1.

2.

3.

4.

5.

6.

7.

8.

9.

10.
