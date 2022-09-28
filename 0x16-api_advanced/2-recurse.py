#!/usr/bin/python3
'''Subreddit api top ten'''


def recurse(subreddit, hot_list=[], after=""):
    '''Subreddit to ten info'''
    import requests

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            headers={"User-Agent": "zamacode-zama"},
                            params={"after": after},
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    for item in response.json().get("data").get("children"):
        hot_list.append(item.get("data").get("title"))
    after = response.json().get("data").get("after")
    if after is not None:
        recurse(subreddit, hot_list, after=after)
    return(hot_list)
