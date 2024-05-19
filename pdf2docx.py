import PyPDF2
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from docx import Document

# Define the path to the PDF
pdf_path = 'path_to_your_pdf.pdf'

# Convert the PDF to images
images = convert_from_path(pdf_path)

# Create a new Word document
doc = Document()

# Perform OCR on each image
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image)
    
    # Add the text to the Word document
    doc.add_paragraph(text)

# Save the Word document
doc.save('output.docx')