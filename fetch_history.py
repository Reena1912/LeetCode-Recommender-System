# This script fetches the user's submission history from LeetCode
# and saves it as a CSV file containing:
# id, title, slug, status, language, runtime, timestamp

import requests
import csv
import time
import os

# ---------------------------
# CONFIG
# ---------------------------

SESSION = "<your_session_cookie_here>"
headers = {
    "Content-Type": "application/json",
    "Cookie": f"LEETCODE_SESSION={SESSION}",
    "Referer": "https://leetcode.com",
}

# NEW: Correct & working GraphQL query
query = """
query submissionList($offset: Int!, $limit: Int!) {
  submissionList(offset: $offset, limit: $limit) {
    submissions {
      id
      title
      titleSlug
      statusDisplay
      lang
      runtime
      timestamp
    }
    hasNext
  }
}
"""

# ---------------------------
# SAVE INSIDE /data
# ---------------------------

os.makedirs("data", exist_ok=True)
csv_path = "data/leetcode_submission_history.csv"

def fetch_batch(offset):
    body = {
        "query": query,
        "variables": {"offset": offset, "limit": 20},
    }
    res = requests.post("https://leetcode.com/graphql", json=body, headers=headers)
    try:
        return res.json()
    except:
        print("❌ JSON decode error:", res.text)
        return None

# ---------------------------
# FETCH LOOP
# ---------------------------

all_rows = []
offset = 0

while True:
    print(f"Fetching offset={offset}")
    data = fetch_batch(offset)

    if not data or "errors" in data:
        print("❌ Error reading response:", data)
        break

    submissions = data["data"]["submissionList"]["submissions"]
    if not submissions:
        break

    for s in submissions:
        all_rows.append([
            s["id"],
            s["title"],
            s["titleSlug"],
            s["statusDisplay"],
            s["lang"],
            s["runtime"],
            s["timestamp"],
        ])

    if not data["data"]["submissionList"]["hasNext"]:
        break

    offset += 20
    time.sleep(1)

# ---------------------------
# WRITE CSV
# ---------------------------

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "title", "slug", "status", "language", "runtime", "timestamp"])
    writer.writerows(all_rows)

print(f"✅ Saved submission history → {csv_path}")
