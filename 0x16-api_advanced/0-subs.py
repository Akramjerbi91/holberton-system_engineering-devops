#!/usr/bin/python3
'''Subreddit api'''

def number_of_subscribers(subreddit):
    '''Subreddit info'''
    import requests

    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "zama-zama"},
                            allow_redirects=False)
    if response.status_code != 200:
        return 0
    
    return response.json().get("data").get("subscribers")