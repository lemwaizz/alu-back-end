#!/usr/bin/python3
"""
Retrieving data using apis
"""
"""
importing the right modules
"""
import requests 
import sys
import json


"""
passing id as the second argument.
"""
user_id = sys.argv[1]
url1= "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

"""
retrieve the data as json using requests method.
"""
resp1 = requests.get(url1, verify= False).json()

"""
get the value of the name key
"""
name = resp1.get("name")
url2= "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
resp2 = requests.get(url2, verify= False).json()

"""
initialize count for completed tasks.
"""
count = 0
"""
loop through the resp2 json
"""
for todo in resp2:
	if todo["completed"]:
		count += 1
		total_tasks = len(resp2)
"""
print all outputs
"""
print("Employee {} is done with tasks({}/{}):".format(name, count, total_tasks))
"""
loop through resp2 again finding the title and print it
"""
for todo in resp2:
	if todo["completed"]:
		title = resp2[int(user_id)-1].get("title")
		print("	{}".format(title))
