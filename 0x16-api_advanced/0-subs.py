#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code == 200 and 'subscribers' in response.json()['data']:
        subscribers_count = response.json()['data']['subscribers']
        return subscribers_count
    else:
        return 0


if __name__ == "__main__":
    subreddit_name = int(sys.argv[1])
    number_of_subscribers(subreddit_name)
