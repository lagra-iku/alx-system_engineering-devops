#!/usr/bin/python3
"""
script to export data in the JSON format.
"""

import json
import requests
import sys


def get_employee_todo_progress():
    base_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(base_url)
    users = response.json()

    all_response_data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url += '/todos/'
        response = requests.get(url)

        current_users = response.json()
        all_response_data[user_id] = []
        for current_user in current_users:
            status = current_user.get('completed')
            title = current_user.get('title')
            all_response_data[user_id].append({
                "username": username,
                "task": title,
                "completed": status
            })
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_response_data, json_file)


if __name__ == "__main__":
    get_employee_todo_progress()
