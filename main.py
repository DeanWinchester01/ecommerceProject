from flask import Flask, redirect
from Search import searchBp
from page import pageBP
from login import loginBP
from signup import signupBP
from upload import uploadBP

app = Flask(__name__)


app.register_blueprint(searchBp)
app.register_blueprint(pageBP)
app.register_blueprint(signupBP)
app.register_blueprint(loginBP)
app.register_blueprint(uploadBP)

@app.route("/")
def mainPage():
    return redirect("/login")

app.run(debug=True)