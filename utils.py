import fitz

def read_pdf(pdf_file):

    doc = fitz.open(pdf_file.name)

    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()

    return text

def copy_text(output_text):

    return output_text