#!/usr/bin/python3
"""
Gather data from API: Return all tasks given employee ID
export this data in the CSV format
"""

import csv
import requests
from sys import argv


def export_to_csv():
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

    """Export  to csv"""
    filename = '{}.csv'.format(argv[1])
    with open(filename, 'w') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLET_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLET_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    export_to_csv()
