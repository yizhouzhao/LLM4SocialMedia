import base64
import requests

CONTEXT = "You are LLaVA, a large language and vision assistant trained by UW Madison WAIV Lab. You are able to understand the visual content that the user provides, and assist the user with a variety of tasks using natural language. Follow the instructions carefully and explain your answers in detail.### Human: Hi!### Assistant: Hi there! How can I help you today?\n"

with open('extreme_ironing.png', 'rb') as f:
    img_str = base64.b64encode(f.read()).decode('utf-8')
    prompt = CONTEXT + f'### Human: Please describe the image?: \n<img src="data:image/png;base64,{img_str}">### Assistant: '
    print(requests.post('http://35.92.201.55:5000/v1/completions', json={'prompt': prompt, 'max_tokens': 200, 'stop': ['\n###']}).json())

# with open('ring.jpg', 'rb') as f:
#     img_str = base64.b64encode(f.read()).decode('utf-8')
#     prompt = CONTEXT + f'### Human: What is flower on the ring?: \n<img src="data:image/jpeg;base64,{img_str}">### Assistant: '
#     print(requests.post('http://35.92.201.55:5000/api/v1/completions', json={'prompt': prompt, 'stopping_strings': ['\n###']}).json())