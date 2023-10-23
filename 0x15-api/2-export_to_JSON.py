#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Define the API endpoint
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos'

    # Fetch user data
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print(f"Error: Could not retrieve user data for ID {employee_id}")
        return

    user_data = user_response.json()
    user_id = user_data.get('id')
    user_name = user_data.get('username')

    # Fetch todos data for a specific user using the query parameter
    params = {"userId": employee_id}
    todos_response = requests.get(todos_url, params=params)

    if todos_response.status_code != 200:
        print(f"Error: Could not retrieve data for user ID {employee_id}")
        return

    todos_data = todos_response.json()

    if not todos_data:
        print(f"No TODO list data found for user ID {employee_id}")
        return

    # Prepare the JSON data
    json_data = {user_id: []}

    for todo in todos_data:
        json_data[user_id].append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": user_name
        })

    # Prepare the JSON filename
    json_filename = f'{user_id}.json'

    # Write the JSON data to the file
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
