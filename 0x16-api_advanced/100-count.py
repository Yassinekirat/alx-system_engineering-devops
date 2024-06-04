#!/usr/bin/python3
""" Count it!"""
import requests


def count_words(subreddit, word_list, key_words={}, count={}, after=None):
    """ Count it!"""

    if not count:
        key_words = {word.lower(): 0 for word in word_list}
        word_list = [word.lower() for word in word_list]
        count = {word: word_list.count(word) for word in word_list}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json().get('data', {})
        after = data.get('after')
        posts = data.get('children', [])

        for post in posts:
            title = post.get('data', {}).get('title', "").lower()
            words = title.split()
            for word in key_words.keys():
                key_words[word] += words.count(word)

        if after:
            return count_words(subreddit,
                               word_list, key_words, count, after)
        else:
            for key in key_words.keys():
                key_words[key] *= count[key]

            sorted_key_words = sorted(key_words.items(),
                                      key=lambda item: (-item[1], item[0]))

            for word, freq in sorted_key_words:
                if freq > 0:
                    print(f"{word}: {freq}")

    except ValueError:
        return None
