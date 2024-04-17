import os
# print("Current Folder:", os.getcwd())
# os.chdir('C:/Users/madis/LLM4SocialMedia')
from IPython.display import display
from IPython.display import Markdown
import textwrap
import google.generativeai as genai
from dotenv import dotenv_values
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

    
    
    
config = dotenv_values(".env")
print("-----------------[gemini] config", config)
genai.configure(api_key=config["GOOGLE_API_KEY"])
os.environ['GOOGLE_API_KEY'] = config["GOOGLE_API_KEY"]
# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#
image_path = 'C:/Users/madis/LLM4SocialMedia/examples/left_half.jpeg'
img = encode_image(image_path)

llm = ChatGoogleGenerativeAI(model='gemini-pro-vision')
prompt = "Please point out there is a cat inside the image or not and describe the image."
message = HumanMessage(
    content=[
        {'type':'text','text':prompt},
        {'type':'image_url','image_url':image_path}
    ]
)
        
         
response = llm.invoke([message])
print(response.content)


base64_image = encode_image(image_path)
from openai import OpenAI
client = OpenAI(api_key =config["OPENAI_KEY"] )
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Please point out there is a cat inside the image or not and describe the image."},
                {
                    "type": "image_url",
                    "image_url":  f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0].message.content)

