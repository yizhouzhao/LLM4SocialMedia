# Import the pl_classes module
import pl_classes
import pyautogui
import time


########抖音########
# tiktok = pl_classes.TikTok()
# tiktok.open_and_position_browser()

#######snap########
# snap = pl_classes.Snap()
# snap.open_and_position_browser()

#####油管##########
# youtube = pl_classes.Youtube()
# youtube.open_and_position_chrome_window()

######INS#########
# instagram = pl_classes.instagram()
# instagram.open_and_position_browser()


import md_classes
# interest = "Pet"
# tiktok = pl_classes.TikTok()
# tiktok.open_and_position_browser()
# gemini = md_classes.Gemini()

# for i in range(3):
#     screen_shot_name = pl_classes.take_screen_shot(tiktok)
#     print(f"{i}'th loop, taken {i+1} picture")
#     ans = gemini.simple_strategy(screen_shot_name, interest)
#     if "yes" in ans.lower():
#             print(f'{gemini.name} decide to stay......\n')
#             time.sleep(30)
#             pyautogui.press('down')
#             time.sleep(1.5)
#     else:
#         pyautogui.press('down')
#         time.sleep(1.5)

success = 0
interest = "Pet"
tiktok = pl_classes.TikTok()
tiktok.open_and_position_browser()
gemini = md_classes.Gemini()
cate1, cate2, cate3, cate4, cate4, cate5 = gemini.ask_general()
categories = [cate1, cate2, cate3, cate4, cate5]
for i in range(10):
    screen_shot_name = pl_classes.take_screen_shot(tiktok)
    print(f"{i}'th loop, taken {i+1} picture")
    category = gemini.spacial_strategy(screen_shot_name, interest, cate1, cate2, cate3, cate4, cate4, cate5)
    if any(cat.lower() in category.lower() for cat in categories):
         print(f"{category} presented, stay for 10s")
         time.sleep(10)
         pyautogui.press('down')
         time.sleep(1.5)
    elif interest in category.lower():
         print(f"{category} presented, stay for 30s")
         time.sleep(30)
         pyautogui.press("down")
         time.sleep(1.5)
         success+=1
    else:
         pyautogui.press("down")
         time.sleep(1.5)

for i in range(10, 30):
    screen_shot_name = pl_classes.take_screen_shot(tiktok)
    print(f"{i}'th loop, taken {i+1} picture")
    category = gemini.spacial_strategy(screen_shot_name, interest, cate1, cate2, cate3, cate4, cate4, cate5)
    if any(cat.lower() in category.lower() for cat in categories):
         success_rate = success/i
         if success_rate > 0.3:
            print(f"{category} presented, stay for 5s")
            time.sleep(5)
            pyautogui.press('down')
            time.sleep(1.5)
         if success_rate >0.5:
             pyautogui.press('down')
             time.sleep(1.5)
         else:
            print(f"{category} presented, stay for 10s")
            time.sleep(10)
            pyautogui.press('down')
            time.sleep(1.5)
         
    elif interest in category.lower():
         print(f"{category} presented, stay for 30s")
         time.sleep(30)
         pyautogui.press("down")
         time.sleep(1.5)
         success+=1
    else:
         pyautogui.press("down")
         time.sleep(1.5)

for i in range(n):
     if i<10:
          screen_shot_name = pl_classes.take_screen_shot(tiktok)
          print(f"{i}'th loop, taken {i+1} picture")
          category = gemini.spacial_strategy(screen_shot_name, interest, cate1, cate2, cate3, cate4, cate4, cate5)
          if any(cat.lower() in category.lower() for cat in categories):
               print(f"{category} presented, stay for 10s")
               time.sleep(10)
               pyautogui.press('down')
               time.sleep(1.5)
          elif interest in category.lower():                           
               print(f"{category} presented, stay for 30s")
               time.sleep(30)
               pyautogui.press("down")
               time.sleep(1.5)
               success+=1
          else:
               pyautogui.press("down")
               time.sleep(1.5)
     else:
          screen_shot_name = pl_classes.take_screen_shot(tiktok)
          print(f"{i}'th loop, taken {i+1} picture")
          category = gemini.spacial_strategy(screen_shot_name, interest, cate1, cate2, cate3, cate4, cate4, cate5)
          if any(cat.lower() in category.lower() for cat in categories):
               success_rate = success/i
               if success_rate > 0.3:
                    print(f"{category} presented, stay for 5s")
                    time.sleep(5)
                    pyautogui.press('down')
                    time.sleep(1.5)
               if success_rate >0.5:
                    pyautogui.press('down')
                    time.sleep(1.5)
               else:
                    print(f"{category} presented, stay for 10s")
                    time.sleep(10)
                    pyautogui.press('down')
                    time.sleep(1.5)
               
          elif interest in category.lower():
               print(f"{category} presented, stay for 30s")
               time.sleep(30)
               pyautogui.press("down")
               time.sleep(1.5)
               success+=1
          else:
               pyautogui.press("down")
               time.sleep(1.5)
    