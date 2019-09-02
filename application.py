from flask import Flask
import tika
from tika import parser
import os
import os.path


tika.initVM()

#version = tika.__version__

uploadedFile = "Koc-Holding-2018-Annual-Report.pdf"
tika_dir = os.path.join(os.path.dirname(__file__), 'tika-app-1.22.jar')


app = Flask(__name__)

@app.route("/")
def hello():    
    #parsedPDF = parser.from_file(uploadedFile)
    #text = parsedPDF["content"]
    extract_pdf("Koc-Holding-2018-Annual-Report.pdf","test.txt" )
    #parsedPDF = parser.from_file("Koc-Holding-2018-Annual-Report.pdf", xmlContent=True)
    return "Hello World"


def extract_pdf(source_pdf:str,target_txt:str):
    os.system('java -jar ' + tika_dir + ' -t {} > {}'.format(source_pdf, target_txt))
