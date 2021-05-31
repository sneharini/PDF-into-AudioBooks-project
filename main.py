import pyttsx3
import PyPDF2

book = open("CD_notes.pdf",'rb')
pdfreader  = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(23,pages):
    page = pdfreader.getPage(23)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()