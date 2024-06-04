#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the first 10 hot posts for a given subreddit."""

    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    user_agent = {'User-Agent': 'MyCustomUserAgent/0.1'}
    response = requests.get(url, headers=user_agent, params={'limit': 10},
                            allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json().get('data', {})
        children = data.get('children', [])

        if not children:
            print("None")
            return

        for post in children:
            print(post.get('data', {}).get('title', "None"))

    except ValueError:
        print("None")
