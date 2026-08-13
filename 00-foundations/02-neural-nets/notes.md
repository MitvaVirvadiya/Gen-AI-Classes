# 0.2 Neural nets in one sitting

**Track:** 0 — Foundations
**Time:** 45 minutes
**Status:** gist notes

## One-sentence truth

A neural net is stacked linear layers with a nonlinearity between them.
Training is: predict, measure loss, send gradients backward, update weights.

## Do this again

When you see `FFN` or `MLP` inside a transformer block, this is that.

## One layer

```
h = activation(x @ W + b)
```

- `W` and `b` are the **parameters** (learned)
- `x` is the **input** (data)
- `activation` is ReLU, GELU, SiLU, ... — without it, stacked linears
  collapse into one linear map and cannot learn curves

## A tiny MLP

```
x          # (batch, 16)
h = relu(x @ W1 + b1)   # W1 is (16, 64)
y = h @ W2 + b2         # W2 is (64, 4)  → 4 logits
p = softmax(y)
loss = cross_entropy(p, target)
```

That is a classifier. A language model is the same picture with:

- input = embedding of tokens
- output size = vocab size
- target = the next token

## What "learning" is

1. Forward: compute `loss`
2. Backward: compute `dLoss/dW` for every parameter
3. Update: `W -= lr * dLoss/dW` (or AdamW)
4. Repeat on the next batch

After enough batches the weights become a compressed program that maps
inputs toward targets. There is no other magic.

## Overfitting, underfitting (one paragraph)

- **Underfit:** model too small or trained too little — cannot even fit train
- **Overfit:** memorizes train, fails on new text
- LLMs are so large they memorize *and* generalize. That tension is why
  we later care about eval sets, not just train loss.

## Regularization you will meet later

- **Dropout** — randomly zero activations in training (less common in modern LMs)
- **Weight decay** — AdamW's "keep weights small" term
- **LoRA** — refuse to touch most weights; train a tiny patch instead

## What a transformer adds (preview)

An MLP looks at one vector. A transformer block does:

1. Let every token look at other tokens (**attention**)
2. Then run an MLP on each token independently (**FFN**)
3. Add the input back each time (**residual**)

So Track 1 is: tokenization → vectors → "look at others" → MLP → stack.

## Done when

You can draw, from memory:

```
x → Linear → Act → Linear → softmax → loss
                 ↘ backprop updates W
```
