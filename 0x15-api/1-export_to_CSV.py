#!/usr/bin/python3
"""Script to export data in the CSV format"""
import csv
import requests as req
import sys

if __name__ == "__main__":
    the_user_id = sys.argv[1]
    the_url = "https://jsonplaceholder.typicode.com/"
    the_usr = req.get(the_url + "users/{}".format(the_user_id)).json()
    the_username = the_usr.get("username")
    the_todo = req.get(the_url + "todos", params={"userId": the_user_id}).json()

    with open("{}.csv".format(the_user_id), "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [csv_writer.writerow([the_user_id, the_username, the_tasks.get("completed"),
                          the_tasks.get("title")]) for the_tasks in the_todo]
