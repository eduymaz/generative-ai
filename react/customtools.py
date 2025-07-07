from langchain.agents import Tool
from openai import OpenAI
from bs4 import BeautifulSoup
from io import BytesIO
import base64
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


my_key_openai = os.getenv("openai_apikey")
my_key_stabilityai = os.getenv("stability_apikey")





def generate_image_with_dalle(prompt):

    AI_Response = client.images.generate(
        model = "dall-e-3",
        size = "1024x1024",
        quality = "hd",
        n = 1,
        response_format = "url",
        prompt = prompt
    )

    image_url = AI_Response.data[0].url

    response = requests.get(image_url)
    image_bytes = BytesIO(response.content)

    timestamp = datetime.now().strftime("&Y&m&d_%H%M%S")
    filepath = f"./img/generated_image_{timestamp}.png"


    if not os.path.exists("./img"):
        os.makedirs("./img")

    with open(filepath, "wb") as file:
        file.write(image_bytes.getbuffer())
    
    return f'<a href="{filepath}">Resminizi Burada </a>'


def generate_with_SD(prompt):
    url = "https: ...."




def get_tool(selected_image_generator):
    if selected_image_generator == "DALL-E 3":
        return Tool(
            name = "Generate Image",           
            func = generate_image_with_dalle,
            description = """ In this text """ # buraya metin girilmelidir.
        )


    elif selected_image_generator == "Stable Diffusion XL":
        return Tool(
            name = "Generate Image",           
            func = generate_with_SD,
            description = """ In this text """ # buraya metin girilmelidir.
        )


def analyze_webpage(target_url):

    response = requests.get(target_url)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser") # ajan tarafından okunnur hale getiriilmesi için eklendi.
    stripped_content = soup.get_text()

    if len(stripped_content) > 4000:
        stripped_content = stripped_content[:4000]

    return stripped_content

def get_web_tool():
    return Tool(
        name = "Get Webpage",
        func=analyze_webpage,
        description="Useful for when you need to get the http from a specific webpage"

    )