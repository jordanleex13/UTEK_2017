from flask import Flask,render_template,url_for
APP = Flask(__name__)

@APP.route("/")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    APP.run()