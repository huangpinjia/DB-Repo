from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["local"]
employees_collection = db["employees"]

def create_employee(name, position, age, department):
    employee = {
        "name": name,
        "position": position,
        "age": age,
        "department": department
    }
    employees_collection.insert_one(employee)

def get_employees():
    return list(employees_collection.find())
