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
    
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        for task in todos_data:
            completed = task.get('completed')
            title_task = task.get('title')
            csv_file.write('"{}","{}","{}","{}"\n'.format(
            employee_id, user_data['username'], completed, title_task))
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
