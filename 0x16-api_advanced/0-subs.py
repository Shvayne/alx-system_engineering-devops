#!/usr/bin/python3
"""A function that queries the Reddit API and return the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of total subscribers for a sub reddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0

    

