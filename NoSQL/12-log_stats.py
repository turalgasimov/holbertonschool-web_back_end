#!/usr/bin/env python3
'''Module 12-log_stats'''
from pymongo import MongoClient

def log_stats(mongo_collection):
    '''Provides some stats about Nginx logs'''
    if mongo_collection is None:
        print(
            "0 logs\nMethods:\n\tmethod GET: 0\n\tmethod POST: 0\n\tmethod PUT: 0\n\tmethod PATCH: 0\n\tmethod DELETE: 0\n0 status check"
        )

    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
