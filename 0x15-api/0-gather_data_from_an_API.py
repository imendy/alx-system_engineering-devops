#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
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
    user_name = user_data.get('name')

    if user_name is None:
        print(f"Error: User name not found for ID {employee_id}")
        return

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

    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo.get('completed'))

    print(f"Employee {user_name} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")

    for todo in todos_data:
        if todo.get('completed'):
            print(f"	 {todo.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
