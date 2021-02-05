#!/usr/bin/python3
'''python module'''
import requests


def number_of_subscribers(subreddit):
    '''python module'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    my_header = {'User-Agent': 'my-integration/1.2.3'}
    r = requests.get(url, headers=my_header).json()
    nb_subscribers = r.get('data', {}).get('subscribers', 0)
    return nb_subscribers
