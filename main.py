import gradio as gr
from content_generator import generate_output
from utils import copy_text

# Create the Gradio interface
iface = gr.Interface(
    fn=generate_output, 
    inputs=[
        gr.File(file_types=[".pdf"]),  # PDF file upload input
        gr.Textbox(lines=6, placeholder="Paste the job description here...", label="Job Description")  # Job description textbox input
    ],
    outputs=gr.Textbox(label="Generated Cover Letter", show_copy_button=True),
    live=False,  # Disable live updates, output will only be generated on button click
    title="Cover Letter Generator",
    description="Upload a PDF file to extract its content and paste the job description. Click 'Submit' to see the result.",

)

# Add the "Generate" button
iface.launch()