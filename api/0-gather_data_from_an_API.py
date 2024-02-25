#!/usr/bin/python3
"""Retrieving data using apis"""

import requests as req
import sys

user_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
resp = req.get(url).json()
print(resp)

