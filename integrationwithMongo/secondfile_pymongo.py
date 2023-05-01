import collections
import pprint
from http import client

import pymongo
import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://codejacque:password@cluster0.xxtfhku.mongodb.net/?retryWrites=true&w=majority")
db = client.test
posts = db.posts

for post in posts.find():
    pprint.pprint(post)

print(posts.count_doments({}))
print(posts.count_documents({"author": "Mike"}))
print(posts.count_documents({"tags": "insert"}))

pprint.pprint(posts.find_one({"tags": "insert"}))

print("\n Retrieving info from the post collection in an orderly manner")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

result = db.profiles.create_index([('auto', pymongo.ASCENDING)], unique=True)

print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {'customer_id': 215, 'name': 'Luke'},
    {'customer_id': 216, 'name': 'Joao'}]

result = db.profile.insert_many(customer_profile_customer)

print("\nStorage collection in mongoDB")
print(db.list_collection_names())

for collection in collections:
    print(collection)

for post in posts.finf():
    pprint.pprint(post)

print(posts.delete_one({"author": "Mike"}))
