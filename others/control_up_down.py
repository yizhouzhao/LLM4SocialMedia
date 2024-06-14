import pyautogui
import time

pyautogui.moveTo(455,419)

pyautogui.click()

i=0

for i in range(0,3):
    time.sleep(3)
    pyautogui.press('down')
    i=i+1