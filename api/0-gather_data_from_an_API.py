#!/usr/bin/python3
"""Retrieving data using apis"""

import requests 
import sys

user_id = sys.argv[1]
url1= "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
resp1 = requests.get(url1, verify= False).json()
name = resp1.get("name")
url2= "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
resp2 = requests.get(url2, verify= False).json()
count = 0
for todo in resp2:
	if todo["completed"]:
		count += 1
		total_tasks = len(resp2)
print("Employee {} is done with tasks({}/{}):".format(name, count, total_tasks))
for todo in resp2:
	if todo["completed"]:
		title = resp2[int(user_id)-1].get("title")
		print("	{}".format(title))
