#!/usr/bin/python3
"""
script exports data in json for all employees
"""

import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    resp = requests.get(url)
    emps = resp.json()

    empId = []
    for n in emps:
        empId.append(n.get('id'))

    tod_list = {}
    for m in empId:
        newUrl = f"{url}/{m}/todos"
        res = requests.get(newUrl)
        tasks = res.json()
        empUrl = f"{url}/{m}"
        username = requests.get(empUrl).json().get('username')
        tod_list[m] = []
        for task in tasks:
            tod_list[m].append({"username": username,
                                "task": task.get('title'),
                                "completed": task.get('completed')})

    with open('todo_all_employees.json', 'w') as file:
        json.dump(tod_list, file)
