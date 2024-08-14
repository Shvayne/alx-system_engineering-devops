#!/usr/bin/python3
"""A function that queries the Reddit API"""
from collections import Counter
import re
import requests

def count_words(subreddit, word_list, hot_list=None, after=None):
    """Recursively queries Reddit API to count the occurrences of keywords in hot article titles."""
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
                return count_and_print(word_list, hot_list)
            for post in posts:
                hot_list.append(post['data']['title'].lower())
            after = data['data'].get('after')
            if after:
                return count_words(subreddit, word_list, hot_list, after)
            else:
                return count_and_print(word_list, hot_list)
        else:
            return None
    except requests.RequestException:
        return None
    

def count_and_print(word_list, hot_list):
    """Counts the occurences of keywords in the hot list and prints it"""
    #compile a regex pattern for keywords to ignore special characters
    word_patterns = {word: re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE) for word in word_list}
    #count occurences of each keyword
    counts = Counter()
    for title in hot_list:
        for word, pattern in word_patterns.items():
            counts[word] += len(pattern.findall(title))
    
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count > 0:
            print(f'{word}: {count}')

            