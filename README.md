# Customer Experience Analytics for Fintech Apps

## Overview

This project is part of the **10 Academy AI Mastery Week 2 Challenge**.
It focuses on analyzing Google Play Store reviews for Ethiopian banking apps to extract actionable insights about customer experience.

The goal is to transform raw user feedback into structured intelligence that helps product teams improve mobile banking apps.

---

## Objective

The project aims to:

* Analyze Ethiopian banking app reviews from Google Play Store
* Perform sentiment analysis on user feedback
* Extract recurring themes and pain points
* Generate actionable insights for product improvement

---

## Banks Analyzed

The following banking apps were analyzed:

* Commercial Bank of Ethiopia
* Bank of Abyssinia
* Dashen Bank

---

## Methodology

### 1. Data Collection

* Reviews were scraped from the Google Play Store using the `google-play-scraper` Python library.
* For each bank app, the following fields were collected:

  * Review text
  * Rating (1–5 stars)
  * Review date
  * Bank name
  * Source (Google Play Store)

---

### 2. Sentiment Analysis

* Sentiment classification was performed using:

  * `distilbert-base-uncased-finetuned-sst-2-english` (Hugging Face Transformer model)
* Each review was labeled as:

  * Positive
  * Negative
* A confidence score was also generated for each prediction.

---

### 3. Thematic Analysis

* Keyword extraction was performed using TF-IDF vectorization.
* Extracted n-grams (1–2 words) were used to identify recurring themes such as:

  * Login issues
  * Transaction delays
  * UI/UX feedback
  * Feature requests

---

### 4. Preprocessing

The raw dataset was cleaned by:

* Removing duplicate reviews using review ID
* Dropping rows with missing review text or rating
* Normalizing review dates to `YYYY-MM-DD` format
* Filtering relevant columns for analysis

---

## Folder Structure

```text
fintech-review-analytics/
├── .github/
│   └── workflows/
│       └── unittests.yml
├── data/
│   └── raw/
├── notebooks/
│   └── eda.ipynb
├── scripts/
│   ├── scrape_reviews.py
│   ├── preprocess_reviews.py
│   ├── sentiment_analysis.py
│   └── thematic_analysis.py
├── src/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Limitations

* Google Play Store scraping is subject to rate limits, which may restrict the number of reviews retrieved per app.
* Some reviews may be missing or incomplete due to API limitations.
* Reviews may include multiple languages, requiring additional preprocessing for multilingual handling.
* Sentiment models may misclassify context-heavy or sarcastic reviews.

---

## Next Steps

* Expand sentiment analysis with fine-tuned or domain-specific models
* Improve theme detection using topic modeling (LDA or BERTopic)
* Store processed data in PostgreSQL for production readiness
* Build dashboards for real-time monitoring of customer feedback

