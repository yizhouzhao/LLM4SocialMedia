import base64
import requests
import pyautogui
import cv2
import numpy as np
import time

def converter(image_path):
    with open(image_path, "rb") as image_file:
        base64_data = base64.b64encode(image_file.read()).decode('utf-8')
        formatted_data = f"data:image/png;base64,{base64_data}"
    return formatted_data

def Use_VQA(VQA, png):
    right_format = converter(png)
    response = requests.post(VQA, json={
        "data": [
            right_format,
            "Is there a cat in the picture?",
        ]
    }).json()
    answer = response["data"][0]

    return answer

def left_screen_shot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    height, width, _ = image.shape
    # Calculate the midpoint to split the image into left and right halves
    midpoint = width // 2
    left_half = image[:, :midpoint]
    # Save the left half as a new PNG file
    cv2.imwrite("left_half.png", left_half)

VQA_url = "https://ofa-sys-ofa-vqa.hf.space/run/predict"
left_screen_shot()
image_path = "left_half.png"
answer = Use_VQA(VQA_url, image_path)

pyautogui.moveTo(455,419)

pyautogui.click()

i=0

for i in range(0,100):
    left_screen_shot()
    image_path = "left_half.png"
    answer = Use_VQA(VQA_url, image_path)
    if "yes" in answer.lower():
        print('6666')
        time.sleep(30)
        pyautogui.press('down')
    else:
        pyautogui.press('down')
    i=i+1


