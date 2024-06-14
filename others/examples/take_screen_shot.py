import base64
import requests
import re
import numpy as np
import pyautogui
import cv2
import time
from PIL import Image
# import subprocess
import requests
from sklearn.metrics import precision_score, recall_score, f1_score



def convert_png_to_jpeg(input_path, output_path, quality=75):
    # Open the PNG image
    png_image = Image.open(input_path)

    # Convert to RGB and save as JPEG
    png_image.convert('RGB').save(output_path, 'JPEG', quality=quality)


def left_screen_shot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    height, width, _ = image.shape
    # Calculate the midpoint to split the image into left and right halves
    midpoint = width // 2
    left_half = image[:, :midpoint]
    # Save the left half as a new PNG file
    cv2.imwrite("left_half.png", left_half)

def retrive_answer(Img):

    CONTEXT = "You are LLaVA, a large language and vision assistant trained by UW Madison WAIV Lab. You are able to understand the visual content that the user provides, the user provided a base64 image strings consist of different characters, please regard it as a picture, and assist the user with a variety of tasks using natural language. Follow the instructions carefully and explain your answers in detail.### Human: Hi!### Assistant: Hi there! How can I help you today?\n"

    with open(Img, 'rb') as f:
        
        img_str = base64.b64encode(f.read()).decode('utf-8')
        prompt = CONTEXT + f'### Human: Please first give the answer there is a cat inside the image or not and then describe the image.: \n<img src="data:image/jpeg;base64,{img_str}">### Assistant: '
        response = (requests.post('http://127.0.0.1:5000/v1/completions', json={'prompt': prompt, 'max_tokens':200, 'stop': ['\n###']}).json())
        # print(response)2002
        # print('\n')
        response = str(response)
        pattern = r"'text': (.*?), 'logprobs'"

        match = re.search(pattern, response)
        if match:
            extracted_text = match.group(1)
            print(extracted_text)
    return extracted_text

import requests
def evaluate(predictions, labels):
    precision = precision_score(labels, predictions)
    recall = recall_score(labels, predictions)
    f1 = f1_score(labels, predictions)

    return precision, recall, f1

url = "http://127.0.0.1:5000/v1/chat/completions"
pyautogui.moveTo(455,419)

pyautogui.click()

headers = {
    "Content-Type": "application/json"
}

history = []
label = 0
predictions = []
i = 0

while i < 10:
    left_screen_shot()

    convert_png_to_jpeg('left_half.png', 'left_half.jpeg', quality=75)

    extracted_text = retrive_answer('left_half.jpeg')
    user_message = f"I am a cat lover, and I am scrolling on tik_tok to find cat videos, and this video is about {extracted_text}, If video includes cat, I will stay at this video otherwise will not stay. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word."
    print(user_message)
    history.append({"role": "user", "content": user_message})

    data = {
        "mode": "chat",
        #"character": "Example",
        "messages": history
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    assistant_message = response.json()['choices'][0]['message']['content']
    history.append({"role": "assistant", "content": assistant_message})
    print(assistant_message)

    if "yes" in assistant_message.lower():
        label = 1
    else:
        label = 0

    predictions.append(label)
    
    if label == 1:
        print('sleeping... #######                                          18%')
        time.sleep(10)
        pyautogui.press('down')
        time.sleep(0.5)
    else:
        pyautogui.press('down')
        time.sleep(0.5)

    i = i + 1

print(predictions)
labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # Assuming your actual labels
precision, recall, f1 = evaluate(predictions, labels)
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")