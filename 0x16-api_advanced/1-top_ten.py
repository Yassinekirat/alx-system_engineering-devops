#!/usr/bin/python3
"""
prints the titles of he first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """returns the first 10 hot posts"""

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    user_agent = {'User-Agent': 'Google Chrome Version 125.0.6422.114'}
    response = requests.get(url, headers=user_agent, params={'limit': 10})

    if 'data' in response.json():
        for posts in response.json().get('data').get('children'):
            print(posts.get('data').get('title'))

    else:
        print(None)
