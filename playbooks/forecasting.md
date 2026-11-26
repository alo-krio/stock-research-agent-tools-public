# Evaluate a forecasting model

**Inputs.** Timestamped features, a prediction target and the date at which each label matures.

1. Start with a simple persistence or historical-average prediction. Freeze the feature set and the test interval.
2. Train only on labels available by the training cutoff. Prevent overlapping forward labels from crossing the train/test boundary.
3. Evaluate the model and baseline on the same dates. Track missing predictions, uncertainty and errors across distinct market conditions.

**Acceptance check.** Keep model selection within the training period. Report performance on the untouched evaluation interval together with forecast coverage.

**Upstream resources.** [scikit-learn](https://github.com/scikit-learn/scikit-learn) · [Chronos / Chronos-Bolt](https://github.com/amazon-science/chronos-forecasting) · [statsmodels](https://github.com/statsmodels/statsmodels)
