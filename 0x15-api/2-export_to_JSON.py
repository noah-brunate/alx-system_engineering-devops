#!/usr/bin/python3
"""Python script to export data in the CSV format"""

import request
import sys
import json


if __name__ == '__main__':
    empId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    empUlr = url + '/' + empId

    response = request.get(empUrl)
    empName = response.json().get('username')

    todoUrl = url + '/todos'
    resp = request.get(todoUrl)
    tasks = resp.json()

    dictionary = {empId: []}
    for task in tasks:
        dictionary[empId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": empName})

    with open('{}.json'.format(empId), 'w') as file:
        json.dump(dictionary, file)
