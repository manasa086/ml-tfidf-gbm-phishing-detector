# ml-tfidf-gbm-phishing-detector

A two-layer ensemble phishing detection system that closes the detection gap between traditional TF-IDF-based classifiers and AI-generated phishing emails.


## Overview

Traditional phishing detectors trained on vocabulary patterns (TF-IDF) fail against AI-generated phishing emails — recall drops from **98.96% → 89%** when the LinearSVM baseline is tested against 200 AI-crafted emails. This project builds a second detection layer using 13 hand-engineered structural features and a Gradient Boosting Classifier (GBM) that recovers the gap to **98% recall** on AI-generated phishing while maintaining 98.96% recall on traditional phishing.

---

## Key Results

| Model | Test Set | Recall | F1 Score |
|---|---|---|---|
| Baseline LinearSVM | Traditional (16K) | 98.96% | 98.73% |
| Baseline LinearSVM | AI Phishing (200) | 89.00% | 94.18% |
| Ensemble (SVM + GBM) | Traditional (16K) | 98.96% | 98.45% |
| Ensemble (SVM + GBM) | AI Phishing (50) | 98.00% | 98.99% |

---

## Project Structure

```
.
├── notebooks/
│   ├── 01_data_loading_and_inspection.ipynb     # Load & inspect Kaggle dataset (~82K emails)
│   ├── 02_preprocessing_and_split.ipynb         # Clean text, stratified 80/20 split
│   ├── 03_feature_extraction_and_baseline_models.ipynb  # TF-IDF + NB / LR / LinearSVM
│   ├── 04_ai_generated_phishing_test.ipynb      # Evaluate baseline on 200 AI phishing emails
│   └── 05_ai_phishing_aware_model.ipynb         # 13 structural features + GBM ensemble
├── data/
│   ├── raw/                                     # Kaggle phishing + Enron legitimate emails
│   ├── processed/                               # Cleaned train/test splits
│   └── generated/                               # AI phishing emails (200 + 150 holdout)
├── models/
│   ├── tfidf_vectorizer.pkl                     # Fitted TF-IDF (10K features)
│   ├── linear_svm_baseline.pkl                  # Baseline LinearSVM (F1=0.987)
│   └── ai_phishing_gbm.pkl                      # GBM structural classifier
├── results/
│   ├── figures/                                 # Performance charts, feature importance plots
│   └── metrics/                                 # CSV evaluation outputs
├── scripts/                                     # Helper scripts for data generation
├── environment.yml                              # Conda environment
└── requirements.txt.txt                         # pip dependencies
```

---

## Pipeline

Each notebook corresponds to one stage of the pipeline:

1. **Notebook 01** — Load the Kaggle phishing dataset (~82,000 emails). Inspect class distribution and email length statistics.
2. **Notebook 02** — Apply text cleaning (`clean_email_text`): lowercase, strip HTML via BeautifulSoup, tokenize URLs → `URL`, emails → `EMAIL`, numbers → `NUM`. Stratified 80/20 split.
3. **Notebook 03** — Fit TF-IDF (10K features, 1–2 n-grams). Train Naive Bayes, Logistic Regression, and LinearSVM. Select LinearSVM (best F1=0.987).
4. **Notebook 04** — Evaluate the saved baseline against 200 AI-generated phishing emails. Measure and document the recall drop.
5. **Notebook 05** — Extract 13 structural features. Train GBM (n_estimators=200, max_depth=4, learning_rate=0.1). Combine with LinearSVM via OR-fusion.

---

## Ensemble Architecture

```
         Input: Raw Email Text
                |
         [Preprocessing: clean_email_text()]
                |
         +------+------+
         |             |
   [Layer 1: TF-IDF    [Layer 2: 13 Structural
    + LinearSVM]        Features + GBM]
    Vocabulary          urgency_density, url_density,
    patterns            brand_count, cta_count, ...
         |             |
         +------+------+
                |
      [OR-Fusion Decision Rule]
      Phishing if Layer1=1 OR Layer2=1
                |
         +------+------+
         |             |
     PHISHING      LEGITIMATE
```

---

## 13 Structural Features

| Feature | Description |
|---|---|
| `url_count` / `url_density` | Number and proportion of URL tokens |
| `urgency_count` / `urgency_density` | Urgency keywords (urgent, expires, suspended, …) |
| `brand_count` / `brand_density` | Brand impersonation (PayPal, Amazon, Microsoft, …) |
| `cta_count` / `cta_density` | Call-to-action phrases (click here, verify now, …) |
| `email_count` | Number of EMAIL tokens |
| `num_count` | Number of NUM tokens |
| `char_count` | Total character count |
| `word_count` | Total word count |
| `avg_word_length` | Average word length |

Top driver: **urgency_density = 56.3%** of all GBM decisions.

---

## Setup

### Conda
```bash
conda env create -f environment.yml
conda activate phishing-detection
```

### pip
```bash
pip install -r requirements.txt.txt
```

### Run notebooks in order
```bash
jupyter notebook
```
Open and run notebooks `01` → `02` → `03` → `04` → `05` sequentially.

---

## Tech Stack

| Component | Tool |
|---|---|
| Language | Python 3.12 |
| ML Framework | scikit-learn 1.7 |
| Data Handling | pandas, numpy |
| HTML Parsing | BeautifulSoup4 |
| Visualization | matplotlib |
| Model Persistence | joblib |
| Version Control | Git / GitHub |

---

## Authors
- **Manasa Somisetty**
