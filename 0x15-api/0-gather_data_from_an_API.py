#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests as req
import sys

if __name__ == '__main__':
    the_url = 'https://jsonplaceholder.typicode.com/'
    the_usr_id = req.get(the_url + 'users/{}'.format(sys.argv[1])).json()
    the_todo = req.get(the_url + 'todos', params={'userId': sys.argv[1]}).json()
#    print(the_todo)
    completed = [title.get("title") for title in the_todo if
                 title.get('completed') is True]
    print(completed)
    print("Employee {} is done with tasks({}/{}):".format(the_usr_id.get("name"),
                                                          len(completed),
                                                          len(the_todo)))
    [print("\t {}".format(title)) for title in completed]
