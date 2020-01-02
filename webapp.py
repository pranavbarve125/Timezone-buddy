from flask import Flask, render_template, flash, redirect, url_for, session, request
from datetime import date
import data

app = Flask(__name__)
app.config["SECRET_KEY"] = "1737e4b44bd8ec494db26e5724b6e110"

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        return "Works"
    else:
        return render_template("index.html", users=4, timeslots=4, timezones=data.timezone_names)

if __name__ == '__main__':
    app.run(debug=True)