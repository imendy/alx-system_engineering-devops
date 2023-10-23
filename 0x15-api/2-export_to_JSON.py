#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    the_user_id = sys.argv[1]
    the_url = "https://jsonplaceholder.typicode.com/"
    the_user = requests.get(the_url + "users/{}".format(the_user_id)).json()
    the_username = the_user.get("username")
    my_todos = requests.get(the_url + "todos", params={"userId": the_user_id}).json()

    with open("{}.json".format(the_user_id), "w") as jsonfile:
        json.dump({the_user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": the_username
            } for t in my_todos]}, jsonfile)
