from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    username = data.get("username")  
    password = data.get("password")

    if not name or not username or not password:
        return jsonify({"error": "Nome, email e senha são obrigatórios"}), 400

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (name, username, password) VALUES (?, ?, ?)", 
                       (name, username, password))
        conn.commit()
        return jsonify({"message": f"Usuário {name} registrado com sucesso!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Usuário já existe"}), 400
    finally:
        conn.close()

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"message": f"Login realizado com sucesso, {user[1]}!"}), 200
    else:
        return jsonify({"error": "Email ou senha incorretos"}), 401

if __name__ == "__main__":
    app.run(debug=True)
