


import fitz

def parse_pdf(file_path):
    doc = fitz.open(file_path)
    chunks = []
    
    for page in doc:
        text = page.get_text()

        for para in text.split("\n\n"):
            if len(para.strip()) > 100:
                chunks.append(para.strip())
        
    return chunks