# Books-into-AudioBooks
Installation:
Python has an ocean of libraries that serve various purposes. In this article, we will require two libraries (pyttsx3, PyPDF2) to develop an audiobook.
You can install the libraries from PyPl,
      pip install PyPDF2
      pip install pyttsx3
---------------------------------------------------------
1) Read the PDF file:
Python has library PyPDF2 which is built as a PDF toolkit. It allows pdf manipulation in memory. This library is capable of:
extracting document information, such as title, author, etc
splitting documents by page
merging documents by page
cropping pages
merging multiple pages into a single page
encrypting and decrypting PDF file
       import PyPDF2
       pdfReader = PyPDF2.PdfFileReader(open('file.pdf', 'rb'))
----------------------------------------------------------
2) Initialize Speaker:
Python has a library pyttsx3, that is capable to convert text-to-speech offline. Text that we are reading from a pdf file using the pypdf2 library is fed as an input to the text-to-speech engine.
       import pyttsx3
       speaker = pyttsx3.init()
