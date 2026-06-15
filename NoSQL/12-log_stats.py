#!/usr/bin/env python3
'''Module 12-log_stats'''
from pymongo import MongoClient


def log_stats():
    '''Provides some stats about Nginx logs'''

    db = MongoClient("mongodb://127.0.0.1:27017").logs
    mongo_collection = db.nginx


    if mongo_collection.count_documents() == 0:
        print(
            '''0 logs\n
            Methods:\n
            \tmethod GET: 0\n
            \tmethod POST: 0\n
            \tmethod PUT: 0\n
            \tmethod PATCH: 0\n
            \tmethod DELETE: 0\n
            0 status check'''
        )

    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")
