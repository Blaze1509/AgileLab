from flask import Flask, request

app = Flask(__name__)

# Valid login for the demo
USERNAME = "student"
PASSWORD = "1234"


def calculate_attendance(attended, total):
    """Return attendance percentage rounded to 2 decimals."""
    if attended < 0 or total < 0:
        raise ValueError("Values cannot be negative")
    if attended > total:
        raise ValueError("Attended cannot be more than total")
    if total == 0:
        return 0
    return round(attended / total * 100, 2)


def attendance_report(name, attended, total):
    """Return a one-line attendance report for a student."""
    percent = calculate_attendance(attended, total)
    status = "OK" if percent >= 75 else "LOW"
    return f"{name}: {percent}% ({status})"


LOGIN_PAGE = """
<html>
<head><title>Student Login</title></head>
<body>
  <h2>Student Login</h2>
  <form method="post" action="/login">
    <input type="text" id="username" name="username" placeholder="Username">
    <input type="password" id="password" name="password" placeholder="Password">
    <button type="submit" id="login-btn">Login</button>
  </form>
  <p id="message">{message}</p>
</body>
</html>
"""


@app.route("/")
def home():
    return LOGIN_PAGE.format(message="")


@app.route("/login", methods=["POST"])
def login():
    if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
        return "<h2 id='welcome'>Welcome, student! Login successful</h2>"
    return LOGIN_PAGE.format(message="Invalid username or password")


if __name__ == "__main__":
    print(attendance_report("Ravi", 8, 10))
    app.run(host="0.0.0.0", port=5000)
