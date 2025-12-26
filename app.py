from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

# Temporary user storage
users = {}

@app.route("/", methods=["GET", "POST"])
def bmi():
    if "user" not in session:
        return redirect(url_for("login"))

    bmi_value = None
    category = None

    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        bmi_value = round(weight / ((height / 100) ** 2), 2)

        if bmi_value < 18.5:
            category = "Underweight"
        elif bmi_value < 24.9:
            category = "Normal weight"
        elif bmi_value < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

    return render_template("index.html", bmi=bmi_value, category=category)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("bmi"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            error = "User already exists"
        else:
            users[username] = password
            return redirect(url_for("login"))

    return render_template("register.html", error=error)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
