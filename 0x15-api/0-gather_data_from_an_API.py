#!/usr/bin/python3
"""A python script that returns info about an emplyee TODO list progress"""
import requests
from sys import argv

if __name__ == "__main__":
    emp_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    emp_url = url + '/' + emp_id
    todo_url = emp_url + '/todos'

    emp_res = requests.get(emp_url)
    emp_name = emp_res.json().get("name")

    tasks = requests.get(todo_url)
    tasks_res = tasks.json()

    done_tasks = []
    done = 0

    for task in tasks_res:
        if task.get("completed"):
            done += 1
            done_tasks.append(task)
    print("Employee {} is done with tasks ({}/{})".format(emp_name, done, len(tasks_res)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
