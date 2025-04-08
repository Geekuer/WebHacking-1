from flask import Flask, request
import sqlite3

app = Flask(__name__)

# 간단한 DB 초기화
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    c.execute("DELETE FROM users")  # 중복 방지
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'supersecret')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return '''
    <form action="/login" method="POST">
        Username: <input name="username"><br>
        Password: <input name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/login', methods=['POST'])  # ← POST로 받기
def login():
    username = request.form.get('username')  # ← form 데이터 읽기
    password = request.form.get('password')

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # SQL Injection 가능 (일부러 취약하게 둠)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("[DEBUG] SQL:", query)

    try:
        c.execute(query)
        result = c.fetchone()
    except Exception as e:
        return f"SQL Error: {e}"

    if result:
        real_username = result[1]
        return f"Welcome {real_username}!"
    else:
        return "Login failed!"

if __name__ == '__main__':
    init_db()
    app.run()