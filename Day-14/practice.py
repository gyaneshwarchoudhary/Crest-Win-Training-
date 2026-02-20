# import MongoClient class from pymongo library
from pymongo import MongoClient

# create connection to MongoDB server running on localhost and port 27017
client = MongoClient("mongodb://localhost:27017/")

# access database named "mydatabase"
db = client["mydatabase"]

# access collection named "users"
collection = db["users"]


# CREATE (Insert a document)
user = {"name": "Rahul", "age": 22, "email": "rahul@example.com"}

result = collection.insert_one(user)

print("Inserted ID:", result.inserted_id)


# READ (Find all documents)
print("\nAll users:")
for u in collection.find():
    print(u)


# UPDATE (Update one document)
collection.update_one({"name": "Rahul"}, {"$set": {"age": 23}})  # filter  # new value

print("\nAfter update:")
for u in collection.find():
    print(u)


# DELETE (Delete one document)
collection.delete_one({"name": "Rahul"})

print("\nAfter delete:")
for u in collection.find():
    print(u)


# ------------------------- with odm -------------------------

# import mongoengine library
from mongoengine import connect, Document, StringField, IntField, EmailField


# connect to database
connect("mydatabase", host="mongodb://localhost:27017/")


# define a model (like a class)
class User(Document):

    name = StringField(required=True)

    age = IntField(required=True)

    email = EmailField(required=True)


# CREATE
user = User(name="Rahul", age=22, email="rahul@example.com")

user.save()

print("Inserted ID:", user.id)


# READ
print("\nAll users:")
for u in User.objects:
    print(u.name, u.age, u.email)


# UPDATE
user = User.objects(name="Rahul").first()

user.age = 23

user.save()

print("\nAfter update:")
for u in User.objects:
    print(u.name, u.age, u.email)


# DELETE
user = User.objects(name="Rahul").first()

user.delete()

print("\nAfter delete:")
for u in User.objects:
    print(u.name, u.age, u.email)
