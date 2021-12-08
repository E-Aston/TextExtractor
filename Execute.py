# To make this go, install pdfminer.six and PyPDF2 using pip from the command line. Simples. Then it just needs
# data_func.py and to be pointed to the right folder using directory =

import data_func
import csv
import os

Variable_names = ['File_Path', "Ground Resolution", "Flying elevation", "Coverage Area"]  # Sets up a CSV with variable
# names in current dir. Note the "w" is for write, so every time you run it, it overwrites the old one. Otherwise it just adds it on to the end
with open("Model Diagnostics.csv", "w", newline='') as f:
    write = csv.writer(f)
    write.writerow(Variable_names)

directory = "C:/Your/Directory"  # Sets WD where pdf files are stored - INPUT NEEDED
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        data_func.extract_metrics(os.path.join(directory, filename))
    else:
        continue