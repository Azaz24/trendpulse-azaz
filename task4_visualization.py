# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 2: Load data
df = pd.read_csv("data/trends_analysed.csv")

# Step 3: Create output folder
if not os.path.exists("outputs"):
    os.makedirs("outputs")

    # Step 4: Chart 1 - Top 10 stories by score

top10 = df.nlargest(10, "score")

plt.figure(figsize=(10,5))
plt.barh(top10["title"].astype(str).str[:50], top10["score"])
plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Title")

plt.savefig("outputs/chart1_top_stories.png")
plt.show()

# Step 5: Chart 2 - Stories per category

category_counts = df["category"].value_counts()

plt.figure(figsize=(8,5))
plt.bar(category_counts.index, category_counts.values)
plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Count")

plt.savefig("outputs/chart2_categories.png")
plt.show()

# Step 6: Chart 3 - Scatter plot

colors = df["is_popular"].map({True: "green", False: "red"})

plt.figure(figsize=(8,5))
plt.scatter(df["score"], df["num_comments"], c=colors)
plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Comments")

plt.savefig("outputs/chart3_scatter.png")
plt.show()

# Step 7: Dashboard (All charts together)

fig, axs = plt.subplots(1, 3, figsize=(18,5))

# Chart 1
axs[0].barh(top10["title"].astype(str).str[:30], top10["score"])
axs[0].set_title("Top Stories")

# Chart 2
axs[1].bar(category_counts.index, category_counts.values)
axs[1].set_title("Categories")

# Chart 3
axs[2].scatter(df["score"], df["num_comments"], c=colors)
axs[2].set_title("Score vs Comments")

plt.tight_layout()
plt.suptitle("TrendPulse Dashboard", y=1.05)

plt.savefig("outputs/dashboard.png")
plt.show()