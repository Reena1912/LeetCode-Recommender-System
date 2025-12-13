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
# SMART RECOMMENDER
# -----------------------------

def recommend_problem():
    """
    Recommends a problem using:
    - weakest topic first
    - EASY → MEDIUM fallback
    - moves to next topic if exhausted
    """

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

            if not candidates.empty:
                rec = candidates.sample(1).iloc[0]

                return {
                    "topic": topic,
                    "title": rec["title"],
                    "slug": rec["slug"],
                    "difficulty": rec["difficulty"],
                    "url": f"https://leetcode.com/problems/{rec['slug']}/"
                }

    return None

# -----------------------------
# RUN
# -----------------------------

result = recommend_problem()

if result:
    print("\n🔥 SMART AUTO-RECOMMENDED PROBLEM")
    print("--------------------------------")
    print(f"Topic      : {result['topic']}")
    print(f"Title      : {result['title']}")
    print(f"Difficulty : {result['difficulty']}")
    print(f"URL        : {result['url']}")
else:
    print("🎉 No suitable problems found. You're too strong 😄")
