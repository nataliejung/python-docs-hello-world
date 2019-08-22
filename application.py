from flask import Flask
from tika import parser


uploadedFile = "Koc-Holding-2018-Annual-Report.pdf"
app = Flask(__name__)

@app.route("/")
def hello():
   parsedPDF = parser.from_file("Koc-Holding-2018-Annual-Report.pdf", xmlContent=True)
   return uploadedFile