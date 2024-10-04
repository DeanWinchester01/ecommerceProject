from flask import Flask, url_for, redirect, render_template, request
app = Flask(__name__)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/page", methods = ["GET","POST"])
def page():
    #user = (request.method == 'POST') and request.form['nm'] or request.args.get('nm')
    return render_template("page.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)