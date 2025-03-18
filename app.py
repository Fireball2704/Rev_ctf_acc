import os
from flask import Flask, render_template, request
import MySQLdb
from dotenv import load_dotenv

# Load environment variables from .env file (if it exists)
load_dotenv()

app = Flask(__name__)

# Get environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")  # Empty password
DB_NAME = os.getenv("DB_NAME", "ctf_db")
DB_PORT = int(os.getenv("DB_PORT", "3306"))  # Default 3306

print("DB_HOST:", DB_HOST)
print("DB_USER:", DB_USER)
print("DB_PASS:", DB_PASS)
print("DB_NAME:", DB_NAME)
print("DB_PORT:", DB_PORT)

# Database connection
try:
    db = MySQLdb.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASS,
        db=DB_NAME,
        port=DB_PORT
    )
    cursor = db.cursor()
    print("✅ Database connected successfully!")
except MySQLdb.Error as e:
    print(f"❌ Database connection failed: {e}")
    exit(1)  # Stop execution if DB connection fails

FLAG = "acc_ctf {h@rd_w0rk_p@ys}"  # Your flag

@app.route("/", methods=["GET", "POST"])
def index():
    users = None
    error = None

    if request.method == "POST":
        user_id = request.form["user_id"]

        # 🚨 SQL Injection Vulnerability for CTF Purposes 🚨
        query = f"SELECT first_name, last_name FROM users WHERE id='{user_id}'"
        print(f"Executing Query: {query}")  # Debugging

        try:
            cursor.execute(query)
            users = cursor.fetchall()

            if users:
                for user in users:
                    if user[0] == "acc_ctf" and user[1] == "{h@rd_w0rk_p@ys}":
                        error = FLAG
                        break
        except MySQLdb.Error as e:
            error = f"SQL Error: {e}"

    return render_template("index.html", users=users, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
