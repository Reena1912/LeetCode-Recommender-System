# LeetCode Recommender System 🚀

**Built a LeetCode recommender system that analyzes submission history, identifies weak topics using failure-rate analytics, and dynamically recommends unsolved problems with difficulty fallback logic. Deployed a FastAPI backend on Railway with live Swagger documentation.**.

---

## 📌 What Does This Project Do?

* Reads LeetCode **submission history data**
* Merges it with **problem metadata** (topic, difficulty)
* Calculates **failure rates per topic**
* Identifies **weak areas** (e.g., DFS, DP, Graphs)
* Recommends **new, unsolved problems** from weak topics
* Applies **difficulty fallback** (Easy → Medium → Hard)
* Exposes functionality via a **FastAPI REST API**

---

## 🧠 Problem Statement

LeetCode users often struggle to decide:

* *Which topic should I practice next?*
* *Which problems match my weak areas?*

This system automates that decision using **data-driven analysis** instead of random problem selection.

---


## ⚙️ Tech Stack

* **Python 3.10+**
* **FastAPI** – REST API framework
* **Pandas** – Data processing & analysis
* **Uvicorn** – ASGI server
* **Railway** – Cloud deployment
* **Swagger (OpenAPI)** – API documentation

---

## 🔍 How Recommendations Work

1. Load submission history
2. Merge with problem topic & difficulty dataset
3. Compute per-topic:

   * Attempts
   * Failures
   * Success rate
4. Sort topics by **highest failure rate**
5. For weakest topic:

   * Recommend **unsolved Easy problems**
   * If none → fallback to Medium
   * If none → fallback to Hard

This ensures **progressive learning**, not frustration.

---

## 🚀 API Endpoints

### ✅ Health Check

```
GET /
```

Response:

```json
{ "status": "running" }
```

---

### 🎯 Recommend Problems

```
GET /recommend
```

Response (example):

```json
{
  "recommended_problems": [
    {
      "title": "Binary Tree Inorder Traversal",
      "topic": "Depth First Search",
      "difficulty": "Easy"
    }
  ]
}
```

---

## 📖 API Documentation (Swagger)

Live Swagger UI:
👉 [https://leetcode-recommender-system-production.up.railway.app/docs](https://leetcode-recommender-system-production.up.railway.app/docs)


---

## 🧪 How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Reena1912/LeetCode-Recommender-System.git
cd LeetCode-Recommender-System
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start API Server

```bash
uvicorn api:app --reload
```

Visit:

* API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## ☁️ Deployment (Railway)

Steps followed:

1. Push code to GitHub
2. Create Railway project
3. Connect GitHub repository
4. Set **Start Command**:

```bash
uvicorn api:app --host 0.0.0.0 --port $PORT
```

5. Railway auto-builds & deploys

Live URL:
👉 [https://leetcode-recommender-system-production.up.railway.app](https://leetcode-recommender-system-production.up.railway.app)

---



## 🧩 How Others Can Use This Project

1. Fork the repo
2. Add their own LeetCode submission CSVs locally
3. Run analysis scripts
4. Call `/recommend` endpoint
5. Get personalized problem recommendations

---
