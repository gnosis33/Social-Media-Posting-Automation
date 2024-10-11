# Pseudocode for TikTok Platform Implementation

# Class TikTokPlatform implements PlatformInterface:
#     Method login():
#         Navigate to TikTok login page
#         Enter TikTok login credentials
#         Handle TikTok 2FA if required

#     Method navigate_to_post_settings():
#         Navigate to TikTok's post settings page

#     Method upload_video(video_directory):
#         Upload video file from the given directory to TikTok

#     Method add_post_details(video_directory):
#         Read and add description, tags, and metadata from files in the directory

#     Method submit_post():
#         Submit the post on TikTok

# tiktok_platform.py file contains the implementation of the TikTokPlatform class, which extends the PlatformInterface class.
# The TikTokPlatform class provides an implementation, using selenium, to login, navigate to post settings, upload a video, add post details, and submit a post on TikTok.
# The class methods interact with TikTok's web interface to perform the necessary actions for posting a video.
# The TikTokPlatform class also has a function for selecting the description, tags, and metadata from files in the video directory and setting them in the description section of the TikTok post.
# The TikTokPlatform class is used by the Post class through the PlatformInterface to post videos to TikTok.
# The TikTokPlatform class is used by the LoginManager class through the PlatformInterface to login to TikTok.
# The TikTokPlatform class can be extended or modified to support additional features or changes in TikTok's web interface.

# tiktok_platform.py

import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import json
import time
import glob
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.insert(0, 'J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/Social-Media-Posting-Automation/src')
from utils.select_window import open_chrome_dev_tools, open_chrome_window

class TikTokPlatform:
    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("debuggerAddress", "localhost:9988")

        # Path to your chromedriver (make sure it matches your Chrome version)
        self.service = Service(executable_path='J:\\Business\\OMNI-SCIENCE_RECORDS_LLC\\Marketing_Promotional\\Social-Media-Posting-Automation\\chromedriver\\chromedriver.exe')

        # Start the driver with the configured options
        self.driver = webdriver.Chrome(service=self.service, options=self.options)


    def login(self):
        try:
            self.driver.get("https://www.tiktok.com/login/phone-or-email/email")
            wait = WebDriverWait(self.driver, 20)
            username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            username_field.send_keys(os.getenv('TIKTOK_USERNAME'))
            password_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password"]')))
            password_field.send_keys(os.getenv('TIKTOK_PASSWORD'))
            time.sleep(3)
            password_field.send_keys(Keys.RETURN)
            input("Please complete the 2FA/CAPTCHA in the browser, then press Enter to continue...")
        except Exception as e:
            print(f"Failed to login to TikTok: {e}")

# this is the page url for posting a video on tiktok: https://www.tiktok.com/tiktokstudio/upload?from=creator_center  once on this page we just need to upload the correct video by 
# pressing this button: <button class="TUXButton TUXButton--default TUXButton--medium TUXButton--primary" aria-disabled="false" type="button" data-hide="false" aria-label="Select videos"><div class="TUXButton-content"><div class="TUXButton-label">Select videos</div></div></button> this will open a file explorer where we can select the video we want to upload. Once the video is uploaded we can add the description and tags by pressing in the <div class="jsx-3804924985 caption-markup"><div class="jsx-3804924985 caption-editor"><div class="DraftEditor-root DraftEditor-alignLeft"><div class="DraftEditor-editorContainer"><div aria-autocomplete="list" aria-expanded="false" class="notranslate public-DraftEditor-content" contenteditable="true" role="combobox" spellcheck="true" style="outline: none; user-select: text; white-space: pre-wrap; overflow-wrap: break-word;"><div data-contents="true"><div class="" data-block="true" data-editor="dn9f1" data-offset-key="7hd4j-0-0"><div data-offset-key="7hd4j-0-0" class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"><span data-offset-key="7hd4j-0-0"><span data-text="true">DREAMOF852-0-Vid-1</span></span></div></div></div></div><grammarly-extension data-grammarly-shadow-root="true" class="dnXmp" style="position: absolute; top: 0px; left: -1px; pointer-events: none; z-index: auto;"></grammarly-extension><grammarly-extension data-grammarly-shadow-root="true" class="dnXmp" style="position: absolute; top: 0px; left: -1px; pointer-events: none; z-index: auto;"></grammarly-extension></div></div></div><div class="jsx-3804924985 caption-toolbar"><div class="jsx-3804924985 operation-button"><div class="jsx-3804924985 button-item"><button type="button" aria-label="Hashtag" id="web-creation-caption-hashtag-button" class="jsx-3804924985 caption-operation-icon"><svg fill="currentColor" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em"><path d="M34.7 3.11h2.42c.54 0 .94.5.83 1.02L35.73 15h6.55c.55 0 .95.5.83 1.03l-.43 2c-.12.57-.62.97-1.2.97H34.9l-1.83 9h7c.54 0 .94.5.83 1.03l-.44 2c-.12.57-.62.97-1.2.97h-7.01L30 43.02c-.12.57-.62.98-1.2.98h-2.43a.85.85 0 0 1-.83-1.02L27.8 32H16.43l-2.25 11.02c-.12.57-.62.98-1.2.98h-2.44a.85.85 0 0 1-.83-1.02L11.95 32H5.1a.85.85 0 0 1-.83-1.03l.43-2c.13-.57.63-.97 1.2-.97h6.87l1.84-9H7.48a.85.85 0 0 1-.83-1.03l.43-2c.12-.57.62-.97 1.2-.97h7.14l2.23-10.9c.12-.58.62-.99 1.2-.99h2.44c.53 0 .94.5.83 1.02L19.9 15h11.37l2.22-10.9c.12-.58.63-.99 1.21-.99ZM19.08 19l-1.84 9h11.37l1.84-9H19.08Z"></path></svg><span class="jsx-3804924985 caption-operation-icon__text">Hashtags</span></button></div><div class="jsx-3804924985 button-item"><button type="button" aria-label="@mention" id="web-creation-caption-mention-button" class="jsx-3804924985 caption-operation-icon"><svg fill="currentColor" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em"><path d="M24.28 44.54c-4.32 0-8.1-.87-11.33-2.6a18.05 18.05 0 0 1-7.49-7.2A21.94 21.94 0 0 1 2.87 23.9c0-4.04.87-7.57 2.6-10.61a18.21 18.21 0 0 1 7.43-7.15c3.2-1.7 6.88-2.55 11.04-2.55 4.04 0 7.59.77 10.66 2.3 3.1 1.51 5.5 3.67 7.2 6.49a18.19 18.19 0 0 1 2.6 9.79c0 3.52-.82 6.4-2.46 8.64-1.63 2.2-3.93 3.31-6.9 3.31-1.86 0-3.34-.4-4.42-1.2a4.6 4.6 0 0 1-1.73-3.7l.67.3a6.42 6.42 0 0 1-2.64 3.4 8.28 8.28 0 0 1-4.56 1.2 8.52 8.52 0 0 1-7.97-4.75 11.24 11.24 0 0 1-1.15-5.19c0-1.95.37-3.66 1.1-5.13a8.52 8.52 0 0 1 7.92-4.75c1.8 0 3.3.41 4.52 1.24 1.24.8 2.1 1.94 2.54 3.41l-.67.82v-4.04a1 1 0 0 1 1-1h2.27a1 1 0 0 1 1 1v12.05c0 .87.22 1.5.67 1.92.48.39 1.12.58 1.92.58 1.38 0 2.45-.75 3.22-2.26.8-1.53 1.2-3.44 1.2-5.7 0-3.05-.67-5.69-2.02-7.93a12.98 12.98 0 0 0-5.52-5.13 17.94 17.94 0 0 0-8.3-1.83c-3.3 0-6.23.69-8.79 2.07a14.82 14.82 0 0 0-5.9 5.76 17.02 17.02 0 0 0-2.11 8.59c0 3.39.7 6.35 2.11 8.88 1.4 2.5 3.4 4.41 6 5.76a19.66 19.66 0 0 0 9.17 2.01h10.09a1 1 0 0 1 1 1v2.04a1 1 0 0 1-1 1H24.28Zm-1-14.12c1.72 0 3.08-.56 4.07-1.68 1.03-1.12 1.54-2.64 1.54-4.56 0-1.92-.51-3.44-1.54-4.56a5.17 5.17 0 0 0-4.08-1.68c-1.7 0-3.05.56-4.08 1.68-.99 1.12-1.49 2.64-1.49 4.56 0 1.92.5 3.44 1.5 4.56a5.26 5.26 0 0 0 4.07 1.68Z"></path></svg><span class="jsx-3804924985 caption-operation-icon__text">Mention</span></button></div></div><div class="jsx-3804924985 word-count"><span class="jsx-3804924985">18</span><span class="jsx-3804924985">/</span><span class="jsx-3804924985">4000</span></div></div></div>  and pasting in the description from the metadata.json file. then we can press the "Post" button to post the video.
# note that the html example elements I provided are probably more html than is needed to find the elements, but I wanted to provide a clear example of what the elements look like on the page.

    def navigate_to_post_settings(self):
        """
        Navigate to the post settings page on TikTok.
        """
        self.driver.get("https://www.tiktok.com/tiktokstudio/upload?from=creator_center")
        time.sleep(10)
        # This will depend on TikTok's UI; adjust as necessary
        # input("Please complete the 2FA/CAPTCHA in the browser, then press Enter to continue...")


    def upload_video(self, video_directory):
        """
        Upload a video file from the specified directory to TikTok.
        """
        # Find the .mp4 file in the video directory
        print("uploading video")
        video_files = glob.glob(os.path.join(video_directory, "*.mp4"))
        
        if not video_files:
            raise FileNotFoundError("No .mp4 files found in the specified directory.")
        
        video_file = video_files[0]  # Assuming you want to pick the first one if there are multiple

        # Normalize the path for the operating system
        video_file = os.path.normpath(video_file)

        time.sleep(3)

        open_chrome_window("TikTok")
        time.sleep(1)
        open_chrome_dev_tools('TikTok')
        time.sleep(3)
        pyautogui.hotkey('ctrl', '`')
        time.sleep(3)
        self.select_video_button()
        time.sleep(3)
        # This will open the file selector; use pyautogui to interact with it
        pyautogui.write(video_file)  # Write the full path of the video file
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)
        open_chrome_window("TikTok")
        time.sleep(1)
        pyautogui.hotkey('ctrl', '`')
        time.sleep(1)
        open_chrome_dev_tools('TikTok')
        time.sleep(120)

         # Adjust the file selector and path as needed
    def select_video_button(self):
        try:
            
            select_video_button = """
                var buttons = document.querySelectorAll('button.TUXButton.TUXButton--default.TUXButton--medium.TUXButton--primary');
                var targetButton = Array.from(buttons).find(btn => btn.getAttribute('data-hide') === 'false');

                if (targetButton) {
                    targetButton.click();
                    console.log('Button clicked successfully.');
                } else {
                    console.log('Button not found or not clickable.');
                }
                """
            time.sleep(1)
            pyautogui.write(select_video_button)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            print("Executed click via JavaScript.")
        except Exception as e:
            print(f"An error occurred while trying to execute JavaScript click: {e}")


    def add_post_details(self, video_directory):
        """
        Read and add description, tags, and metadata from files in the directory.
        """
        # Assuming you have a JSON or text file containing this info
        print('adding post details')
        with open(f"{video_directory}/metadata.json", "r") as file:
            metadata = json.load(file)
            description = metadata.get("description", "")
            name = metadata.get("name", "")
            tags = metadata.get("tags", "")
            if len(tags) == 1:
                tags_string = tags[0]
            else:
                tags_string = " ".join(tags)
            ID = metadata.get("ID", "")
            # Assuming the description field is a text area
            try:
                # Use a more general selector to find the editable content area
                description_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".public-DraftEditor-content[contenteditable='true']"))
                )
                time.sleep(1)  # Short sleep to ensure the field is ready

                # Clear existing content in a more robust way
                description_field.click()  # Focus on the field
                description_field.send_keys(Keys.CONTROL + 'a')  # Select all content
                description_field.send_keys(Keys.DELETE)  # Delete the content

                # Define the text to be entered
                description_text = f"{description} Thx to {name} for the visuals. {tags_string} {ID}"
                time.sleep(1)
                # Send the new text to the description field
                description_field.send_keys(description_text)
                print("Description added successfully.")

            except Exception as e:
                print(f"An error occurred: {e}")
        time.sleep(5)
            # Add tags in a similar manner
            # This will depend on TikTok's UI; adjust as necessary

        

    def submit_post(self):
        """
        Submit the post on TikTok.
        """
        # time.sleep(120)  # Wait for the video to process
        print("submitting post")
        self.post_button()
        time.sleep(2)
        self.upload_button()
        time.sleep(5)
        # This will depend on TikTok's UI; adjust as necessary  

    def post_button(self):
        try:
            post_button = """
                var button = document.querySelector('button.TUXButton.TUXButton--default.TUXButton--large.TUXButton--primary');
                if (button) {
                    button.click();
                    console.log('Button clicked successfully.');
                } else {
                    console.log('Button not found or not clickable.');
                }
                """
            self.driver.execute_script(post_button)
            print("Executed click via JavaScript.")
        except Exception as e:
            print(f"An error occurred while trying to execute JavaScript click: {e}")

    def upload_button(self):
        try:
            post_button = """
                var button = document.querySelector('button.TUXButton.TUXButton--default.TUXButton--medium.TUXButton--primary');
                if (button) {
                    button.click();
                    console.log('Button clicked successfully.');
                } else {
                    console.log('Button not found or not clickable.');
                }
                """
            self.driver.execute_script(post_button)
            print("Executed click via JavaScript.")
        except Exception as e:
            print(f"An error occurred while trying to execute JavaScript click: {e}")


    def close_browser(self):
        """
        Close the browser session.
        """
        self.driver.quit()
