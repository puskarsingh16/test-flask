from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            num = int(request.form["number"])
            if num < 0:
                result = "Factorial is not defined for negative numbers."
            else:
                result = math.factorial(num)
        except ValueError:
            result = "Please enter a valid integer."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
