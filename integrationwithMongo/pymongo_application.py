import datetime
import pprint
from http import client

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://codejacque:password@cluster0.xxtfhku.mongodb.net/?retryWrites=true&w=majority")


db = client.test
collection = db.test_collection
print(db.test_collection)

#
post = {
    "author": "Mike",
    "text": "My firts mongdb application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}


posts = db.posts
post_id = post.insert_one(post).inserted_id
print(post_id)


print.pprint(db.posts.find_one())


new_posts = [{
       "author": "Mike",
       "text": "Another post",
       "tags": ["bulk", "post", "insert"],
       "date": datetime.datetime.utcnow()},
    {
       "author": "Joao",
       "text":  "Post from Joao. New post available",
       "title": "Mongo is fun",
       "date": datetime.datetime(2023, 11, 10, 10, 45)}]

result = post.insert_many(new_posts)
print(result.insert_ids)

print("\n Final Recovery")
pprint.pprint(db.posts.find_one({"author": "Joao"}))

print("\n Documents present in the posts collection")
for post in posts.find():
    pprint.pprint(post)
