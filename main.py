import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfdoc
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.acroform import acroform

def extract_pdf(filename):
    document = fitz.open(filename)
    markers = []
    
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text('dict')
        
        for block in text['blocks']:
            for line in block['lines']:
                for span in line['spans']:
                    if "\uf0a8" in span["text"]:
                        markers.append({
                            "type": "radio",
                            "x": span["bbox"][0],
                            "y": span["bbox"][1],
                            "page_num": page_num
                        })
                    elif "___" in span["text"]:
                        markers.append({
                            "type": "text",
                            "x": span["bbox"][0],
                            "y": span["bbox"][1],
                            "width": span["bbox"][2] - span["bbox"][0],
                            "page_num": page_num
                        })
                        
    return markers
                        
                    
pdf = extract_pdf('./Form.pdf')
print(pdf)