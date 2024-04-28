import md_classes
import pl_classes

from pl_classes import TikTok, Youtube, Snap, Instagram
from md_classes import Llava, Gemini, GPT4
import time
import pyautogui
import os
import csv

class Bot:
    def __init__(self, interest, platform, model, time1):
        self.interest = interest
        self.platform = platform  # Assuming TikTok class is defined elsewhere
        self.model = model      # Model object with a simple_strategy method
        self.time1 = time1

    def open_platform(self):
        self.platform.open_and_position_browser()

    def save_to_csv(self, image_name, prompt, stay_duration):
        csv_file = 'experiment_data.csv'
        print("Saving to CSV:", os.path.abspath(csv_file))
        fieldnames = ['Image Name', 'Prompt', 'User Interest', 'Stay Duration', 'Platform', 'Model Name']
        file_exists = os.path.isfile(csv_file)
        
        with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader() 
            
            writer.writerow({
                'Image Name': image_name,
                'Prompt': prompt,
                'User Interest': str(self.interest),
                'Stay Duration': stay_duration,
                'Platform': str(self.platform.name),
                'Model Name':str(self.model.name)
            })


    def experiment(self, n):
        self.open_platform()
        for i in range(n):
            screen_shot_name = pl_classes.take_screen_shot(self.platform)
            print(f"{i}th loop, captured {i + 1} picture")
            
            prompt, decision = self.model.simple_strategy(screen_shot_name, self.interest)
            stay_duration = 0
            if "yes" in decision.lower():
                stay_duration = self.time1 if decision else 0
                print(f'{self.model.name} decides to stay on this content...\n')
                time.sleep(self.time1)
            else:
                print(f'Scrolling down to new content...')
            self.save_to_csv(screen_shot_name, prompt, stay_duration)
            pyautogui.press('down')
            time.sleep(1)

    @staticmethod
    def run_experiment(interest, platform, model, n, time1):
        bot = Bot(interest,platform, model, time1)
        bot.experiment(n)

class Spatial_Bot:
    def __init__(self, interest, platform, model):
        self.interest = interest
        self.platform = platform  # Assuming TikTok class is defined elsewhere
        self.model = model      # Model object with a simple_strategy method

    def open_platform(self):
        self.platform.open_and_position_browser()

    def experiment(self, n):
        success = 0
        self.open_platform()
        categories = set(self.model.ask_general(self.interest))
        
        for i in range(n):
            screen_shot_name = pl_classes.take_screen_shot(self.platform)
            print(f"{i+1}'th loop, taken {i+1} picture")
            category = self.model.spacial_strategy(screen_shot_name, self.interest, *categories)

            if any(cat.lower() in category.lower() for cat in categories):
                print(f"{category} presented, stay for 10s")
                time.sleep(10)
                pyautogui.press('down')
                time.sleep(1)
                if i >= 10:
                    success_rate = success / (i + 1)
                    if success_rate > 0.3:
                        print(f"{category} presented, stay for 5s")
                        time.sleep(5)
                    if success_rate > 0.5:
                        pyautogui.press('down')
                        time.sleep(1)
                    else:
                        print(f"{category} presented, stay for 10s")
                        time.sleep(10)
                        pyautogui.press('down')
                        time.sleep(1)
            elif self.interest.lower() in category.lower():                           
                print(f"{category} presented, stay for 30s")
                time.sleep(30)
                pyautogui.press("down")
                time.sleep(1)
                success += 1
            else:
                pyautogui.press("down")
                time.sleep(1)

        
    def run_experiment(interest, platform, model, n):
        bot = Spatial_Bot(interest,platform, model)
        bot.experiment(n)
# class Spacial_Bot:
#     def __init__(self, interest, platform, model):
#         self.interest = interest
#         self.platform = platform  # Assuming TikTok class is defined elsewhere
#         self.model = model      # Model object with a simple_strategy method

#     def open_platform(self):
#         self.platform.open_and_position_browser()

#     def experiment(self, n):
#         success = 0
#         self.open_platform()
#         cate1, cate2, cate3, cate4, cate4, cate5 = self.platform.ask_general()
#         categories = [cate1, cate2, cate3, cate4, cate5]
#         for i in range(n):
#             if i<10:
#                 screen_shot_name = pl_classes.take_screen_shot(self.platform)
#                 print(f"{i}'th loop, taken {i+1} picture")
#                 category = self.model.spacial_strategy(screen_shot_name, self.interest, cate1, cate2, cate3, cate4, cate4, cate5)
#                 if any(cat.lower() in category.lower() for cat in categories):
#                     print(f"{category} presented, stay for 10s")
#                     time.sleep(10)
#                     pyautogui.press('down')
#                     time.sleep(1.5)
#                 elif self.interest in category.lower():                           
#                     print(f"{category} presented, stay for 30s")
#                     time.sleep(30)
#                     pyautogui.press("down")
#                     time.sleep(1.5)
#                     success+=1
#                 else:
#                     pyautogui.press("down")
#                     time.sleep(1.5)
#             else:
#                 screen_shot_name = pl_classes.take_screen_shot(tiktok)
#                 print(f"{i}'th loop, taken {i+1} picture")
#                 category = self.model.spacial_strategy(screen_shot_name, self.interest, cate1, cate2, cate3, cate4, cate4, cate5)
#                 if any(cat.lower() in category.lower() for cat in categories):
#                     success_rate = success/i
#                     if success_rate > 0.3:
#                             print(f"{category} presented, stay for 5s")
#                             time.sleep(5)
#                             pyautogui.press('down')
#                             time.sleep(1.5)
#                     if success_rate >0.5:
#                             pyautogui.press('down')
#                             time.sleep(1.5)
#                     else:
#                             print(f"{category} presented, stay for 10s")
#                             time.sleep(10)
#                             pyautogui.press('down')
#                             time.sleep(1.5)
                    
#                 elif self.interest in category.lower():
#                     print(f"{category} presented, stay for 30s")
#                     time.sleep(30)
#                     pyautogui.press("down")
#                     time.sleep(1.5)
#                     success+=1
#                 else:
#                     pyautogui.press("down")
#                     time.sleep(1.5)
            