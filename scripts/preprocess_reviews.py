import pandas as pd

df = pd.read_csv("data/raw/raw_reviews.csv")

print("Original shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates(subset="review_id")

# Remove missing values
df = df.dropna(subset=["review", "rating"])

# Normalize date
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# Keep required columns
df = df[["review", "rating", "date", "bank", "source"]]

print("Cleaned shape:", df.shape)

df.to_csv("data/raw/clean_reviews.csv", index=False)