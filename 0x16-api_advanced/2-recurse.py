#!/usr/bin/python3
"""
Recursive function that queries Reddit API returns a list containing the
titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {'User-Agent': 'RedditDataAnalyzer/1.0 (ALX Africa)'}
    params = {'limit': 100}  # Limit the number of posts to 100 (maximum)

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for post in data.get('data', {}).get('children', []):
            title = post.get('data', {}).get('title', '')
            hot_list.append(title)

        # Check if there are more pages (pagination) and continue the recursion
        after = data.get('data', {}).get('after')
        if after:
            return recurse(subreddit, hot_list, after)

        # If no more pages, return the hot_list
        return hot_list
    else:
        return None
