from cover_letter_generator import get_cover_letter
from utils import read_pdf

def generate_output(pdf, job_description):

    resume_content = read_pdf(pdf)
    cover_letter = get_cover_letter(resume_content, job_description)

    return cover_letter

    