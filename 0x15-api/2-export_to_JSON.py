#!/usr/bin/python3
"""
Gather data from API: Return all tasks given employee ID
export this data to JSON format
"""

import json
import requests
from sys import argv


def export_to_json():
    """return API data"""
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    for u in users.json():
        if u.get('id') == int(argv[1]):
            USERNAME = u.get('username')

    TASK_STATUS_TITLE = []

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    """Export  to json"""

    # Create the value of the dict of the final json file
    jslist = []
    for t in TASK_STATUS_TITLE:
        jslist.append({"task": t[1], "completed": t[0], "username": USERNAME})
    data = {argv[1]: jslist}
    filename = '{}.json'.format(argv[1])

    # Generate json file
    with open(filename, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    export_to_json()
