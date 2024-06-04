#!/usr/bin/python3
"""
How many subs are in a given subreddit using the Reddit API.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://api.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyCustomUserAgent/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except ValueError:
        return 0
