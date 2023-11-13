import base64
import requests

CONTEXT = "You are LLaVA, a large language and vision assistant trained by UW Madison WAIV Lab. You are able to understand the visual content that the user provides, and assist the user with a variety of tasks using natural language. Follow the instructions carefully and explain your answers in detail.### Human: Hi!### Assistant: Hi there! How can I help you today?\n"

with open('extreme_ironing.png', 'rb') as f:
    img_str = base64.b64encode(f.read()).decode('utf-8')
    prompt = CONTEXT + f'### Human: What is unusual about this image: \n<img src="data:image/jpeg;base64,{img_str}">### Assistant: '
    print(requests.post('http://127.0.0.1:5000/api/v1/generate', json={'prompt': prompt, 'stopping_strings': ['\n###']}).json())