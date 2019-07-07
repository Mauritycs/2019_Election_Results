# from flask import Flask, jsonify, render_template, url_for, request, redirect
from flask import Flask
app = Flask(__name__)


# # create route that renders index.html template
# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route("/")
def hello():
    return "hello world"

# # route to the arabic page 
# @app.route("/arabic")
# def arabic():
#     """ renders the arabic version of the analysis"""
#     return render_template("arabic.html")

# # route to the french page 
# @app.route("/french")
# def french():
#     """ renders the french version of the analysis """
#     return render_template("french.html")


if __name__ == "__main__":
    app.run()

