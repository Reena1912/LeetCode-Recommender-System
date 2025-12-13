from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="LeetCode Recommender API")

@app.get("/")
def health():
    return {"status": "running"}

@app.get("/recommend")
def recommend():
    # Load data
    problems = pd.read_csv("data/leetcode_problem_list.csv")
    history = pd.read_csv("data/merged_full_history.csv")
    failure_rates = pd.read_csv("data/topic_failure_rates.csv")

    # weakest topic
    weakest_topic = failure_rates.iloc[0]["topics"]

    # solved problems
    solved = set(
        history[history["status"] == "Accepted"]["slug"].dropna().unique()
    )

    # filter
    candidates = problems[
        problems["topics"].str.contains(weakest_topic, na=False)
        & ~problems["slug"].isin(solved)
    ]

    # difficulty fallback
    for level in ["EASY", "MEDIUM"]:
        choice = candidates[candidates["difficulty"] == level]
        if not choice.empty:
            row = choice.iloc[0]
            return {
                "topic": weakest_topic,
                "title": row["title"],
                "difficulty": row["difficulty"],
                "slug": row["slug"]
            }

    return {"message": "No recommendation found"}
