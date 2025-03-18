from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

# Database connection
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="ctf_db")
cursor = db.cursor()

FLAG = "acc_ctf {h@rd_w0rk_p@ys}"  # Your flag

@app.route("/", methods=["GET", "POST"])
def index():
    users = None
    error = None

    if request.method == "POST":
        user_id = request.form["user_id"]

        # 🚨 VULNERABLE SQL QUERY 🚨
        query = f"SELECT first_name, last_name FROM users WHERE id='{user_id}'"
        print(f"Executing Query: {query}")  # Debugging

        try:
            cursor.execute(query)
            users = cursor.fetchall()

            # Check if the query returned more than one row (indicating SQL injection)
            if len(users) > 1:  # Normal input should return 0 or 1 row
                # Display the flag if the payload is detected
                for user in users:
                    if user[0] == "acc_ctf" and user[1] == "{h@rd_w0rk_p@ys}":
                        error = FLAG
                        break
        except MySQLdb.Error as e:  # Catch all MySQL errors
            error = f"SQL Error: {e}"

    return render_template("index.html", users=users, error=error)

# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
