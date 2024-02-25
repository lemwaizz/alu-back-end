#!/usr/bin/python3
"""
    python script that returns TODO list progress for a given employee ID
"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    """
       passing id as the second argument.
    """
    user_id = sys.argv[1]
    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    """
       retrieve the data as json using requests method.
    """
    resp1 = requests.get(url1, verify=False).json()
    """
       get the value of the name key
    """
    name = resp1.get("name")
    url_raw = "https://jsonplaceholder.typicode.com/users/{}/todos"
    url2 = url_raw.format(user_id)
    """
       convert to json.
    """
    resp2 = requests.get(url2, verify=False).json()
    """
       initialize count for completed tasks.
    """
    count = 0
    """
       loop through the resp2 json while increasing count of completed tasks.
    """
    for todo in resp2:
        if todo["completed"]:
            count += 1
            total = len(resp2)
    """
       print all outputs
    """
    print("Employee {} is done with tasks({}/{}):".format(name, count, total))
    """
       loop through resp2 again finding the title and print it
    """
    for todo in resp2:
        if todo["completed"]:
            title = resp2[int(user_id)-1].get("title")
            print("	 {}".format(title))
