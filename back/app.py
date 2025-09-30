from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute( """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY
        AUTOINCREMENT,
            username TEXT UNIQUE
            password TEXT
        )
    """)
    conn.commit()
    conn.close()
    
init_db()

@app.route("/register", methods=["POST"])

def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return jsonify({"error": "Usuário já existe"}), 400
    finally:
        conn.close()

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data("username")
    password = data("password")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))

    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify ({"message": "Login realizado com sucesso, pequeno crioulo!"})
    else:
        return jsonify({"error": "Username ou senha incorretas"})