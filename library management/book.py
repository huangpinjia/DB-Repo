from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# 資料庫配置
# 設定資料庫連接
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'library'
}

# 建立資料庫連接
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# 查詢所有書籍
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Book")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('book.html', books=books)

# 新增書籍
@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Book (Title, Author) VALUES (%s, %s)", (title, author))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# 刪除書籍
@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Book WHERE BookID = %s", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# 更新書籍資料
@app.route('/update/<int:book_id>', methods=['POST'])
def update_book(book_id):
    title = request.form['title']
    author = request.form['author']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Book SET Title = %s, Author = %s WHERE BookID = %s", (title, author, book_id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # 使用 5001 埠

