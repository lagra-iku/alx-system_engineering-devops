#!/usr/bin/python3
"""
a script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = sum(task['completed'] for task in todos_data)

    print(f"Employee {user_data['name']} is done \
with tasks ({completed_tasks}/{total_tasks}):")
    print(f"{user_data['name']}:", end=' ')
    print(f"name of the employee")

    for task in todos_data:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
