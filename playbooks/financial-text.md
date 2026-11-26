# Test a text or sentiment feature

**Inputs.** Time-stamped issuer text with source identifiers and a labeled evaluation sample.

1. Deduplicate syndicated text and record the first verified publication time. Keep issuer statements separate from commentary.
2. Compare a financial-language model with a simple text baseline. Review negations, guidance language and mixed-sentiment passages.
3. If studying returns, join the frozen feature to later market observations. Evaluate classification and financial prediction separately.

**Acceptance check.** Report class-level errors and the effect of duplicates on the result. Check model-weight and dataset terms before redistribution.

**Upstream resources.** [FinBERT (ProsusAI)](https://huggingface.co/ProsusAI/finbert) · [Financial PhraseBank](https://huggingface.co/datasets/takala/financial_phrasebank) · [trafilatura](https://github.com/adbar/trafilatura)
