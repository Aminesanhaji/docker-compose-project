from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Connexion à la base de données PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),  # Nom du service PostgreSQL dans Docker
        database=os.getenv("DB_NAME", "mydatabase"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASSWORD", "password")
    )
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Bienvenue sur mon API Flask avec PostgreSQL !"})

@app.route('/data')
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM test_table;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
