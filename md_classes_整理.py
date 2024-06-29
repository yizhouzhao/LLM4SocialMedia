import requests
import pyautogui
import os
from IPython.display import display
from IPython.display import Markdown
import textwrap
import google.generativeai as genai
from dotenv import dotenv_values
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from openai import OpenAI
import base64
import re
from google.generativeai.types import generation_types



def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


#############################################
#                                           #
#                  GPT4O                    #
#                                           #
#############################################


#############################################
#                                           #
#                  Plain                    #
#                                           #
#############################################

#无性格，gpto图文，yes/no
def gpto_image_to_text(prompt, image_path, config):
    try:
        base64_image = encode_image(image_path)
        client = OpenAI(api_key =config["OPENAI_KEY"] )
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. You should provide your opinion."},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}",
                "detail": "high"
            },
                        },
                    ],
                }
            ],
        max_tokens=300,
        )
        text = response.choices[0].message.content
        return text
    except openai.InvalidRequestError as e:
        print(f"InvalidRequestError: {e}")
        return "Exception occurred"
    except openai.BadRequestError as e: # Don't forget to add openai
  # Handle error 400
        print(f"Error 400: {e}")
        return "Exception occurred"

#无性格，gpto图文，reason
def gpto_reason(prompt1, extracted_message1 ,prompt2, image_path, config):
    try:
        base64_image = encode_image(image_path)
        client = OpenAI(api_key =config["OPENAI_KEY"] )
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. You should provide your opinion."},
                {"role": "user", "content": prompt1},
                {"role": "assistant", "content": extracted_message1},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt2},
                        {
                            "type": "image_url",
                            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}",
                "detail": "high"
            },
                        },
                    ],
                }
            ],
        max_tokens=300,
        )
        text = response.choices[0].message.content
        return text
    except openai.InvalidRequestError as e:
        print(f"InvalidRequestError: {e}")
        return "Exception occurred"

    except openai.BadRequestError as e: # Don't forget to add openai
  # Handle error 400
        print(f"Error 400: {e}")
        return "Exception occurred"

def gpto_unbiased_discription(prompt, image_path, config):
    base64_image = encode_image(image_path)
    client = OpenAI(api_key =config["OPENAI_KEY"] )
    response = client.chat.completions.create(
        model="gpt-4o",
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


#############################################
#                                           #
#                  Persona                  #
#                                           #
#############################################

#有性格，图文，yes/no
def gpto_persona_decision(persona, prompt, image_path, config):
    try:
        base64_image = encode_image(image_path)
        client = OpenAI(api_key =config["OPENAI_KEY"] )
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You are a person who have the following traits {persona}. Provide opinion based as this person."},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}",
                "detail": "high"
            },
                        },
                    ],
                }
            ],
        max_tokens=300,
        )
        text = response.choices[0].message.content
        return text
    except openai.InvalidRequestError as e:
        print(f"InvalidRequestError: {e}")
        return "Exception occurred"

    except openai.BadRequestError as e: # Don't forget to add openai
  # Handle error 400
        print(f"Error 400: {e}")
        return "Exception occurred"




#有性格，图文，reason
def gpto_persona_reason(persona,prompt1, extracted_message1 ,prompt2, image_path, config):
    try:
        base64_image = encode_image(image_path)
        client = OpenAI(api_key =config["OPENAI_KEY"] )
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You are a person who have the following traits {persona}. Provide opinion based as this person."},
                {"role": "user", "content": prompt1},
                {"role": "assistant", "content": extracted_message1},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt2},
                        {
                            "type": "image_url",
                            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}",
                "detail": "high"
            },
                        },
                    ],
                }
            ],
        max_tokens=300,
        )
        text = response.choices[0].message.content
        return text
    except openai.InvalidRequestError as e:
        print(f"InvalidRequestError: {e}")
        return "Exception occurred"

    except openai.BadRequestError as e: # Don't forget to add openai
  # Handle error 400
        print(f"Error 400: {e}")
        return "Exception occurred"

#############################################
#                                           #
#        Spacial(ask general)               #
#                                           #
#############################################

#性格，无图，只问
def gpto_peron_chat(persona, prompt, config):
    client = OpenAI(api_key =config["OPENAI_KEY"])
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
          {"role": "system", "content": f"You are a person who have the following traits {persona}. Provide opinion based as this person."},
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



#############################################
#                                           #
#                 GPT                       #
#                                           #
#############################################

#############################################
#                                           #
#                  Plain                    #
#                                           #
#############################################

def gpt_image_to_text(prompt, image_path, config):
    base64_image = encode_image(image_path)
    client = OpenAI(api_key =config["OPENAI_KEY"] )
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. You should provide your opinion."},
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


def gpt_reason(prompt1, extracted_message1 ,prompt2, image_path, config):
    
    try:
        base64_image = encode_image(image_path)
        client = OpenAI(api_key =config["OPENAI_KEY"] )
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. You should provide your opinion."},
                {"role": "user", "content": prompt1},
                {"role": "assistant", "content": extracted_message1},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt2},
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
    except openai.InvalidRequestError as e:
        print(f"InvalidRequestError: {e}")
        return "Exception occurred"

    except openai.BadRequestError as e: # Don't forget to add openai
  # Handle error 400
        print(f"Error 400: {e}")
        return "Exception occurred"

#############################################
#                                           #
#           simple(persona)                 #
#                                           #
#############################################

def gpt_persona_decision(persona, prompt, image_path, config):
    try:
        base64_image = encode_image(image_path)
        client = OpenAI(api_key =config["OPENAI_KEY"] )
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {"role": "system", "content": f"You are a person who have the following traits {persona}. Provide opinion based as this person."},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}",
                "detail": "high"
            },
                        },
                    ],
                }
            ],
        max_tokens=300,
        )
        text = response.choices[0].message.content
        return text
    except openai.InvalidRequestError as e:
        print(f"InvalidRequestError: {e}")
        return "Exception occurred"

    except openai.BadRequestError as e: # Don't forget to add openai
  # Handle error 400
        print(f"Error 400: {e}")
        return "Exception occurred"
    

def gpt_persona_reason(persona,prompt1, extracted_message1 ,prompt2, image_path, config):
    try:
        base64_image = encode_image(image_path)
        client = OpenAI(api_key =config["OPENAI_KEY"] )
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {"role": "system", "content": f"You are a person who have the following traits {persona}. Provide opinion based as this person."},
                {"role": "user", "content": prompt1},
                {"role": "assistant", "content": extracted_message1},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt2},
                        {
                            "type": "image_url",
                            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}",
                "detail": "high"
            },
                        },
                    ],
                }
            ],
        max_tokens=300,
        )
        text = response.choices[0].message.content
        return text
    except openai.InvalidRequestError as e:
        print(f"InvalidRequestError: {e}")
        return "Exception occurred"

    except openai.BadRequestError as e: # Don't forget to add openai
  # Handle error 400
        print(f"Error 400: {e}")
        return "Exception occurred"
    

#############################################
#                                           #
#                   Spacial                 #
#                                           #
#############################################
    
def gpt_person_chat_alert(persona, prompt, config):
    client = OpenAI(api_key =config["OPENAI_KEY"])
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
          {"role": "system", "content": f"You are a person who have the following traits {persona}. Provide opinion based as this person."},
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



#############################################
#                                           #
#                Gemini                     #
#                                           #
#############################################


#############################################
#                                           #
#                Plain                      #
#                                           #
#############################################

def gemini_image_to_text(prompt, image_path, config):
    try:
        genai.configure(api_key=config["GOOGLE_API_KEY"])
        os.environ['GOOGLE_API_KEY'] = config["GOOGLE_API_KEY"]

        llm = ChatGoogleGenerativeAI(model='gemini-pro-vision')
        system_message = SystemMessage(content="You are a helpful assistant. You should give opinion of your own")
        message = HumanMessage(
            content=[
                {'type': 'text', 'text': prompt},
                {'type': 'image_url', 'image_url': image_path}
            ]
        )
                
        response = llm.invoke([system_message, message])
        # print(f"-------here is the image {image_path} to text-------")
        # print(response.content)
        # print("end of image to text")
        return str(response.content)

    except generation_types.StopCandidateException as e:
        print("StopCandidateException: Raised when the model stops generating candidates.")
        print("This can occur due to various reasons such as safety concerns, maximum length reached, or other internal model decisions.")
        return "Exception occurred"
    except generation_types.BlockedPromptException as e:
        print("BlockedPromptException: Raised when the prompt provided to the model is blocked for generating content.")
        print("This can happen if the prompt violates content policies or is deemed inappropriate.")
        return "Exception occurred"


#############################################
#                                           #
#             Simple(person)                #
#                                           #
#############################################

def gemini_person_decision(persona, prompt, image_path, config):
    try:
        genai.configure(api_key=config["GOOGLE_API_KEY"])
        os.environ['GOOGLE_API_KEY'] = config["GOOGLE_API_KEY"]

        llm = ChatGoogleGenerativeAI(model='gemini-pro-vision')
        system_message = SystemMessage(content=f"You are a person who have the following traits {persona}. Provide opinion based as this person.")
        message = HumanMessage(
            content=[
                {'type': 'text', 'text': prompt},
                {'type': 'image_url', 'image_url': image_path}
            ]
        )
                
        response = llm.invoke([system_message, message])
        print(f"-------here is the image {image_path} to text-------")
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


#############################################
#                                           #
#                Spacial                    #
#                                           #
#############################################

def gemini_person_chat(persona, prompt, config):
    genai.configure(api_key=config["GOOGLE_API_KEY"])
    os.environ['GOOGLE_API_KEY'] = config["GOOGLE_API_KEY"]
    textgemi = genai.GenerativeModel( model_name="gemini-pro",
  system_instruction=f"You are a person who have the following traits {persona}. Provide opinion based as this person.")
    response = textgemi.generate_content(prompt)
    print("----------------here is chat content ----------------")
    print(response.text)
    print("end of content")
    return str(response.text)

def gemini_chat(prompt, config):
    genai.configure(api_key=config["GOOGLE_API_KEY"])
    os.environ['GOOGLE_API_KEY'] = config["GOOGLE_API_KEY"]
    textgemi = genai.GenerativeModel('gemini-pro')
    response = textgemi.generate_content(prompt)
    print("----------------here is chat content ----------------")
    print(response.text)
    print("end of content")
    return str(response.text)



class GPT4o:
    def __init__(self):
        self.name = 'GPT4o'
        self.config = dotenv_values(".env")
    
    # def simple_strategy(self, image_path, interest):
    #     prompt1 = f"I am a {interest} lover, and I am scrolling on TikTok to find {interest} videos, based on this screenshot, please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word. "
    #     extracted_text = gpto_image_to_text(prompt1, image_path,self.config)
    #     if(extracted_text == "Exception occurred"):
    #         return "no"
    #     return prompt1, str(extracted_text)
    # def spacial_strategy(self, image_path, interest, cate1, cate2, cate3, cate4, cate5):
    #     prompt1 = f"I am scrolling on TikTok. Based on this screenshot, given 7 catergories: {cate1}, {cate2}, {cate3}, {cate4}, {cate5}, {interest}, other.  Help me decide which category it belongs to. Please answer in a single word."
    #     extracted_text = gpto_image_to_text(prompt1, image_path,self.config)
    #     return str(extracted_text)
    # def ask_general(self, interest):
    #     prompt = f"I am scrolling on TikTok, I am an illiterate person who is interested in {interest}. Can you come up with general visual content related but is not {interest} I would want to watch? Answer short word separated in commas. Your response should only be the answer."
    #     response = gpt_chat(prompt,self.config)
    #     response.replace(".", '')
    #     categories = re.split(r'\s*,\s*', response)
    #     cate1, cate2, cate3, cate4, cate5 = categories[:5]
    #     return cate1, cate2, cate3, cate4, cate4, cate5
    # def plain_strategy(self, image_path):
    #     prompt = "I am scrolling on TikTok, this is a picture of the content.Do you find this content interesting and want to stay? Please include yes or no in your answer, just respond in one word."
    #     extracted_text = gpto_image_to_text(prompt, image_path,self.config)
    #     return prompt, extracted_text
    
    def fundamental_expor(self, image_path):
        prompt1 = "I am scrolling on tiktok and saw this picture. Based on the image, is this content interesting? Help me decide. Please include yes or no in your answer, just respond in one word."
        extracted_text1 = gpto_image_to_text(prompt1, image_path,self.config)
        prompt2 = "Explain briefly"
        extracted_text2 = gpto_reason(prompt1, extracted_text1, prompt2,image_path, self.config )
        prompt3 = "Describe this image in English briefly."
        image_description = gpto_unbiased_discription(prompt3, image_path, self.config)


        print(extracted_text1)
        print(extracted_text2)
        print(image_description)
        return prompt1, extracted_text1, prompt2, extracted_text2, prompt3, image_description
    
    def simple_person_strat(self, image_path, interest):
        prompt1 = f"Based on the image, is this content interesting? Decide yourself based on your personality. Please include yes or no in your answer, just respond in one word."
        extracted_text1 = gpto_persona_decision(interest, prompt1, image_path, self.config)
        if(extracted_text1 == "Exception occurred"):
            return prompt1, "no(exception)", "none", "none"
        prompt2 = f"Explain your decision briefly"
        extracted_text2 = gpto_persona_reason(interest, prompt1,extracted_text1, prompt2, image_path, self.config)
        print(extracted_text1)
        
        print(extracted_text2)
        return prompt1, extracted_text1, prompt2, extracted_text2
    
    def DynamicLP(self, image_path, core, cate1, cate2, cate3, cate4, cate5):
        prompt1 = f"I am scrolling on TikTok. Based on this screenshot, given 7 catergories: {cate1}, {cate2}, {cate3}, {cate4}, {cate5}, {core}, other.  Help me decide which category it belongs to or related to. Please answer in a single word."
        extracted_text = gpto_image_to_text(prompt1, image_path,self.config)
        print(f"extracted text_from functionLP___{extracted_text}")
        return prompt1, str(extracted_text)
    def DPL_ask_cate(self, interest):
        prompt = f"I am scrolling on TikTok, Based on your personality. Can you come up with six general visual content you given your personality might enjoy? Rank it in order. Answer short word separated in commas. Your response should only be the answer."
        response = gpto_peron_chat(interest, prompt,self.config)
        print(response)
        print("split....")
        response.replace(".", '')
        categories = re.split(r'\s*,\s*', response)
        core, cate1, cate2, cate3, cate4, cate5 = categories[:6]
        print("result of asking for the categories should only apear once")
        print(f"{core}, {cate1}, {cate2}, {cate3}, {cate4}, {cate5}")

        return core, cate1, cate2, cate3, cate4, cate5
    
    def new_version_spacial__ask(self, interest):
        prompt = f"I am scrolling on TikTok, Based on your personality. Can you come up with six general visual content you given your personality might enjoy? Rank it in order. Answer short word separated in commas. Your response should only be the answer."
        response = gpto_peron_chat(interest, prompt,self.config)
        print("reponse:")
        print(response)
        return response
    def new_version_experim(self, response, image_path, interest):
        prompt1 = f"Based on the image, is this content interesting? Decide yourself based on your personality keeping in mind your previous reponse. Please include yes or no in your answer, just respond in one word."
        extracted_text1 = gpto_persona_reason(interest, prompt1,response, prompt1, image_path, self.config)
        prompt2 = f"Explain your decision briefly"
        extracted_text2 = gpto_persona_reason(interest, prompt1,extracted_text1, prompt2, image_path, self.config)
        print(extracted_text1)
        
        print(extracted_text2)
        return prompt1, extracted_text1, prompt2, extracted_text2


    


class GPT4:
    def __init__(self):
        self.name = 'GPT4'
        self.config = dotenv_values(".env")

    def simple_strategy(self, image_path, interest):
        prompt1 = f"I am a {interest} lover, and I am scrolling on TikTok to find {interest} videos, based on this screenshot, please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word. "
        extracted_text = gpt_image_to_text(prompt1, image_path,self.config)
        if(extracted_text == "Exception occurred"):
            return "no"
        return prompt1, str(extracted_text)
    def spacial_strategy(self, image_path, interest, cate1, cate2, cate3, cate4, cate5):
        prompt1 = f"I am scrolling on TikTok. Based on this screenshot, given 7 catergories: {cate1}, {cate2}, {cate3}, {cate4}, {cate5}, {interest}, other.  Help me decide which category it belongs to. Please answer in a single word."
        extracted_text = gpt_image_to_text(prompt1, image_path,self.config)
        return str(extracted_text)
    def ask_general(self, interest):
        prompt = f"I am scrolling on TikTok, I am an illiterate person who is interested in {interest}. Can you come up with general visual content related but is not {interest} I would want to watch? Answer short word separated in commas. Your response should only be the answer."
        response = gpt_chat(prompt,self.config)
        response.replace(".", '')
        categories = re.split(r'\s*,\s*', response)
        cate1, cate2, cate3, cate4, cate5 = categories[:5]
        return cate1, cate2, cate3, cate4, cate4, cate5
    def plain_strategy(self, image_path):
        prompt = "I am scrolling on TikTok, this is a picture of the content.Do you find this content interesting and want to stay? Please include yes or no in your answer, just respond in one word."
        extracted_text = gpt_image_to_text(prompt, image_path,self.config)
        return prompt, extracted_text
    
    def fundamental_expor(self, image_path):
        prompt1 = "I am scrolling on tiktok and saw this picture. Baed on the image, is this content interesting? Help me decide. Please include yes or no in your answer, just respond in one word."
        extracted_text1 = gpt_image_to_text(prompt1, image_path,self.config)
        prompt2 = "Explain briefly"
        extracted_text2 = gpt_reason(prompt1, extracted_text1, prompt2,image_path, self.config )
        print(extracted_text1)
        
        print(extracted_text2)
        return prompt1, extracted_text1, prompt2, extracted_text2
    
    def simple_person_strat(self, image_path, interest):
        prompt1 = f"Based on the image, is this content interesting? Decide yourself based on your personality. Please include yes or no in your answer, just respond in one word."
        extracted_text1 = gpt_persona_decision(interest, prompt1, image_path, self.config)
        if(extracted_text1 == "Exception occurred"):
            return prompt1, "no(exception)", "none", "none"
        prompt2 = f"Explain your decision briefly"
        extracted_text2 = gpt_persona_reason(interest, prompt1,extracted_text1, prompt2, image_path, self.config)
        print(extracted_text1)
        
        print(extracted_text2)
        return prompt1, extracted_text1, prompt2, extracted_text2
    
    def DynamicLP(self, image_path, core, cate1, cate2, cate3, cate4, cate5):
        prompt1 = f"I am scrolling on TikTok. Based on this screenshot, given 7 catergories: {cate1}, {cate2}, {cate3}, {cate4}, {cate5}, {core}, other.  Help me decide which category it belongs to or related to. Please answer in a single word."
        extracted_text = gpt_image_to_text(prompt1, image_path,self.config)
        print(f"extracted text_from functionLP___{extracted_text}")
        return prompt1, str(extracted_text)
    def DPL_ask_cate(self, interest):
        prompt = f"I am scrolling on TikTok, Based on your personality. Can you come up with six general visual content you given your personality might enjoy? Rank it in order. Answer short word separated in commas. Your response should only be the answer."
        response = gpt_person_chat_alert(interest, prompt,self.config)
        print(response)
        print("split....")
        response.replace(".", '')
        categories = re.split(r'\s*,\s*', response)
        core, cate1, cate2, cate3, cate4, cate5 = categories[:6]
        print("result of asking for the categories should only apear once")
        print(f"{core}, {cate1}, {cate2}, {cate3}, {cate4}, {cate5}")

        return core, cate1, cate2, cate3, cate4, cate5
    

    

class Llava:
    def __init__(self):
        self.name = 'llava'
    
    def simple_strategy(self, image_path, interest):
        prompt1 = "please Describe this image in a few words in English"
        extracted_text = llava_image_to_text(prompt1, image_path)
        prompt2 = f"""I am a {interest} lover, and I am scrolling on TikTok to find {interest} videos, and this video is about {extracted_text}. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word."""
        response = llava_chat(prompt2)
        return str(response)
    


class Gemini:
    def __init__(self):
        self.name = 'gemini'
        self.config = dotenv_values(".env")
    def simple_strategy(self, image_path, interest):
        prompt1 = f"I am a {interest} lover, and I am scrolling on TikTok to find {interest} videos, based on this screenshot, please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word. "
        extracted_text = gemini_image_to_text(prompt1, image_path,self.config)
        if(extracted_text == "Exception occurred"):
            return "no"
        return prompt1, str(extracted_text)
    def spacial_strategy(self, image_path, interest, cate1, cate2, cate3, cate4, cate5):
        prompt1 = f"I am scrolling on TikTok. Based on this screenshot, given 7 catergories: {cate1}, {cate2}, {cate3}, {cate4}, {cate5}, {interest}, other.  Help me decide which category it belongs to. Please answer in a single word."
        extracted_text = gemini_image_to_text(prompt1, image_path,self.config)
        return str(extracted_text)
    def ask_general(self, interest):
        prompt = f"I am scrolling on TikTok, I am an illiterate person who is interested in {interest}. Can you come up with general visual content related but is not {interest} I would want to watch? Answer short word separated in commas. Your response should only be the answer."
        response = gemini_chat(prompt,self.config)
        response.replace(".", '')
        categories = re.split(r'\s*,\s*', response)
        cate1, cate2, cate3, cate4, cate5 = categories[:5]
        return cate1, cate2, cate3, cate4, cate4, cate5
    def plain_strategy(self, image_path):
        prompt = "I am scrolling on TikTok, this is a picture of the content.Do you find this content interesting and want to stay? Please include yes or no in your answer, just respond in one word."
        extracted_text = gemini_image_to_text(prompt, image_path,self.config)
        return prompt, extracted_text
    
    def fundamental_expor(self, image_path):
        prompt1 = "I am scrolling on tiktok and saw this picture. Is this content interesting? Help me decide.Please include yes or no in your answer, just respond in one word."
        extracted_text1 = gemini_image_to_text(prompt1, image_path,self.config)
        if ("yes" in extracted_text1.lower()):
            att = "interesting"
        else:
            att = "uninteresting"

        prompt2 = f"What is the thing that makes this picture {att}?"
        extracted_text2 = gemini_image_to_text(prompt2, image_path, self.config )
        print(extracted_text1)
        
        print(extracted_text2)
        return prompt1, extracted_text1, prompt2, extracted_text2
    
    def simple_person_strat(self, image_path, interest):
        prompt1 = f"Based on the image, is this content interesting? Decide yourself based on your personality. Please include yes or no in your answer, just respond in one word."
        extracted_text1 = gemini_person_decision(interest, prompt1, image_path, self.config)
        if(extracted_text1 == "Exception occurred"):
            return prompt1, "no(exception)", "none", "none"
        elif ("yes" in extracted_text1.lower()):
            att = "interesting"
        else:
            att = "uninteresting"

        prompt2 = f"What is the thing that makes this picture {att} based on your personality?"
        extracted_text2 = gemini_person_decision(interest, prompt2, image_path, self.config)
        print(extracted_text1)
        print(prompt2)
        
        print(extracted_text2)
        return prompt1, extracted_text1, prompt2, extracted_text2


    