# Import the pl_classes module
import pl_classes
import pyautogui
import time


########抖音########
tiktok = pl_classes.TikTok()
tiktok.open_and_position_browser()

#######snap########
# snap = pl_classes.Snap()
# snap.open_and_position_browser()

#####油管##########
# youtube = pl_classes.Youtube()
# youtube.open_and_position_chrome_window()

######INS#########
# instagram = pl_classes.instagram()
# instagram.open_and_position_browser()

# screen_shot_name = pl_classes.take_screen_shot(instagram)


# try:
#     while True:
#         x, y = pyautogui.position()
    
#         print(f"X: {x}, Y: {y}", end='\r')
#         time.sleep(0.1)
# except KeyboardInterrupt:
#     print("\nDone")

