# Dataset Notes

## Ham dataset
- Source: Enron Email Dataset
- Purpose: legitimate email samples

## Phishing dataset
- Source: [Kaggle]
- Purpose: phishing email samples

## Planned label mapping
- 0 = ham
- 1 = phishing



## Dataset observations

- The Kaggle dataset contains both label 0 and label 1.
- Class counts are relatively balanced.
- For the baseline model, I am using this dataset directly instead of combining a separate ham dataset.
- The text column used for modeling is `text`.

## Current working dataset

Using `phishing_email.csv` as the main baseline dataset.

### Columns used
- `text_combined` → renamed to `text`
- `label`

### Class distribution
- label 1: 42891
- label 0: 39595

### Note
This dataset already contains both classes, so a separate ham dataset is not required for the baseline model.


## Preprocessing summary

Working dataset:
- `combined_raw_emails.csv`

Cleaned dataset:
- `emails_cleaned_full.csv`

Train/test files:
- `train_emails.csv`
- `test_emails.csv`

Cleaning steps:
- lowercasing
- HTML stripping
- URL replacement
- email replacement
- number replacement
- whitespace normalization

Split:
- 80/20 train/test
- stratified by label

