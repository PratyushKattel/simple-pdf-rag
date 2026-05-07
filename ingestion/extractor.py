import pymupdf
from pathlib import Path    

def extract_text_from_pdf(pdf_path):
    '''
    Extracts text from a PDF file using the PyMuPDF library.
    Args:        pdf_path (str): The path to the PDF file.
    Returns:        str: The extracted text from the PDF file
    '''
    doc = pymupdf.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

