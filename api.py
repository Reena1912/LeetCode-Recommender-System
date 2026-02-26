from fastapi import FastAPI
from recommend import recommend_problem
import pandas as pd

app = FastAPI(title="LeetCode Recommender API")

# Load data once at startup
history_df = pd.read_csv("data/merged_full_history.csv")
failure_df = pd.read_csv("data/topic_failure_rates.csv")

@app.get("/")
def health():
    return {"status": "running"}

@app.get("/recommend")
def recommend(top: int = 3):
    results = recommend_problem(top_n=top)
    if not results:
        return {"message": "No problems left! You're crushing LeetCode!"}
    return {"recommended_problems": results}

@app.get("/stats")
def get_stats():
    total_solved = int((history_df["status"] == "Accepted").sum())
    total_failed = int((history_df["status"] != "Accepted").sum())
    total_attempts = len(history_df)

    weak_topics = failure_df.sort_values("failure_rate", ascending=False).head(5)
    weak_list = [
        {
            "topic": row["topics"],
            "failure_rate": round(float(row["failure_rate"]) * 100, 1),
            "total_attempts": int(row.get("total", 0))
        }
        for _, row in weak_topics.iterrows()
    ]

    return {
        "summary": {
            "total_attempts": total_attempts,
            "total_solved": total_solved,
            "total_failed": total_failed,
            "overall_success_rate": round((total_solved / total_attempts) * 100, 1)
        },
        "weakest_topics": weak_list
    }
