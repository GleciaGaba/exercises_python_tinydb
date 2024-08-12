from tinydb import TinyDB, Query, where

db = TinyDB('data.json', indent=4)
"""
db.update({"score": 300}, where('name') == "Patrick")

db.update({"roles": ["Junior"]})
db.update({"roles": ["Pythonista"]}, where("name") == "Patrick")"""
db.upsert({"name": "Pierre", "score": 10, "roles": ["Senior"]}, where('name') == 'Pierre')