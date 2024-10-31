from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# 資料庫配置

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

# 查詢所有借閱記錄
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT Loan.LoanID, Reader.Name AS ReaderName, Book.Title AS BookTitle, 
               Loan.LoanDate, Loan.ReturnDate, Loan.created_at
        FROM Loan
        JOIN Reader ON Loan.ReaderID = Reader.ReaderID
        JOIN Book ON Loan.BookID = Book.BookID
    """
    cursor.execute(query)
    loans = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('loan.html', loans=loans)

# 新增借閱記錄
@app.route('/add', methods=['POST'])
def add_loan():
    reader_id = request.form['reader_id']
    book_id = request.form['book_id']
    loan_date = request.form['loan_date']
    return_date = request.form['return_date']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Loan (ReaderID, BookID, LoanDate, ReturnDate) VALUES (%s, %s, %s, %s)",
        (reader_id, book_id, loan_date, return_date)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# 刪除借閱記錄
@app.route('/delete/<int:loan_id>')
def delete_loan(loan_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Loan WHERE LoanID = %s", (loan_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# 更新借閱記錄
@app.route('/update/<int:loan_id>', methods=['POST'])
def update_loan(loan_id):
    loan_date = request.form['loan_date']
    return_date = request.form['return_date']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Loan SET LoanDate = %s, ReturnDate = %s WHERE LoanID = %s",
        (loan_date, return_date, loan_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5002, debug=True)
