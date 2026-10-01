# Automated ML results (KNN only)

- Job name: knn-automl-iram15-v3
- Best algorithm (scaler + model):
- n_neighbors:
- weights:
- AUC weighted:
- Test recall (failure class):
- Test F1 (failure class):
- Observation: what did AutoML choose differently from my notebook?

## Issues faced
1. First job failed: target column was read as string, so values looked empty.
2. Second job failed: "All allow-listed algorithms are incompatible with sparse datasets" (one-hot encoding of `type` with KNN only).
3. Fix: encoded `type` as 0/1/2 in a new MLTable asset (ai4i-maintenance-numeric).
