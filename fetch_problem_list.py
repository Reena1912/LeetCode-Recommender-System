##total problem list saved from leetcode
#fetch_problem_list.py this script fetches the complete list of problems from LeetCode and saves it as a CSV file.
#the csv file name is leetcode_problem_list.csv

import requests
import pandas as pd

query = """
query {
  problemsetQuestionListV2(
    categorySlug: ""
    limit: 5000
    skip: 0
  ) {
    questions {
      title
      titleSlug
      difficulty
      topicTags {
        name
        slug
      }
    }
  }
}
"""

url = "https://leetcode.com/graphql"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://leetcode.com",
    "Content-Type": "application/json"
}

response = requests.post(url, json={'query': query}, headers=headers)
data = response.json()

# Error handling
if "data" not in data or data.get("errors"):
    print("❌ LeetCode returned an error:")
    print(data)
    exit()

questions = data["data"]["problemsetQuestionListV2"]["questions"]

rows = []
for q in questions:
    rows.append({
        "title": q["title"],
        "slug": q["titleSlug"],
        "difficulty": q["difficulty"],
        "topics": ",".join([t["slug"] for t in q["topicTags"]])
    })

df = pd.DataFrame(rows)
df.to_csv("data/leetcode_problem_list.csv", index=False) 

print("✅ Saved: data/leetcode_problem_list.csv")
print("Total problems:", len(df))
