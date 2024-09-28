from flask import Flask, render_template, request, redirect
import mysql.connector
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="294784r3e2w1q",
    database="user_data"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    platform = request.form['platform']
    
    # Hash the password for security
    hashed_password = generate_password_hash(password)
    
    cursor = db.cursor()
    sql = "INSERT INTO users (email, username, password, platform) VALUES (%s, %s, %s, %s)"
    val = (email, username, hashed_password, platform)
    cursor.execute(sql, val)
    db.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
