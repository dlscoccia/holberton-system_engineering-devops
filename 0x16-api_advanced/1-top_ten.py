#!/usr/bin/python3
'''python module'''
import requests


def top_ten(subreddit):
    '''queries the Reddit API'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    my_header = {'User-Agent': 'my-integration/1.2.3'}
    r = requests.get(url, headers=my_header, allow_redirects=False)
    if (r.status_code != 200):
        print(None)
        return
    r = r.json()
    r_data = r.get('data', None)
    if (r_data):
        for i in range(10):
            hot_title = r_data['children'][i]['data']['title']
            print(hot_title)
