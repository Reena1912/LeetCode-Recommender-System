import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from recommend import recommend_problem

def test_recommend_returns_list():
    results = recommend_problem(top_n=1)
    assert isinstance(results, list)

def test_recommend_top_n():
    results = recommend_problem(top_n=3)
    assert len(results) <= 3

def test_recommend_has_required_keys():
    results = recommend_problem(top_n=1)
    if results:
        keys = results[0].keys()
        assert "topic" in keys
        assert "title" in keys
        assert "difficulty" in keys
        assert "url" in keys

def test_recommend_difficulty_is_valid():
    results = recommend_problem(top_n=5)
    for r in results:
        assert r["difficulty"] in ["EASY", "MEDIUM", "HARD"]

def test_recommend_url_format():
    results = recommend_problem(top_n=1)
    if results:
        assert results[0]["url"].startswith("https://leetcode.com/problems/")
