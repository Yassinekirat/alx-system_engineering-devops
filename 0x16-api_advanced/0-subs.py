#!/usr/bin/python3

"""How many subs are in a given subreddit using the Reddit api"""
import requests


def number_of_subscribers(subreddit):
    """returns How many subs"""
    if subreddit is None or not type(subreddit) is str:
        return (0)
    
    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    user_agent = {'User-Agent': 'Google Chrome Version 125.0.6422.114'}
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code >= 300:
        return (0)
    if 'data' in response.json():
        return (response.json().get('data').get('subscribers'))

    else:
        return (0)
