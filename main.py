from flask import Flask
from page import pageBP
from login import loginBP
from signup import signupBP

app = Flask(__name__)

app.register_blueprint(pageBP)
app.register_blueprint(signupBP)
app.register_blueprint(loginBP)

if __name__ == "__main__":
    app.run(debug=True)