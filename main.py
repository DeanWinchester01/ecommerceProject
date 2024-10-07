from flask import Flask, redirect
from page import pageBP
from login import loginBP
from signup import signupBP

app = Flask(__name__)

app.register_blueprint(pageBP)
app.register_blueprint(signupBP)
app.register_blueprint(loginBP)

@app.route("/")
def mainPage():
    return redirect("/login")

app.run(debug=True)