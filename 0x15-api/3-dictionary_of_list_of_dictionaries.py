#!/usr/bin/python3
"""
Gather data from API: Return all tasks all employees
export this data to JSON format
"""

import json
import requests


def all_to_json():
    """return API data"""
    USERS = []
    userss = requests.get('https://jsonplaceholder.typicode.com/users')
    for u in userss.json():
        USERS.append((u.get('id'), u.get('username')))

    TASK_STATUS_TITLE = []

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for t in todos.json():
        TASK_STATUS_TITLE.append((t.get('userId'), t.get('completed'),
                                  t.get('title')))

    """Export  to json"""

    # Create the value of the dict of the final json file
    data = dict()
    for u in USERS:
        t = []
        for task in TASK_STATUS_TITLE:
            if task[0] == u[0]:
                t.append({"username": u[1], "task": task[2],
                          "completed": task[1]})
        data[u[0]] = t
    filename = 'todo_all_employees.json'

    # Generate json file
    with open(filename, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    all_to_json()
