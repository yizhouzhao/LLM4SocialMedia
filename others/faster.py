from transformers import ViltProcessor, ViltForQuestionAnswering
import pyautogui
from PIL import Image
import cv2
import numpy as np
import time
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

def left_screen_shot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    height, width, _ = image.shape
    # Calculate the midpoint to split the image into left and right halves
    midpoint = width // 2
    left_half = image[:, :midpoint]
    # Save the left half as a new PNG file
    cv2.imwrite("left_half_test.png", left_half)


def predict_answer(image_path, question):
    # Open the image using PIL
    image = Image.open(image_path)

    # Load VQA model
    processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

    # Prepare inputs
    encoding = processor(image, question, return_tensors="pt")

    # Forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()

    # Return the predicted answer
    return model.config.id2label[idx]


# Example usage:
image_path = "left_half_test.png"
question = "Is there a cat in the image?"

pyautogui.moveTo(455,419)

pyautogui.click()
# Perform actions based on the answer
for i in range(0,100):
    left_screen_shot()
    image_path = "left_half_test.png"
    predicted_answer = predict_answer(image_path, question)
    if "yes" in predicted_answer.lower():
        print('6666')
        time.sleep(10)
        pyautogui.press('down')
    else:
        pyautogui.press('down')
