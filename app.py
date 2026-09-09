import os
import psycopg2
from flask import Flask

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
 
def get_db_connection():
return psycopg2.connect(
host=DB_HOST,
database=DB_NAME,
user=DB_USER,
password=DB_PASSWORD
)

@app.route("/")
def home():
    return {"application": "Book Inventory API"}

@app.route("/books")
def books():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, title FROM books")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {
            "id": row[0],
            "title": row[1]
        }
        for row in rows
    ]

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
