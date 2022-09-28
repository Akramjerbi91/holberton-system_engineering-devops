#!/usr/bin/python3
'''Subreddit api top ten'''


def top_ten(subreddit):
    '''Subreddit to ten info'''
    import requests

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            headers={"User-Agent": "zamacode-zama"},
                            params={"limit": "10"},
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)

    for item in response.json().get("data").get("children"):
        print(item.get("data").get("title"))
