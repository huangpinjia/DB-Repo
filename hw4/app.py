from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Database setup
client = MongoClient("mongodb://localhost:27017/")
db = client["local"]
employees_collection = db["employees"]

# Create
@app.route('/create', methods=['POST'])
def create_employee():
    data = request.form
    employee = {
        "name": data["name"],
        "position": data["position"],
        "age": int(data["age"]),
        "department": data["department"]
    }
    employees_collection.insert_one(employee)
    return redirect(url_for('home'))

# Read
@app.route('/')
def home():
    employees = list(employees_collection.find())
    return render_template('index.html', employees=employees)

# Update
@app.route('/update/<employee_id>', methods=['POST'])
def update_employee(employee_id):
    data = request.form
    updated_employee = {
        "name": data["name"],
        "position": data["position"],
        "age": int(data["age"]),
        "department": data["department"]
    }
    employees_collection.update_one({"_id": ObjectId(employee_id)}, {"$set": updated_employee})
    return redirect(url_for('home'))

# Delete
@app.route('/delete/<employee_id>', methods=['POST'])
def delete_employee(employee_id):
    employees_collection.delete_one({"_id": ObjectId(employee_id)})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
