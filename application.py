from flask import Flask
import tika
from tika import parser

print("initiating tika")
tika.initVM()
print("initiating VM")
version = tika.__version__
print("tika version: " + version)

uploadedFile = "Koc-Holding-2018-Annual-Report.pdf"
app = Flask(__name__)

@app.route("/")
def hello():
    print("Hello")
    parsedPDF = parser.from_file("Koc-Holding-2018-Annual-Report.pdf", xmlContent=True)
    return uploadedFile