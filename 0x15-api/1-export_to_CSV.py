#!/usr/bin/python3
"""Python script to export data in the CSV format"""

import request
import sys


if __name__ == '__main__':
    empId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    empUlr = url + '/' + empId

    response = request.get(empUrl)
    empName = response.json().get('username')

    todoUrl = url + '/todos'
    resp = request.get(todoUrl)
    tasks = resp.json()

    with open('{}.csv'.format(empId), 'w') as file:
        for task in tasks:
            file.write('{},{},{},{}\n'
                       .format(empId, username, resp.get('completed'),
                               resp.get('title')))
