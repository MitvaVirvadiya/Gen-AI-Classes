# Fine-tune with PEFT / TRL

## One-sentence truth

`trl.SFTTrainer` + `peft.LoraConfig` is the standard open-source way
to do Lessons 2.1 and 2.2 without writing a training loop.

## Do this again

```python
from peft import LoraConfig
from trl import SFTTrainer, SFTConfig

peft = LoraConfig(r=16, lora_alpha=32, target_modules="all-linear")
args = SFTConfig(output_dir="out", max_steps=50, per_device_train_batch_size=1)
trainer = SFTTrainer(model=model, args=args, train_dataset=ds, peft_config=peft)
trainer.train()
trainer.save_model()   # adapter, not a full 14 GB copy
```

Load later with `PeftModel.from_pretrained(base, "out")`.

---

## What we will insist on in the lab

1. Print one tokenized sample (prompt masked in labels)
2. Overfit 20 rows until loss crashes toward 0 — proves the pipe
3. Only then train on more data
4. Save a 5-prompt eval before and after

If you cannot overfit 20 rows, the pipeline is wrong. Do not add data.
