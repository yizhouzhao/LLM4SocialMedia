import md_classes
import pl_classes

from pl_classes import TikTok, Youtube, Snap, Instagram
from md_classes import Llava, Gemini, GPT4, GPT4o
import time
import pyautogui
import os
import csv
import datetime






def save_to_csv(self, image_name, prompt, stay_duration):
        csv_file = 'experiment_data_plain_gpt4o_youtube.csv'
        print("Saving to CSV:", os.path.abspath(csv_file))
        fieldnames = ['Image Name', 'Prompt', 'User Interest', 'Stay Duration', 'Platform', 'Model Name']
        file_exists = os.path.isfile(csv_file)
        current_time = str(datetime.datetime.now().time())[:-7]
        with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader() 
            
            writer.writerow({
                'Image Name': image_name+current_time,
                'Prompt': prompt,
                'User Interest': str(self.interest),
                'Stay Duration': stay_duration,
                'Platform': str(self.platform.name),
                'Model Name':str(self.model.name)
            })

def save_to_csv_plain(self, image_name, prompt1, extracted_text1, prompt2, extracted_text2, stay_duration, prompt3, image_description):
        csv_file = 'experiment_data_plain_gpt_tiktok1.csv'
        print("Saving to CSV:", os.path.abspath(csv_file))
        fieldnames = ['Image Name', 'Prompt',"Answer","Reason","Image Description", 'Stay Duration', 'Platform', 'Model Name']
        file_exists = os.path.isfile(csv_file)
        current_time = str(datetime.datetime.now().time())[:-7]
        with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader() 
            
            writer.writerow({
                'Image Name': image_name+current_time,
                'Prompt': prompt1+prompt2+prompt3,
                'Answer': extracted_text1,
                "Reason":extracted_text2,
                "Image Description": image_description,
                'Stay Duration': stay_duration,
                'Platform': str(self.platform.name),
                'Model Name':str(self.model.name)
            })


def save_to_csv_simple(self, image_name,prompt1, extracted_text1, prompt2, extracted_text2, stay_duration):
        csv_file = f'experiment_data_simple_{self.model.name}_{self.platform.name}11.csv'
        print("Saving to CSV:", os.path.abspath(csv_file))
        fieldnames = ['Image Name', 'Persona', 'Prompt',"Answer","Reason", 'Stay Duration', 'Platform', 'Model Name']
        file_exists = os.path.isfile(csv_file)
        current_time = str(datetime.datetime.now().time())[:-7]
        with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader() 
            
            writer.writerow({
                'Image Name': image_name+current_time,   
                'Persona': str(self.interest),
                'Prompt': prompt1+prompt2,
                'Answer': extracted_text1,
                "Reason":extracted_text2,
                'Stay Duration': stay_duration,
                'Platform': str(self.platform.name),
                'Model Name':str(self.model.name)
            })


def save_to_csv_spacial(self, image_name,prompt, category, stay_duration):
        csv_file = f'experiment_data_spacial_{self.model.name}_{self.platform.name}_test.csv'
        print("Saving to CSV:", os.path.abspath(csv_file))
        fieldnames = ['Image Name', 'Persona', 'Prompt',"Category", 'Stay Duration', 'Platform', 'Model Name']
        file_exists = os.path.isfile(csv_file)
        current_time = str(datetime.datetime.now().time())[:-7]
        with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader() 
            
            writer.writerow({
                'Image Name': image_name+current_time,   
                'Persona': str(self.interest),
                'Prompt': prompt,
                'Category': category,
                'Stay Duration': stay_duration,
                'Platform': str(self.platform.name),
                'Model Name':str(self.model.name)
            })

def save_to_csv_spacial_eval(self, image_name,prompt, category,type):
        csv_file = f'experiment_data_spacial_{self.model.name}_{self.platform.name}_evaltest.csv'
        print("Saving to CSV:", os.path.abspath(csv_file))
        fieldnames = ['Image Name', 'Persona', 'Prompt',"Category", 'Type', 'Platform', 'Model Name']
        file_exists = os.path.isfile(csv_file)
        current_time = str(datetime.datetime.now().time())[:-7]
        with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader() 
            
            writer.writerow({
                'Image Name': image_name+current_time,   
                'Persona': str(self.interest),
                'Prompt': prompt,
                'Category': category,
                'Type': type,
                'Platform': str(self.platform.name),
                'Model Name':str(self.model.name)
            })



class Plain_bot:
    def __init__(self, platform, model, time):
        self.platform = platform
        self.model = model
        self.time = time 
        self.t = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.interest = "None"
    def open_platform(self):
        self.platform.open_and_position_browser()
    def experiment(self, n):
        self.open_platform()
        for i in range(n):
            screen_shot_name = pl_classes.take_screen_shot(self.platform, self.t)
            print(f"{i}th loop, captured {i + 1} picture")
            
            prompt1, extracted_text1, prompt2, extracted_text2, prompt3, image_description = self.model.fundamental_expor(screen_shot_name)
            stay_duration = 0
            if "yes" in extracted_text1.lower():
                stay_duration = self.time if extracted_text1 else 0
                print(f'{self.model.name} decides to stay on this content...\n')
                time.sleep(self.time)
            else:
                print(f'Scrolling down to new content...')
            save_to_csv_plain(self, screen_shot_name[45:], prompt1, extracted_text1, prompt2, extracted_text2, stay_duration, prompt3, image_description)
            pyautogui.press('down')
            time.sleep(1)

    @staticmethod
    def run_experiment(platform, model, n, time):
        bot = Plain_bot(platform, model, time)
        bot.experiment(n)

    
    




class Simple_Bot:
    def __init__(self, interest, platform, model, time1):
        self.interest = interest
        self.platform = platform  # Assuming TikTok class is defined elsewhere
        self.model = model      # Model object with a simple_strategy method
        self.time1 = time1
        self.t = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    def open_platform(self):
        self.platform.open_and_position_browser()


    def experiment(self, n):
        self.open_platform()
        for i in range(n):
            screen_shot_name = pl_classes.take_screen_shot(self.platform,self.t)
            print(f"{i}th loop, captured {i + 1} picture")
            
            prompt1, extracted_text1, prompt2, extracted_text2 = self.model.simple_person_strat(image_path = screen_shot_name, interest = self.interest)
            stay_duration = 0
            if "yes" in extracted_text1.lower():
                stay_duration = self.time1 if extracted_text1 else 0
                print(f'{self.model.name} decides to stay on this content...\n')
                time.sleep(self.time1)
            else:
                print(f'Scrolling down to new content...')
            save_to_csv_simple(self, screen_shot_name[45:], prompt1, extracted_text1, prompt2, extracted_text2,  stay_duration)
            pyautogui.press('down')
            time.sleep(1)

    @staticmethod
    def run_experiment(interest, platform, model, n, time1):
        bot = Simple_Bot(interest,platform, model, time1)
        bot.experiment(n)


class Spatial_Bot:
    def __init__(self, interest, platform, model):
        self.interest = interest
        self.platform = platform  # Assuming TikTok class is defined elsewhere
        self.model = model      # Model object with a simple_strategy method
        self.t  = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.cates = ""
        self.core = ''
    def open_platform(self):
        self.platform.open_and_position_browser()

    def experiment(self, n):
        success = 0
        self.open_platform()
        categories = list(self.model.DPL_ask_cate(self.interest))  # Convert the set to a list
       
        core = categories[0]  # Get the first element
        self.core = core
        categories.pop(0)  # Remove the first element from the list
        self.cates = categories
        print()

        
        
        for i in range(n):
            screen_shot_name = pl_classes.take_screen_shot(self.platform, self.t)
            print(f"{i+1}'th loop, taken {i+1} picture")
            prompt, category = self.model.DynamicLP(screen_shot_name, core, *categories)
            

            if any(cat.lower() in category.lower() or category.lower() in cat.lower() for cat in categories):
                if i >= 10:
                    success_rate = success / (i + 1)
                    if success_rate > 0.3:
                        print(f"{category} presented, stay for 5s")
                        time.sleep(5)
                        stay_duration = 5
                    if success_rate > 0.5:
                        print(f"{category} presented, but I dont want to stay")
                        stay_duration = 0
                    else:
                        print(f"{category} presented, stay for 10s")
                        time.sleep(10)
                        stay_duration = 10
                else:
                    print(f"{category} presented, stay for 10s")
                    time.sleep(10)
                    stay_duration = 10
            elif core.lower() in category.lower() or category.lower() in core.lower():                           
                print(f"{category} presented, stay for 30s")
                time.sleep(30)
                stay_duration = 30
                success += 1
            else:
                print("scrolling down to next content....")
                stay_duration = 0
            save_to_csv_spacial(self, screen_shot_name[45:], prompt, category,  stay_duration)
            pyautogui.press('down')
            time.sleep(1)
        
    def run_experiment(interest, platform, model, training_number, evaluating_number):
        bot = Spatial_Bot(interest,platform, model)
        bot.experiment(training_number)
        boteval = Spatial_Bot_eval(interest,platform, model, bot.cates, bot.core)
        boteval.experiment(evaluating_number)
    def run_experiment_with_additional_eval(interest, platform, model, model_for_eval= GPT4o(), training_number= 100, evaluating_number=50, additional_evaluation = 50):
        bot = Spatial_Bot(interest,platform, model)
        bot.experiment(training_number)
        boteval = Spatial_Bot_eval(interest,platform, model, bot.cates, bot.core)
        boteval.experiment(evaluating_number)
        boteval2 = Spatial_Bot_eval(interest,platform, model_for_eval, bot.cates, bot.core)
        boteval2.experiment(additional_evaluation)

class Spatial_Bot_eval:
    def __init__(self, interest, platform, model, cates, core):
        self.interest = interest
        self.platform = platform  # Assuming TikTok class is defined elsewhere
        self.model = model      # Model object with a simple_strategy method
        self.t  = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.cates = cates
        self.core = core
    def open_platform(self):
        self.platform.open_and_position_browser()

    def experiment(self, n):
        self.open_platform()
        categories = self.cates  # Convert the set to a list
        core = self.core

        
        
        for i in range(n):
            screen_shot_name = pl_classes.take_screen_shot(self.platform, self.t)
            print(f"{i+1}'th loop, taken {i+1} picture")
            prompt, category = self.model.DynamicLP(screen_shot_name, core, *categories)
            

            # if any(cat.lower() in category.lower() for cat in categories):
            if any(cat.lower() in category.lower() or category.lower() in cat.lower() for cat in categories):
                print(f"{category} presented")
                kind  = "general"
            elif core.lower() in category.lower() or category.lower() in core.lower():                           
                print(f"{category} presented")
                kind = "core"
            else:
                print("scrolling down to next content....")
                kind = "other"
            save_to_csv_spacial_eval(self, screen_shot_name[45:], prompt, category, kind)
            pyautogui.press('down')
            time.sleep(1)
        
    def run_experiment(interest, platform, model, n):
        bot = Spatial_Bot_eval(interest,platform, model)
        bot.experiment(n)

class New_spacial_bot:
    def __init__(self, interest, platform, model, time1):
        self.interest = interest
        self.platform = platform  # Assuming TikTok class is defined elsewhere
        self.model = model      # Model object with a simple_strategy method
        self.t  = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.time1 = time1
    def open_platform(self):
        self.platform.open_and_position_browser()

    def experiment(self, n):
        self.open_platform()
        response = self.model.new_version_spacial__ask(self.interest) # Convert the set to a list


        for i in range(n):
            screen_shot_name = pl_classes.take_screen_shot(self.platform, self.t)
            print(f"{i+1}'th loop, taken {i+1} picture")
            prompt1, extracted_text1, prompt2, extracted_text2 = self.model.new_version_experim(response, screen_shot_name, self.interest)
            stay_duration = 0
            if "yes" in extracted_text1.lower():
                stay_duration = self.time1 if extracted_text1 else 0
                print(f'{self.model.name} decides to stay on this content...\n')
                time.sleep(self.time1)
            else:
                print(f'Scrolling down to new content...')
            save_to_csv_simple(self, screen_shot_name[45:], prompt1, extracted_text1, prompt2, extracted_text2,  stay_duration)
            pyautogui.press('down')
            time.sleep(1)

    @staticmethod
    def run_experiment(interest, platform, model, n, time1):
        bot = New_spacial_bot(interest,platform, model, time1)
        bot.experiment(n)