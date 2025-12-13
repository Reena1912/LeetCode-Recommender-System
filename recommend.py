import argparse
import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------

history_df = pd.read_csv("data/merged_full_history.csv")
problem_df = pd.read_csv("data/leetcode_problem_list.csv")
failure_df = pd.read_csv("data/topic_failure_rates.csv")

# -----------------------------
# PREPROCESS
# -----------------------------

problem_df["topics"] = problem_df["topics"].fillna("").apply(
    lambda x: x.split(",") if x else []
)

ACCEPTED_SLUGS = set(
    history_df[history_df["status"] == "Accepted"]["slug"]
    .dropna()
    .unique()
)

failure_df = failure_df.sort_values(
    by="failure_rate",
    ascending=False
)

# -----------------------------
# RECOMMENDER LOGIC
# -----------------------------

def recommend_problem(top_n=1):
    recommendations = []

    for _, row in failure_df.iterrows():
        topic = row["topics"]

        topic_problems = problem_df[
            problem_df["topics"].apply(lambda x: topic in x)
        ]

        unsolved = topic_problems[
            ~topic_problems["slug"].isin(ACCEPTED_SLUGS)
        ]

        if unsolved.empty:
            continue

        for difficulty in ["EASY", "MEDIUM"]:
            candidates = unsolved[
                unsolved["difficulty"] == difficulty
            ]

            for _, prob in candidates.iterrows():
                recommendations.append({
                    "topic": topic,
                    "title": prob["title"],
                    "difficulty": prob["difficulty"],
                    "url": f"https://leetcode.com/problems/{prob['slug']}/"
                })

                if len(recommendations) >= top_n:
                    return recommendations

    return recommendations

# -----------------------------
# CLI INTERFACE
# -----------------------------

def main():
    parser = argparse.ArgumentParser(
        description=" LeetCode Problem Recommender (based on your weaknesses)"
    )

    parser.add_argument(
        "--top",
        type=int,
        default=1,
        help="Number of problems to recommend (default: 1)"
    )

    args = parser.parse_args()

    results = recommend_problem(top_n=args.top)

    if not results:
        print(" No problems left to recommend. You're crushing LeetCode!")
        return

    print("\n RECOMMENDED PROBLEMS")
    print("-" * 40)

    for i, r in enumerate(results, 1):
        print(f"\n#{i}")
        print(f"Topic      : {r['topic']}")
        print(f"Title      : {r['title']}")
        print(f"Difficulty : {r['difficulty']}")
        print(f"URL        : {r['url']}")

if __name__ == "__main__":
    main()
