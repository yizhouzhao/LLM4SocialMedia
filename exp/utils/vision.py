import pyautogui
from PIL import Image

from paddleocr import PaddleOCR
ocr = PaddleOCR(use_gpu=True) # use_angle_cls=True, lang='en'

def capture_and_crop(x1, y1, x2, y2):
    '''
    Capture the screen and crop the image using PIL
    '''
    # Capture the entire screen
    screenshot = pyautogui.screenshot()

    # Crop the screenshot using PIL
    cropped_image = screenshot.crop((x1, y1, x2, y2))

    return cropped_image