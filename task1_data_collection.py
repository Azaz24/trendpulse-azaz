
# STEP 1: Import Libraries

import requests
import json
import os
import time
from datetime import datetime



# STEP 2: Fetch Top Story IDs

print("Fetching top stories...")

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent": "trendpulse"}

response = requests.get(url, headers=headers, timeout=5)

if response.status_code != 200:
    print("Error fetching story IDs")
    story_ids = []
else:
    story_ids = response.json()[:500]   # Should be More IDs (important)



# STEP 3: Define Categories

categories = {
    "technology": ["ai", "tech", "software", "code"],
    "worldnews": ["war", "election", "government"],
    "sports": ["game", "team", "player"],
    "science": ["research", "space", "nasa"],
    "entertainment": ["movie", "music", "show"]
}


# STEP 4: Initialize Storage

results = []
print("Processing stories...")



# STEP 5: Fetch + Categorize

for sid in story_ids:
    try:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
        res = requests.get(story_url, headers=headers, timeout=5)

        if res.status_code != 200:
            continue

        data = res.json()
        title = data.get("title", "").lower()

        print("Processing:", sid)

        for category, keywords in categories.items():
            if any(word in title for word in keywords):

                story = {
                    "id": data.get("id"),
                    "title": data.get("title"),
                    "category": category,
                    "score": data.get("score", 0),
                    "comments": data.get("descendants", 0),
                    "author": data.get("by"),
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M")
                }

                results.append(story)
                break   # Only one category should be received

        #  STOP CONDITION 
        if len(results) >= 100:
            break

        time.sleep(0.1)

    except Exception as e:
        print("Error:", e)



# STEP 6: Save Data

print("Saving data...")

os.makedirs("data", exist_ok=True)

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(results, f, indent=4)



# STEP 7: Final Output

print("Done ✅")
print(f"Collected {len(results)} stories")
print(f"Saved to: {filename}")