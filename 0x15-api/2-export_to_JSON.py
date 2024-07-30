#!/usr/bin/python3
"""A python script that returns info about an emplyee TODO list progress"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    emp_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    emp_url = url + '/' + emp_id
    todo_url = emp_url + '/todos'

    emp_res = requests.get(emp_url)
    emp_username = emp_res.json().get("username")

    tasks = requests.get(todo_url)
    tasks_res = tasks.json()

    file_name = emp_id + ".json"

    emp_dict = {emp_id: []}
    for task in tasks_res:
        emp_dict[emp_id].append({"task": task.get("title"), "completed": task.get("completed"), "username": emp_username})

    with open(file_name, "w") as f:
        json.dump(emp_dict, f)

