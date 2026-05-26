import pymupdf
from pathlib import Path    
import pymupdf4llm

def extract_text_from_pdf(pdf_path): 
    # doc = pymupdf.open(pdf_path)
    # text = ""
    # for page in doc:
    #     text += page.get_text()
    # return text.strip()

    data = pymupdf4llm.to_markdown(pdf_path)
    return data

# with open("ingestion/test.md",'w') as f:
#     f.write(extract_text_from_pdf("ingestion/test.pdf"))