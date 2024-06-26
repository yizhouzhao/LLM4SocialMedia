import webbrowser
import time
import win32gui
import win32con
import subprocess
import pyautogui
import os
import datetime

def open_and_position_chrome_window(url):
    # Path to Chrome executable
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    # Profile directory
    profile_directory = 'Profile 6'

    # Construct the command with the profile
    command = f'"{chrome_path}" --profile-directory="{profile_directory}" {url}'

    # Execute the command
    subprocess.run(command, shell=True)

    # Wait for the window to open and become the foreground window
    time.sleep(1)

    def get_foreground_window_handle():
        """
        Returns the handle to the foreground window.
        """
        return win32gui.GetForegroundWindow()

    def resize_and_move_window(hwnd):
        """
        Resizes and moves the window to the specified position and size.
        """
        if hwnd:
            # Screen dimensions for half the screen
            screen_width_half = 2560 // 2
            screen_height_full = 1380

            # Calculate the position to place the window on the left half of the screen
            x_position = 0  # Start from the left edge of the screen
            y_position = 0  # Start from the top of the screen

            # Set the position and size of the window
            # Use win32con.HWND_TOP to ensure the window is placed at the top of the Z order
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x_position, y_position, screen_width_half, screen_height_full, 0)
        else:
            print("No active window found. Please ensure the window is open and selected.")

    # Get the handle of the current foreground window
    foreground_window_handle = get_foreground_window_handle()

    # Resize and move the foreground window
    resize_and_move_window(foreground_window_handle)
    
def open_and_position_browser(url, window_title):
    # Open the browser to the specified URL
    webbrowser.open(url)

    # Wait for the browser to open
    time.sleep(5)  # Adjust based on your system

    # Find the browser window using the title
    browser_handle = win32gui.FindWindow(None, window_title)

    if browser_handle:
        # Screen dimensions for half the screen
        screen_width_half = 2560 // 2
        screen_height_full = 1380

        # Calculate the position to place the window on the left half of the screen
        x_position = 0  # Start from the left edge of the screen
        y_position = 0  # Start from the top of the screen

        # Set the position and size of the window
        win32gui.SetWindowPos(browser_handle, win32con.HWND_TOP, x_position, y_position, screen_width_half, screen_height_full, 0)
    else:
        print("Browser window not found. Please ensure the title is correct and the browser is open to the specified page.")

def take_screen_shot(self,t):
    width = self.bottom_right[0] - self.top_left[0]
    height = self.bottom_right[1] - self.top_left[1]

    # Take a screenshot of the specified region using the class variables
    screenshot = pyautogui.screenshot(region=(self.top_left[0], self.top_left[1], width, height))
    self.count += 1  

  # Create a directory in the current working directory


    
    save_directory = os.path.join(os.getcwd(), f'{self.name}{t}')  # Correct path to save in current directory
    os.makedirs(save_directory, exist_ok=True)

    file_name = f"{self.name}{self.count}.jpeg"
    file_path = os.path.join(save_directory, file_name)
    try:
        screenshot.save(file_path)
        print(f"Saved screenshot as {file_name}")
    except Exception as e:
        print(f"Failed to save screenshot: {e}")
        
    print(file_name)
    return file_path



class Snap:
    def __init__(self):
        self.url = "https://www.snapchat.com/spotlight?locale=en-US"
        self.window_title = "Spotlight - Google Chrome"
        self.name = 'Snap'
        self.top_left = [44,240]
        self.bottom_right = [567,1056]
        self.count = 0

    def open_and_position_browser(self):
        # open_and_position_browser(self.url, self.window_title)
        open_and_position_chrome_window(self.url)

class TikTok:
    def __init__(self):
        self.url = "https://www.tiktok.com/"
        self.window_title = "TikTok - Make Your Day - Google Chrome"
        self.name = 'TikTok'
        self.top_left = [28,188]
        self.bottom_right = [648,1273]
        self.count = 0

    def open_and_position_browser(self):
        open_and_position_browser(self.url, self.window_title)
        # pyautogui.click(711,875)#continue
        pyautogui.click(668,598)#enter the vedio
        time.sleep(5)

class Youtube:
    def __init__(self):
        self.url = 'https://www.youtube.com/shorts/'
        self.top_left = [356,177]
        self.bottom_right = [980,1306]
        self.name = 'Youtube'
        self.count = 0

    def open_and_position_browser(self):
        open_and_position_chrome_window(self.url)
        
class Instagram:
    def __init__(self):
        self.url = 'https://www.instagram.com/reels/'
        self.window_title = "Instagram - Google Chrome"
        self.top_left = [410,160]
        # [272,153]
        self.bottom_right = [998,1133]
        # [914,1344]

        self.name = 'instagram'
        self.count = 0

    def open_and_position_browser(self):
        open_and_position_browser(self.url, self.window_title)
    
