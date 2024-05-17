import os
from crewai import Agent, Task, Crew, Process
from textwrap import dedent
from agents import storyAgent
from tasks import StorybookTasks
import warnings
warnings.filterwarnings('ignore')


class StorybookCreationCrew:
    def __init__(self):
        self= self

    def run(self):
        # Initialize agents
        agents = storyAgent()
        story_outliner = agents.storyOutliner()
        story_writer = agents.storyWriter()
        image_generator = agents.imageGenerator()
        content_formatter = agents.contentFormatter()
        markdown_to_pdf_creator = agents.markdownToPdfCreator()

        # Initialize tasks
        tasks = StorybookTasks()
        task_outline = tasks.createStoryOutline(story_outliner)
        task_write = tasks.writeStoryContent(story_writer)
        task_image_generate = tasks.generateStoryImages(image_generator)
        task_format_content = tasks.formatStoryContent(content_formatter)
        task_markdown_to_pdf = tasks.convertMarkdownToPdf(markdown_to_pdf_creator)

        # Define crew
        crew = Crew(
            agents=[
                story_outliner,
                story_writer,
                image_generator,
                content_formatter,
                markdown_to_pdf_creator,
            ],
            tasks=[
                task_outline,
                task_write,
                task_image_generate,
                task_format_content,
                task_markdown_to_pdf,
            ],
            verbose=True,
            process=Process.sequential
        )

        # Execute tasks
        result = crew.kickoff()

        return result


# Example usage with Streamlit
if __name__ == "__main__":
    print("## Welcome to Storybook Creation Crew")
    print('-------------------------------')
    story_creation_crew = StorybookCreationCrew()
    result = story_creation_crew.run()
    print("\n\n########################")
    print("## Here is the Created Storybook")
    print("########################\n")
    print(result)
