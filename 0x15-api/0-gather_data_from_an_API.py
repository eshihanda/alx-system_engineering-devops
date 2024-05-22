#!/usr/bin/python3
"""
This script takes an employee ID as a command-line argument And fetches.
Returns to-do list information for a given employee ID
"""

import requests
import sys


if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the employee information using the provided employee ID
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Get the to-do list for the employee using the provided employeeID.
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # Filter completed tasks and count it.
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print the employee's name and the number of completed task.
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the completed tasks one by one.
    [print("\t {}".format(complete)) for complete in completed]
