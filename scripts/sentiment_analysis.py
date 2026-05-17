import pandas as pd
from transformers import pipeline

df = pd.read_csv("data/raw/clean_reviews.csv")

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

sample_df = df.head(400)

results = []

for review in sample_df["review"]:
    result = classifier(str(review))[0]

    label = result["label"]
    score = result["score"]

    results.append({
        "sentiment_label": label,
        "sentiment_score": score
    })

sentiment_df = pd.DataFrame(results)

final_df = pd.concat(
    [sample_df.reset_index(drop=True), sentiment_df],
    axis=1
)

print(final_df.head())

final_df.to_csv(
    "data/raw/sentiment_results.csv",
    index=False
)