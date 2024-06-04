#!/usr/bin/python3
"""recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively get all hot articles for a given subreddit."""

    if subreddit is None or not isinstance(subreddit, str):
        return (None)

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return (None)

    try:
        data = response.json().get('data', {})
        after = data.get('after')
        posts = data.get('children', [])

        for post in posts:
            hot_list.append(post.get('data', {}).get('title', "None"))

        if after:
            return (recurse(subreddit, hot_list, after))
        else:
            return (hot_list)
    except ValueError:
        return None
