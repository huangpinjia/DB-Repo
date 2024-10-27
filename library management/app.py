from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# 設定資料庫連接
db_config = {
    'user': 'root',
    'password': '294784r3e2w1q',
    'host': 'localhost',
    'database': 'library'
}

# 建立資料庫連接
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# 查詢所有讀者
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Reader")
    readers = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', readers=readers)

# 新增讀者
@app.route('/add', methods=['POST'])
def add_reader():
    name = request.form['name']
    email = request.form['email']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Reader (Name, Email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# 刪除讀者
@app.route('/delete/<int:reader_id>')
def delete_reader(reader_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Reader WHERE ReaderID = %s", (reader_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# 更新讀者資料
@app.route('/update/<int:reader_id>', methods=['POST'])
def update_reader(reader_id):
    name = request.form['name']
    email = request.form['email']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Reader SET Name = %s, Email = %s WHERE ReaderID = %s", (name, email, reader_id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(port=5000, debug=True)  # 使用 5000 埠

