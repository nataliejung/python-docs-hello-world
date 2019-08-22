from flask import Flask
from tika import parser



app = Flask(__name__)

@app.route("/")
def hello():
    #version = tika.__version__
    return "version"