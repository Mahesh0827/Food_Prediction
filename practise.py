import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["practise_database"]
collection=db["swathi"]

for i in range(5):
    name=input("Enter the name: ")
    age = int(input("Age: "))
    roll = input("Roll Number: ")
    phone = input("Phone Number: ")
    address = input("Address: ")
    collection.insert_one({
        "name":name,
        "age":age,
        "roll":roll,
        "phone":phone,
        "address":address
    })

