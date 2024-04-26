import requests
import pyautogui
import os
from IPython.display import display
from IPython.display import Markdown
import textwrap
import google.generativeai as genai
from dotenv import dotenv_values
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from openai import OpenAI
import base64
import re
import csv

def llava_image_to_text(prompt, Img):

    CONTEXT = "You are LLaVA, a large language and vision assistant trained by UW Madison WAIV Lab. You are able to understand the visual content that the user provides, the user provided a base64 image strings consist of different characters, please regard it as a picture, and assist the user with a variety of tasks using natural language. Follow the instructions carefully and explain your answers in detail.### Human: Hi!### Assistant: Hi there! How can I help you today?\n"

    with open(Img, 'rb') as f:
        
        img_str = base64.b64encode(f.read()).decode('utf-8')
        prompt = CONTEXT + f'### Human: {prompt}: \n<img src="data:image/jpeg;base64,{img_str}">### Assistant: '
        response = (requests.post('http://127.0.0.1:5000/v1/completions', json={'prompt': prompt, 'max_tokens':100, 'stop': ['\n###']}).json())
        response = str(response)
        pattern = r"'text': (.*?), 'logprobs'"

        match = re.search(pattern, response)
        if match:
            extracted_text = match.group(1)
            print(extracted_text)
    return extracted_text

def llava_chat(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    history = []
    predictions = []

    url = "http://127.0.0.1:5000/v1/chat/completions"
    
    
    ######strategy!!!###########
    user_message = prompt
    history.append({"role": "user", "content": user_message})
    
    data = {
        "mode": "chat",
        "messages": history
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    assistant_message = response.json()['choices'][0]['message']['content']
    print(assistant_message)
    return assistant_message



def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def gpt_image_to_text(prompt, image_path, config):
    base64_image = encode_image(image_path)
    client = OpenAI(api_key =config["OPENAI_KEY"] )
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url":  f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        ],
    max_tokens=300,
    )
    text = response.choices[0].message.content
    return text
#gpt4v apikey and 
def gpt_chat(prompt, config):
    client = OpenAI(api_key =config["OPENAI_KEY"])
    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
            ],
        }
    ],
    max_tokens=300,
    )
    text = response.choices[0].message.content
    return text

# def gemini_image_to_text(prompt, image_path, config):
#     genai.configure(api_key=config["GOOGLE_API_KEY"])
#     os.environ['GOOGLE_API_KEY'] = config["GOOGLE_API_KEY"]
#     img = encode_image(image_path)

#     llm = ChatGoogleGenerativeAI(model='gemini-pro-vision')
#     message = HumanMessage(
#         content=[
#             {'type':'text','text':prompt},
#             {'type':'image_url','image_url':image_path}
#         ]
#     )
          
            
#     response = llm.invoke([message])
#     print(f"-------here is the image{image_path} to text-------")
#     print(response.content)
#     print("end of image to text")
#     return str(response.content)
from google.generativeai.types import generation_types

def gemini_image_to_text(prompt, image_path, config):
    try:
        genai.configure(api_key=config["GOOGLE_API_KEY"])
        os.environ['GOOGLE_API_KEY'] = config["GOOGLE_API_KEY"]
        
        # Assuming you have a function named encode_image to encode the image
        img = encode_image(image_path)

        llm = ChatGoogleGenerativeAI(model='gemini-pro-vision')
        message = HumanMessage(
            content=[
                {'type':'text','text':prompt},
                {'type':'image_url','image_url':image_path}
            ]
        )
                
        response = llm.invoke([message])
        print(f"-------here is the image{image_path} to text-------")
        print(response.content)
        print("end of image to text")
        return str(response.content)

    except generation_types.StopCandidateException as e:
        print("StopCandidateException: Raised when the model stops generating candidates.")
        print("This can occur due to various reasons such as safety concerns, maximum length reached, or other internal model decisions.")
        return "Exception occurred"
    except generation_types.BlockedPromptException as e:
        print("BlockedPromptException: Raised when the prompt provided to the model is blocked for generating content.")
        print("This can happen if the prompt violates content policies or is deemed inappropriate.")
        return "Exception occurred"
    
def gemini_chat(prompt, config):
    genai.configure(api_key=config["GOOGLE_API_KEY"])
    os.environ['GOOGLE_API_KEY'] = config["GOOGLE_API_KEY"]
    textgemi = genai.GenerativeModel('gemini-pro')
    response = textgemi.generate_content(prompt)
    print("----------------here is chat content ----------------")
    print(response.text)
    print("end of content")
    return str(response.text)


def save_to_csv(self, image_path, extracted_text, interest, response):
    with open(f'{self.name}.csv', 'a', newline='') as csvfile:
        fieldnames = ['Image Path', 'Extracted Text', 'Interest', 'Response']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Image Path': image_path, 'Extracted Text': extracted_text, 'Interest': interest, 'Response': response})

class GPT4:
    def __init__(self):
        self.name = 'GPT4'
        self.config = dotenv_values(".env")


    def simple_strategy(self,image_path,interest):
        prompt1 = "Describe this image in English"
        extracted_text = gpt_image_to_text(prompt1, image_path, self.config)
        prompt2 = f"""I am a {interest} lover, and I am scrolling on TikTok to find interest videos, and this video is about {extracted_text}. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word."""
        response = gpt_chat(prompt2, self.config)
        self.save_to_csv(image_path, extracted_text, interest, response)
        return str(response) 
        #(yes/no)
    

class Llava:
    def __init__(self):
        self.name = 'llava'
    
    def simple_strategy(self, image_path, interest):
        prompt1 = "please Describe this image in a few words in English"
        extracted_text = llava_image_to_text(prompt1, image_path)
        prompt2 = f"""I am a {interest} lover, and I am scrolling on TikTok to find interest videos, and this video is about {extracted_text}. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word."""
        response = llava_chat(prompt2)
        return str(response)

class Gemini:
    def __init__(self):
        self.name = 'gemini'
        self.config = dotenv_values(".env")
    def plain_strategy(self, image_path, interets):
        prompt1 = "please Describe this image in a few words in English"
        extracted_text = gemini_image_to_text(prompt1, image_path,self.config)
        prompt2 = f"I am scrolling on TikTok, and this video is about {extracted_text}. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word."
        response = gemini_chat(prompt2,self.config)
        return str(response)
    def simple_strategy(self, image_path, interest):
        prompt1 = "please Describe this image in a few words in English"
        extracted_text = gemini_image_to_text(prompt1, image_path,self.config)
        if(extracted_text == "Exception occurred"):
            return "no"
        prompt2 = f"""I am a {interest} lover, and I am scrolling on TikTok to find {interest} videos, and this video is about {extracted_text}. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word."""
        response = gemini_chat(prompt2,self.config)
        return str(response)
    def spacial_strategy(self, image_path, interest, cate1, cate2, cate3, cate4, cate5):
        prompt1 = "please Describe this image in a few words in English"
        extracted_text = gemini_image_to_text(prompt1, image_path,self.config)
        prompt2 = f"I am scrolling on TikTok, and this video is about {extracted_text}, given 7 catergories: {cate1}, {cate2}, {cate3}, {cate4}, {cate5}, {interest}, other.  Help me decide which category it belongs to. Please answer in a single word."
        response = gemini_chat(prompt2,self.config)
        return str(response)
    def ask_general(self, interest):
        prompt = f"I am scrolling on TikTok, I am an illiterate person who is interested in {interest}. Can you come up with general visual content related but is not {interest} I would want to watch? Answer short word separated in commas. Your response should only be the answer."
        response = gemini_chat(prompt,self.config)
        response.replace(".", '')
        categories = re.split(r'\s*,\s*', response)
        cate1, cate2, cate3, cate4, cate5 = categories[:5]
        return cate1, cate2, cate3, cate4, cate4, cate5
    

    
        