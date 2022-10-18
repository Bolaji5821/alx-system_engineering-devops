#!/usr/bin/python3
"""A Python script that uses REST API to get some employee's ID
    and returns their TODO list progress"""

import sys
import requests

if __name__ == "__main__":

    user_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id))
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = 0
    name = user.json().get('name')
    completed = 0
    for task in todo.json():
        if task.get('userId') == int(user_id):
            tasks += 1
            if task.get('completed'):
                completed += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, tasks))
    print('\n'.join(["\t " + task.get('title') for task in todo.json()
          if task.get('userId') == int(user_id) and task.get('completed')]))
