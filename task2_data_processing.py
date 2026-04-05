import pandas as pd

# Step 1: Load JSON dataset
# This loads raw trending data from Task 1 output file into a DataFrame
file_path = "data/trends_20260405.json"
df = pd.read_json(file_path)

print(f"Loaded {len(df)} stories from {file_path}")

# Step 2: Remove duplicate posts based on post_id
df = df.drop_duplicates(subset="id")
print(f"After removing duplicates: {len(df)}")

# Step 3: Remove missing values
# Drop rows where important fields are missing (id, title, score)
df = df.dropna(subset=["id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Step 4: Filter low quality posts (score < 5)
# Keep only meaningful/trending posts with decent engagement
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Step 5: Clean text fields
df["title"] = df["title"].str.strip()

# Convert numeric columns to proper integer type
df["score"] = df["score"].astype(int)
df["comments"] = df["comments"].astype(int)

# Step 6: Save cleaned dataset
# Export final cleaned data into CSV for analysis (Task 3)
output_path = "data/trends_clean.csv"
df.to_csv(output_path, index=False)

print("\nStories per category:")
print(df["category"].value_counts())

print(f"\nSaved {len(df)} rows to {output_path}")