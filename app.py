from flask import Flask, render_template, request
import MySQLdb
import os

app = Flask(__name__)

# Use Railway-provided MySQL credentials
db = MySQLdb.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASS"),
    db=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT", 3306))  # Default MySQL port
)
cursor = db.cursor()

FLAG = "acc_ctf {h@rd_w0rk_p@ys}"

@app.route("/", methods=["GET", "POST"])
def index():
    users = None
    error = None

    if request.method == "POST":
        user_id = request.form["user_id"]
        query = f"SELECT first_name, last_name FROM users WHERE id='{user_id}'"
        print(f"Executing Query: {query}")

        try:
            cursor.execute(query)
            users = cursor.fetchall()
            if len(users) > 1:
                for user in users:
                    if user[0] == "acc_ctf" and user[1] == "{h@rd_w0rk_p@ys}":
                        error = FLAG
                        break
        except MySQLdb.Error as e:
            error = f"SQL Error: {e}"

    return render_template("index.html", users=users, error=error)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
