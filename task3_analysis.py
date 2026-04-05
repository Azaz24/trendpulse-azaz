# Step 1: Import libraries
import pandas as pd
import numpy as np

# Step 2: Load data
df = pd.read_csv("data/trends_clean.csv")

df.rename(columns={
    "descendants": "num_comments",
    "comments": "num_comments"
}, inplace=True)

print(df.columns)
# Step 3: Basic analysis
print("First 5 rows:")
print(df.head())

print("\nShape:", df.shape)

print("\nAverage score:", df["score"].mean())
print("Average comments:", df["num_comments"].mean())

# Step 4: Category insights
print("\nCategory count:")
print(df["category"].value_counts())

# Step 5: NumPy stats
print("\n--- NumPy Stats ---")
print("Mean:", np.mean(df["score"]))
print("Median:", np.median(df["score"]))
print("Std:", np.std(df["score"]))

print("Max:", np.max(df["score"]))
print("Min:", np.min(df["score"]))

# Step 6: Extra analysis
df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > df["score"].mean()

df.to_csv("data/trends_analysed.csv", index=False)

print("\nSaved successfully!")