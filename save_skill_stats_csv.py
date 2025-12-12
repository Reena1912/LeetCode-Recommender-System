#total history how much solved in each skill category-----leetcode_history.csv


import requests
import csv
import os


# CONFIG


SESSION = "<your_session_cookie_here>"

os.makedirs("data", exist_ok=True)

url = "https://leetcode.com/graphql"

headers = {
    "Content-Type": "application/json",
    "Cookie": f"LEETCODE_SESSION={SESSION}"
}

payload = {
    "operationName": "skillStats",
    "query": """
    query skillStats($username: String!) {
      matchedUser(username: $username) {
        tagProblemCounts {
          advanced { tagName tagSlug problemsSolved }
          intermediate { tagName tagSlug problemsSolved }
          fundamental { tagName tagSlug problemsSolved }
        }
      }
    }
    """,
    "variables": {"username": "NovaAsher"}
}


# ---------------------------
# FETCH
# ---------------------------

res = requests.post(url, json=payload, headers=headers)
data = res.json()

tag_data = data["data"]["matchedUser"]["tagProblemCounts"]

rows = []

for level in ["fundamental", "intermediate", "advanced"]:
    for item in tag_data[level]:
        rows.append({
            "category": level,
            "tagName": item["tagName"],
            "tagSlug": item["tagSlug"],
            "problemsSolved": item["problemsSolved"],
        })

# ---------------------------
# SAVE CSV
# ---------------------------

csv_path = "data/leetcode_history.csv"

with open(csv_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, 
        fieldnames=["category", "tagName", "tagSlug", "problemsSolved"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Skill stats saved → {csv_path}")
