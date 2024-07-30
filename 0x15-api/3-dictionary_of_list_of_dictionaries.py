#!/usr/bin/python3
"""A script to return info about an employee to and export to Json"""
import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + 'users'
    todo_url = url + 'todos'

    users = requests.get(user_url).json()

    filename = 'todo_all_employees.json'
    with open(filename, "w") as f:
        json.dump({user.get("id"): [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": task.get("username")
            } for task in requests.get(
                todo_url, params={"userId": user.get("id")}
                ).json()] for user in users}, f)
