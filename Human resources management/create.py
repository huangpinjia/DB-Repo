from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import noSQL  # 引入noSQL模組

app = Flask(__name__)

# MongoDB 設定
client = MongoClient("mongodb://localhost:27017/")
db = client["local"]
employees_collection = db["employees"]

@app.route('/')
def index():
    employees = noSQL.get_employees()
    return render_template("index.html", employees=employees)

@app.route('/create', methods=['GET', 'POST'])
def create_employee():
    if request.method == 'POST':
        name = request.form.get("name")
        position = request.form.get("position")
        age = request.form.get("age")
        department = request.form.get("department")
        noSQL.create_employee(name, position, age, department)
        return redirect(url_for('index'))
    return render_template("create.html")

if __name__ == '__main__':
    app.run(debug=True)
