# LeetCode-Recommender-System

A personalized recommendation system that analyzes your LeetCode submissions, understands your strengths and weaknesses by topic, difficulty, and performance, and recommends the best next problems to practice.

1. Fetch full LeetCode problem list using GraphQL API

2. save-skill-stats-csv.py = this file contains total history of how much solved in each skill category like category,tagName,tagSlug,problemsSolved(fundamental,Array,array,62) and creates a csv with the name "leetcode_history.csv"

3. fetch_history.py = this script fetches the user's submission history from LeetCode like about id,title,slug,status,language,runtime,timestamp(1853674747,Increasing Triplet Subsequence,increasing-triplet-subsequence,Accepted,python3,14 ms,1765537402) and saves it as a CSV file named as "leetcode_submission_history.csv".

4. fetch_problem_list.py = this script fetches the complete list of problems from LeetCode and saves it as a CSV file named "leetcode_problem_list.csv"

5. merged.py = this script merges the user's submission history with the complete problem list from LeetCode based on the problem slug. the merged file name is "merged_full_history.csv". (id,title_x,slug,status,language,runtime,timestamp,title_y,difficulty,topics)

6. bye running the merged.py file we will get all the data that we need

7. topic_analysis.py = Problems can have multiple topics:array, greedy They are unnested using: df.explode("topics") Result:1. One row per (submission × topic) 2.Enables accurate per-topic statistics
8. Failure Analysis-The data is grouped by:topics × status
    This reveals:Total attempts per topic, Accepted vs failed counts, Weakest topics based on failure rate

9.  Topic Failure Rates- you now have a ranked list of topics you suck at the most- it sees you have an 83% failure rate in depth-first search


10. next process is to build the recommendation logic


11. steps 
 1.  *Data Gathering*:  pulled two datasets - your personal submission history, and a master list of all LeetCode problems with their topics/difficulty.
 2.  *Data Merging & Cleaning*: combined these two datasets into one, using the problem 'slug' to link them. This gave you a single file with every attempt you ever made, plus the topics for that problem.
 3.  *The Analysis: This was the core insight.  calculated 'failure rate' for every single topic to find out *quantitatively where you struggle the most.
 4.  *The Recommendation Logic*:  wrote a function that takes your #1 weakest topic, finds all the 'Easy' problems for it that you haven't solved yet, and picks one for you to practice.
 5.  *Automation*:  tied it all together. The final script automatically finds your weakest spot from the analysis file and runs the recommender on it, printing out a targeted problem.



 Anyone can run it locally by cloning the repo, installing dependencies, adding their own LeetCode session cookie, and running the pipeline scripts. The recommender then automatically analyzes their submission history and suggests problems based on their weakest topics.




