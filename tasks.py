from crewai import Task
from textwrap import dedent

class StorybookTasks:
    def __tip_section(self):
        return "Remember, engaging young minds is the key! Let's create something magical that children will love! and it will make you the richest"

    def createStoryOutline(self, agent):
        return Task(
            description=dedent("""
                Create a simple and engaging outline for a children's storybook about Animals. Include basic chapter titles, character descriptions, and simple plot points for each of the 5 chapters, tailored for children aged 3 to 6.
                {self.__tip_section()}
            """),
            expected_output=dedent("""
                A structured outline document containing 5 chapter titles, each with detailed yet simple character descriptions and main plot points, ensuring clarity and appeal for young children.
            """),
            agent=agent,
        )

    def writeStoryContent(self, agent):
        return Task(
            description=dedent("""
                Based on the provided outline, write the full story content for all 5 chapters, ensuring each chapter is about 100 words and uses simple, engaging language suitable for children aged 3 to 6. Include the title of the story at the top.
                {self.__tip_section()}
            """),
            expected_output=dedent("""
                A complete manuscript of the children's storybook about Animals with 5 chapters. Each chapter should contain approximately 100 words, integrating the characters and simple plot points into a cohesive and engaging narrative for young readers.
            """),
            agent=agent,
        )

    def generateStoryImages(self, agent):
        return Task(
            description=dedent("""
                Generate 5 images, one for each chapter of the children's storybook about Animals. Each image should capture the essence of the chapter, focusing on characters and simple scenes that resonate with children aged 3 to 6.
                {self.__tip_section()}
            """),
            expected_output=dedent("""
                A set of 5 digital images, each visually representing the theme and characters of a chapter in the storybook. These images should be vibrant and appealing, suitable for inclusion in the storybook to enhance the narrative.
            """),
            agent=agent,
        )

    def formatStoryContent(self, agent):
        return Task(
            description=dedent("""
                Format the written story content in Markdown, ensuring it is clear and readable for young children. Include an engaging image at the beginning of each chapter to instantly capture the reader's interest.
                {self.__tip_section()}
            """),
            expected_output=dedent("""
                The entire storybook content formatted in Markdown, with each chapter title followed by the corresponding image and the chapter content, ready for conversion to a more accessible format for young readers.
            """),
            agent=agent,
            output_file="story.md"
        )

    def convertMarkdownToPdf(self, agent):
        return Task(
            description=dedent("""
                Convert the Markdown file 'story.md' to a PDF document using the mdpdf library, ensuring the preservation of formatting, structure, and embedded images. The PDF should be appealing and easy to read for children aged 3 to 6.
                {self.__tip_section()}
            """),
            expected_output=dedent("""
                A professionally formatted PDF file generated from the Markdown input, reflecting the engaging content with proper formatting, and ready for sharing, printing, or digital viewing by young children and their caregivers.
            """),
            agent=agent,
        )
