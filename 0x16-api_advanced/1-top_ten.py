#!/usr/bin/python3
"""A function that queries the Reddit API and prints the titles of the first 10 hot posts for a given sub reddit"""
import requests

def top_ten(subreddit):
    """prints the titles of the first 10 hot posts for a sub reddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data'].get('children', [])
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)