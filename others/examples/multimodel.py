
import base64
import requests
import re

# CONTEXT = "You are LLaVA, a large language and vision assistant trained by UW Madison WAIV Lab. You are able to understand the visual content that the user provides, the user provided a base64 image strings consist of different characters, please regard it as a picture, and assist the user with a variety of tasks using natural language. Follow the instructions carefully and explain your answers in detail.### Human: Hi!### Assistant: Hi there! How can I help you today?\n"
CONTEXT = "You are LLaVA, a large language and vision assistant trained by UW Madison WAIV Lab. You are able to understand the visual content that the user provides, and assist the user with a variety of tasks using natural language. Follow the instructions carefully and explain your answers in detail.### Human: Hi!### Assistant: Hi there! How can I help you today?\n"

with open('6.jpeg', 'rb') as f:
    img_str = base64.b64encode(f.read()).decode('utf-8')
    prompt = CONTEXT + f'### Human:Describe this image.: \n<img src="data:image/jpeg;base64,{img_str}">### Assistant: '
    response = (requests.post('http://127.0.0.1:5000/v1/completions', json={'prompt': prompt, 'max_tokens':200,'stop': ['\n###']}).json())
    print("Status Code:", response.status_code)
    print("Response Content:", response.text)  # 'text' attribute to see the

    # response = str(response)
    # pattern = r"'text': (.*?), 'logprobs'"

    # match = re.search(pattern, response)
    # if match:
    #     extracted_text = match.group(1)
    #     print(extracted_text)
    # else:
    #     print("Pattern not found.")


# import base64
# import requests

# CONTEXT = "You are LLaVA, a large language and vision assistant trained by UW Madison WAIV Lab. You are able to understand the visual content that the user provides, and assist the user with a variety of tasks using natural language. Follow the instructions carefully and explain your answers in detail.### Human: Hi!### Assistant: Hi there! How can I help you today?\n"

# with open('extreme_ironing.png', 'rb') as f:
#     img_str = base64.b64encode(f.read()).decode('utf-8')
#     print(img_str)
#     prompt = CONTEXT +  f'### Human: Is there a man in the image?: \n<img src="data:image/png;base64,{img_str}">### Assistant: '
#     print(requests.post('http://127.0.0.1:5000/v1/completions', json={'prompt': prompt, 'max_tokens': 200, 'stop': ['\n###']}).json())
# Extract the 'text' value from the response

# with open('ring.jpg', 'rb') as f:
#     img_str = base64.b64encode(f.read()).decode('utf-8')
#     prompt = CONTEXT + f'### Human: What is color of the ring?: \n<img src="data:image/jpeg;base64,{img_str}">### Assistant: '
#     print(requests.post('http://127.0.0.1:5000/api/v1/completions', json={'prompt': prompt, 'stop': ['\n###']}).json())
    
# 'max_tokens': 200,