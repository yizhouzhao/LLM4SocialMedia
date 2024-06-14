import pyautogui
from PIL import Image
import numpy as np

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

def capture_time_stamp(x1, y1, x2, y2):
    '''
    Capture the screen and crop the image using PIL
    '''
    # Crop the screenshot using PIL
    cropped_image = capture_and_crop(x1, y1, x2, y2)

    cropped_image.show()

    # img_path = os.path.join(OUTPUT_FOLDER, "capture0.png")
    result = ocr.ocr(np.array(cropped_image), cls=True)
    result = result[0]

    if result:
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]

        return txts

    else:
        return None