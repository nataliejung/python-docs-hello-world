from flask import Flask



app = Flask(__name__)

@app.route("/")
def hello():
    #version = tika.__version__
    return "version"