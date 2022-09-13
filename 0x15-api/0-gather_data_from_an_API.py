#!/usr/bin/python3
"""Gather_data_from_an_API module"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        id = int(argv[1])
    except Exception as e:
        exit(1)

    baseurl = "https://jsonplaceholder.typicode.com/"
    endpoint = "users/{}".format(id)

    def main_request(baseurl, endpoint):
        """request function"""
        r = requests.get(baseurl + endpoint)
        return r.json()

    user_info = main_request(baseurl, endpoint)
    user_todos = main_request(baseurl, endpoint+'/todos')
    name = user_info['name']

    done_title = []

    for user_todo in user_todos:
        if(user_todo['completed'] is True):
            done_title.append(user_todo['title'])
    number_of_todos = len(user_todos)
    done_number = len(done_title)

    print(done_number)
    print("Employee {} is done with tasks({}/{}):".format(
        name, done_number, number_of_todos))

    for item in done_title:
        print('\t ' + str(item))
