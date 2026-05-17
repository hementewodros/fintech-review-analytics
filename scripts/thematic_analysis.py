import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("data/raw/clean_reviews.csv")

reviews = df["review"].astype(str)

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1,2),
    max_features=20
)

X = vectorizer.fit_transform(reviews)

keywords = vectorizer.get_feature_names_out()

print("Top Keywords:")
print(keywords)