from flask import Flask
import tika
from tika import parser


tika.initVM()
#version = tika.__version__

uploadedFile = "Koc-Holding-2018-Annual-Report.pdf"
app = Flask(__name__)

@app.route("/")
def hello():
    parsedPDF = parser.from_file(uploadedFile)
    text = parsedPDF["content"]
    #parsedPDF = parser.from_file("Koc-Holding-2018-Annual-Report.pdf", xmlContent=True)
    return text