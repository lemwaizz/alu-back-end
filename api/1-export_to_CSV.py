#!/usr/bin/python3
"""
   python script that exports  data in csv
"""
if __name__ == "__main__":
    """
       requests in csv
    """
    import csv
    import json
    import requests
    import sys
    user_id = sys.argv[1]
    url_raw = "https://jsonplaceholder.typicode.com/users/{}/todos"
    url1 = url_raw.format(user_id)
    resp1 = requests.get(url1, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/{}"
    url2 = url.format(user_id)
    resp2 = requests.get(url2, verify=False).json()
    filename = f"{sys.argv[1]}.csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=",", quotechar='"',
                                quoting=csv.QUOTE_ALL)
    for data in resp1:
        csv_writer.writerow([data["userId"], resp2.get("username"),
                            data["completed"], data["title"]])
