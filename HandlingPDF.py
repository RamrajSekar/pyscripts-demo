import PyPDF2 as pypdf

pdfFileObj = open('ticket.pdf', 'rb')
pdfReader = pypdf.PdfFileReader(pdfFileObj)

#To get the number of pages in pdf
print(pdfReader.numPages)

#To get text from pdf
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

