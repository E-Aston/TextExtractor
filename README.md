# TextExtractor
Extracting customised parts of PDF files. Useful for when there are many files with the same structure and you want information from all of them.
Set up for extracting some useful things from model reports that come from Agisoft Metashape that don't appear to be extractable any other way. 

You just need both files, data_func which has the functions embedded that do the work, as well as Execure, which makes it go. 

You need PyPDF2 and pdfminer.six installed as packages using pip to make it go. Output is a .csv file in the current environment. 
