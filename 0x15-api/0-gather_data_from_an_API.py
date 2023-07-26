#!/usr/bin/python3
"""
 script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
import sys

if __name__ == '__main__':
    empId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    empUrl = url + '/' + empId

    response = requests.get(empUrl)
    empName = response.json().get('name')

    todoUrl = url + "/todos"
    res = requests.get(todoUrl)
    tasks = res.json()

    done = 0
    done_tasks = []
    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(empName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
