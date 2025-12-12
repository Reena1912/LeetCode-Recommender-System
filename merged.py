#merged.py this script merges the user's submission history with the complete problem list from LeetCode based on the problem slug.
#the merged file name is merged_full_history.csv
import pandas as pd

# Load files
sub_df = pd.read_csv("data/leetcode_submission_history.csv")  
prob_df = pd.read_csv("data/leetcode_problem_list.csv")

# Merge on slug
merged_df = pd.merge(sub_df, prob_df, on="slug", how="left")

# Save merged file
merged_df.to_csv("data/merged_full_history.csv", index=False)

print("✅ Merged dataset saved as data/merged_full_history.csv")
print("Rows:", len(merged_df))
print("\nSample:")
print(merged_df.head())
