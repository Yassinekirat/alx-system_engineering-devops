#!/usr/bin/python3
"""
script that uses a REST API to returns information
about his/her TODO list progress
"""
import json
import requests
import sys
import urllib
import urllib.request

if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    completed_tasks_count = 0
    completed_tasks = []

    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            completed_tasks_count += 1

    total_tasks_count = len(tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_tasks_count, total_tasks_count))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
