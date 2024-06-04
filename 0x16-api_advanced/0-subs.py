#!/usr/bin/python3

"""How many subs are in a given subreddit using the Reddit api"""
import requests


def number_of_subscribers(subreddit):
    """returns How many subs"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        return 0

    data = response.json().get("data", {})
    return data.get("subscribers", 0)
