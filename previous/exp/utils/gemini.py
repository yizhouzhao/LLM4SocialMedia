import google.generativeai as genai
from dotenv import dotenv_values
config = dotenv_values(".env")
print("-----------------[gemini] config", config)
genai.configure(api_key=config["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-pro')
model_vision = genai.GenerativeModel('gemini-pro-vision')

