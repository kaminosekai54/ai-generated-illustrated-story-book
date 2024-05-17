from crewai_tools import tool
from langchain_openai import ChatOpenAI
import os, requests, re, mdpdf, subprocess
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
@tool
def convertMarkdownToPDF(markdownfile_name: str) -> str:
    """
    Converts a Markdown file to a PDF document using the mdpdf command line application.

    Args:
        markdownfile_name (str): Path to the input Markdown file.

    Returns:
        str: Path to the generated PDF file.
    """
    output_file = os.path.splitext(markdownfile_name)[0] + '.pdf'
    
    # Command to convert markdown to PDF using mdpdf
    cmd = ['mdpdf', '--output', output_file, markdownfile_name]
    
    # Execute the command
    subprocess.run(cmd, check=True)
    
    return output_file

import os
from md2pdf.core import md2pdf

def convert_markdown_to_pdf(markdownfile_name: str) -> str:
    with open(markdownfile_name, 'r', encoding='utf-8') as md_file:
        markdown_text = md_file.read()

    # List all files in the base_path directory
    for filename in os.listdir("./"):
        # Check if the file is an image (you can add more extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            absolute_path = os.path.join("./", filename)
            relative_path = os.path.relpath(absolute_path, os.path.dirname(markdownfile_name))
            markdown_text = markdown_text.replace(absolute_path, relative_path)

    # Convert and save the PDF
    md2pdf("test.pdf", md_content=markdown_text)

# Call the function with the base path of your images and the markdown file
# convert_markdown_to_pdf('path_to_your_markdown_file.md', 'C:/Users/culpi/Desktop/git-repo/ai-generated-illustrated-story-book')

convert_markdown_to_pdf("story.md")