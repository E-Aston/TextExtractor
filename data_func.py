from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import csv
import PyPDF2


def convert_pdf_to_string(file_path):
    output_string = StringIO()
    with open(file_path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    return (output_string.getvalue())

def extract_metrics(file):

    reader = PyPDF2.PdfFileReader(file)

    text = convert_pdf_to_string(file)
    gr = (text.index("Ground resolution:"))

    groundres = (str(text[gr+20:gr+32]))

    fe = (text.index("Flying altitude"))

    flyingel = (str(text[fe+18:fe+24]))

    ce = (text.index("Coverage area"))

    coveragearea = (str(text[ce+16:ce+23]))

    list = [str(file), groundres, flyingel, coveragearea ]

    print(list)

    with open("Model Diagnostics.csv", "a", newline='') as f:
        write = csv.writer(f)
        write.writerow(list)
