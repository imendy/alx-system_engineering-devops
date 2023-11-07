#!/usr/bin/python3
""" Function that queries Reddit API and prints titles of 1st 10 hot post."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {'User-Agent': 'RedditDataAnalyzer/1.0 (ALX Africa)'}
    params = {'limit': 10}  # Limit the number of posts to 10

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for post in data.get('data').get('children'):
            title = post.get('data').get('title')
            print(title)
    else:
        print(None)
