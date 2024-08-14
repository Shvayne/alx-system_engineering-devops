#!/usr/bin/python3
"""A function that queries the Reddit API"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    """Recursively query the reddit api to return hot articles"""
    if hot_list is None:
        hot_list = []
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100} 
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data'].get('children', [])

            if not posts:
                return hot_list if hot_list else None
            for post in posts:
                hot_list.append(post['data']['title'])
            #next page
            after = data['data'].get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None