from crewai import Agent
from crewai_tools import tool
import os, requests, re, mdpdf, subprocess
from textwrap import dedent
from openai import OpenAI
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools import generateIllustration
from mkdtools import convertMarkdownToPDF
from crewai_tools.tools import FileReadTool
from langchain_openai import AzureChatOpenAI

load_dotenv()

llm_model =ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-70b-8192"
        ) 

llm_model2 = AzureChatOpenAI(
    openai_api_version=os.environ.get("AZURE_OPENAI_VERSION"),
    azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
)
file_read_tool = FileReadTool(
	file_path='template.md',
	description='A tool to read the Story Template file and understand the expected output format.'
)

class storyAgent():
    def storyOutliner(self):
        return Agent(
            role='Story Outliner',
            goal="Create a simple and visually engaging outline for a children's storybook about Animals, including basic chapter titles and characters for 5 short chapters. Aimed at children aged 3 to 6 years old.",
            backstory=dedent("""\
                             As an imaginative creator crafting stories for very young children, you specialize in developing basic, clear, and colorful concepts that captivate and educate. Your outlines are the foundation of storybooks that introduce young minds to the wonders of reading through engaging animal characters and simple narratives.
                             """),
            allow_delegation=False,
            verbose=True,
            llm=llm_model,
        )

    def storyWriter(self):
        return Agent(
            role='Story Writer',
            goal="Write the content of the story for all 5 chapters, ensuring each chapter is about 100 words and uses simple language suitable for children aged 3 to 6. Seamlessly integrate the characters and settings from the outline.",
            backstory=dedent("""\
                             You are a talented storyteller with a flair for writing enchanting and simple stories that resonate with preschoolers. Your task is to weave narratives that are easy to follow, filled with gentle humor and clear morals, fostering a love for reading in young children.
                             """),
            allow_delegation=False,
            verbose=True,
            llm=llm_model,
        )

    def imageGenerator(self):
        return Agent(
            role='Image Generator',
            goal="Generate one bright and cheerful image for each chapter, focusing on clear, colorful depictions of animals and simple scenes that appeal to children aged 3 to 6. Produce a total of 5 images, ensuring they are visually stimulating for young children.",
            backstory=dedent("""
                             As a creative AI specializing in visual storytelling for young children, you transform written stories into vibrant, captivating images. Your artwork supports early learning by emphasizing bold, recognizable shapes and colors that grab the attention of young readers.
                             """),
            tools=[generateIllustration],
            allow_delegation=False,
            verbose=True,
            llm=llm_model2,
        )

    def contentFormatter(self):
        return Agent(
            role='Content Formatter',
            goal="Arrange the written story content in a simple markdown format suitable for young children, including placing the colorful images at the beginning of each chapter to immediately engage young readers.",
            backstory=dedent("""
                             As a meticulous formatter focused on children's books, you enhance readability and visual appeal for young children. Your expertise in layout ensures that each page is not only beautiful but also perfectly suited to hold the fleeting attention of preschoolers.
                             """),
            allow_delegation=False,
            verbose=True,
            llm=llm_model2,
            tools=[file_read_tool],
        )

    def markdownToPdfCreator(self):
        return Agent(
            role='PDF Converter',
            goal="Convert the simple Markdown story file into a PDF document, ensuring it's formatted in a way that's easy for young children to engage with. The file 'story.md' is the markdown file name.",
            backstory=dedent("""
                             As an efficient converter, you transform simple Markdown files into colorful, professionally formatted PDF documents. Your role is crucial in producing final storybooks that are easy for young children to handle and visually appealing.
                             """),
            allow_delegation=False,
            verbose=True,
            llm=llm_model2,
            tools=[convertMarkdownToPDF],
        )
