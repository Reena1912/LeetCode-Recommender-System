# LeetCode-Recommender-System

A personalized recommendation system that analyzes your LeetCode submissions, understands your strengths and weaknesses by topic, difficulty, and performance, and recommends the best next problems to practice.
1) Fetch full LeetCode problem list using GraphQL API
2) save-skill-stats-csv.py = this file contains total history of how much solved in each skill category like category,tagName,tagSlug,problemsSolved(fundamental,Array,array,62) and creates a csv with the name "leetcode_history.csv"
3) fetch_history.py = this script fetches the user's submission history from LeetCode like  about id,title,slug,status,language,runtime,timestamp(1853674747,Increasing Triplet Subsequence,increasing-triplet-subsequence,Accepted,python3,14 ms,1765537402) and saves it as a CSV file named as "leetcode_submission_history.csv".
4) fetch_problem_list.py = this script fetches the complete list of problems from LeetCode and saves it as a CSV file named "leetcode_problem_list.csv"
5) merged.py =  this script merges the user's submission history with the complete problem list from LeetCode based on the problem slug. the merged file name is "merged_full_history.csv". (id,title_x,slug,status,language,runtime,timestamp,title_y,difficulty,topics)
