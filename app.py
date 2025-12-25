from flask import Flask , render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi():
    bmi_value = None
    category = None

    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        bmi_value = round(weight / ((height / 100)**2), 2)

        if bmi_value < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi_value < 24.9:
            category = "Normal weight"
        elif 25 <= bmi_value < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

    return render_template("index.html", bmi=bmi_value, category=category)


if __name__ == "__main__":
    app.run(debug=True)
