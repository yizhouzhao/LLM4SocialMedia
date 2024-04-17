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


#Encode Image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

#API Key Setup    
config = dotenv_values(".env")
print("-----------------[gemini] config", config)
genai.configure(api_key=config["GOOGLE_API_KEY"])
os.environ['GOOGLE_API_KEY'] = config["GOOGLE_API_KEY"]
# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#Image Path
image_path = 'C:/Users/madis/LLM4SocialMedia/examples/left_half.jpeg'
img = encode_image(image_path)

#Spatial Strategy Prompt Template --Gemini
Interest = "pet"
textgemi = genai.GenerativeModel('gemini-pro')
prompt1 = f"I am scrolling on TikTok, I am an illiterate person who is interested in {Interest}. Can you come up with 5 visual content related but is not {Interest} I would want to watch?"
response1 = textgemi.generate_content(prompt)
print(response1.text)

gemi = ChatGoogleGenerativeAI(model='gemini-pro-vision')
prompt2 = "Please point out there is a cat inside the image or not and describe the image."
message = HumanMessage(
    content=[
        {'type':'text','text':prompt},
        {'type':'image_url','image_url':image_path}
    ]
)
        
response2 = gemi.invoke([message])
print(response2.content)

#Spatial Strategy Prompt Template --GPT4 https://platform.openai.com/docs/models/continuous-model-upgrades==GPT4 Version lists
base64_image = encode_image(image_path)
from openai import OpenAI
client = OpenAI(api_key =config["OPENAI_KEY"])
response3 = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt1},
            ],
        }
    ],
    max_tokens=300,
)
print(response3.choices[0].message.content)

# client = OpenAI(api_key =config["OPENAI_KEY"])
response4 = client.chat.completions.create(
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

print(response4.choices[0].message.content)

