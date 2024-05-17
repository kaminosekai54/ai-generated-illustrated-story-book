from crewai_tools import tool
from langchain_openai import ChatOpenAI
import os, requests, re, mdpdf, subprocess
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

@tool
def generateIllustration(chapterAndCharDesc: str) -> str:
    """
    Generates an illustration for a given chapter number, chapter content, detailed location details and character details.
    Using the OpenAI image generation API,
    saves it in the current folder, and returns the image path.
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.images.generate(
        model="dall-e-3",
        prompt=f"Image is about: {chapterAndCharDesc}. Style: Illustration. Create an illustration incorporating a colorful palette with round and cute shape, it should be suited for very young kid. Image should be augmented by splashes of gold and purple for contrast and visual interest. The style should evoke wonderland, full of love, friendship and magic, everything should look fluffy and cute, like a dream. The composition should be rich in texture, with a soft, luminous lighting that enhances the magical atmosphere. Attention to the interplay of light and shadow will add depth and dimensionality, inviting the viewer to delve into the scene. DON'T include ANY text in this image.",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    words = chapterAndCharDesc.split()[:5] 
    safe_words = [re.sub(r'[^a-zA-Z0-9_]', '', word) for word in words]  
    filename = "_".join(safe_words).lower() + ".png"
    filepath = os.path.join(os.getcwd(), filename)

    # Download the image from the URL
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open(filepath, 'wb') as file:
            file.write(image_response.content)
    else:
        print("Failed to download the image.")
        return ""

    return filepath

