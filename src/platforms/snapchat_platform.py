

import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import json
import time
import glob
import pyautogui
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
sys.path.insert(0, 'J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/Social-Media-Posting-Automation/src')
from utils.select_window import open_chrome_dev_tools, open_chrome_window



class SnapchatPlatform:
    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("debuggerAddress", "localhost:9988")

        # Path to your chromedriver (make sure it matches your Chrome version)
        self.service = Service(executable_path='J:\\Business\\OMNI-SCIENCE_RECORDS_LLC\\Marketing_Promotional\\Social-Media-Posting-Automation\\chromedriver\\chromedriver.exe')

        # Start the driver with the configured options
        self.driver = webdriver.Chrome(service=self.service, options=self.options)


    def login(self):
        try:
            self.driver.get("https://www.Snapchat.com/")
            wait = WebDriverWait(self.driver, 20)
            username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            username_field.send_keys(os.getenv('Snapchat_USERNAME'))
            password_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password"]')))
            password_field.send_keys(os.getenv('Snapchat_PASSWORD'))
            time.sleep(3)
            password_field.send_keys(Keys.RETURN)
            input("Please complete the 2FA/CAPTCHA in the browser, then press Enter to continue...")
        except Exception as e:
            print(f"Failed to login to Snapchat: {e}")

    def navigate_to_post_settings(self):
        """
        Navigate to the post settings page on Snapchat.
        """
        self.driver.get("https://my.snapchat.com/")
        time.sleep(10)


    def upload_video(self, video_directory):
        """
        Upload a video file from the specified directory to Snapchat.
        """
        # Find the .mp4 file in the video directory
        video_files = glob.glob(os.path.join(video_directory, "*.mp4"))
        
        if not video_files:
            raise FileNotFoundError("No .mp4 files found in the specified directory.")
        
        video_file = video_files[0]  # Assuming you want to pick the first one if there are multiple

        # Normalize the path for the operating system
        video_file = os.path.normpath(video_file)

        time.sleep(3)

        # select_video_button = WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_Yd"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[2]'))
        # )
        # time.sleep(1)
        # select_video_button.click()

            # Use execute_script to find and click the span by its class names and text content
                    # JavaScript to find the specific div and click it
        post_script = """
            var uploadButton = document.querySelector('button.ant-btn.sds-button.css-afv2hz.regular.sds-base-button.elevated');
            if (uploadButton) {
                uploadButton.click();
                console.log('Upload button clicked');
            } else {
                console.log('Upload button not found');
            }
            """ 
        time.sleep(1)
        open_chrome_dev_tools("Snapchat")
        time.sleep(1)
        open_chrome_window('Snapchat')
        time.sleep(1)
        pyautogui.hotkey('ctrl', '`')
        time.sleep(1)
        pyautogui.write(post_script)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write(video_file)  # Write the full path of the video file
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
        open_chrome_window('Snapchat')
        time.sleep(1)
        pyautogui.hotkey('ctrl', '`')
        time.sleep(120)
        open_chrome_dev_tools("Snapchat")
        time.sleep(1)


    def add_post_details(self, video_directory):
        """
        Read and add description, tags, and metadata from files in the directory.
        """
        # Assuming you have a JSON or text file containing this info
        with open(f"{video_directory}/metadata.json", "r") as file:
            metadata = json.load(file)
            description = metadata.get("description", "")
            name = metadata.get("name", "")
            tags = metadata.get("tags", [])
            tags_string = " ".join(tags) if tags else ""
            ID = metadata.get("ID", "")

            # Update the selector to target the correct paragraph element
        time.sleep(1)
        self.spotlight_button()
        time.sleep(1)
        self.my_story_button()
        try:
            description_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.sds-mentions-input__input[placeholder='Add a description and #topics']"))
            )
            # Ensure the field is clear before setting new text
            description_field.clear()  # This clears the textarea
            time.sleep(2)  # Short pause to ensure the field is clear

            # Construct and set the description text
            description_text = f"{tags_string} ID: {ID}"
            description_field.send_keys(description_text)
            print("Description added successfully.")

        except Exception as e:
            print(f"An error occurred while setting the description: {e}")

            # Add additional interactions here, such as adding tags if necessary
    def spotlight_button(self):
        try:
            # JavaScript to find the specific div and click it
            post_script = """
                var spotlightButton = document.querySelector('button.ant-btn.sds-button.css-15iiyh5.regular.sds-base-button.default.circle.ant-btn-circle');
                if (spotlightButton) {
                    spotlightButton.click();
                    console.log('Spotlight button clicked');
                } else {
                    console.log('Spotlight button not found');
                }
                """
            # Execute the JavaScript on the current page
            self.driver.execute_script(post_script)
            print("Executed click via JavaScript.")
        except Exception as e:
            print(f"An error occurred while trying to execute JavaScript click: {e}")

    def my_story_button(self):
        try:
            # JavaScript to find the specific div and click it
            post_script = """
                var postButton = document.querySelector('button.ant-btn.sds-button.css-15iiyh5');
                if (postButton) {
                    postButton.click();
                    console.log('Button clicked successfully.');
                } else {
                    console.log('Button not found.');
                }
                """
            # Execute the JavaScript on the current page
            self.driver.execute_script(post_script)
            print("Executed click via JavaScript.")
        except Exception as e:
            print(f"An error occurred while trying to execute JavaScript click: {e}")

    def submit_post(self):
        """
        Submit the post on Snapchat using JavaScript execution.
        """
        self.publish_button()
        time.sleep(5)
        self.accept_button()
        time.sleep(2)
        time.sleep(120)  # Wait for the post to be submitted

    def accept_button(self):
        try:
            # JavaScript to find the specific div and click it
            post_script = """
                var acceptButton = document.querySelector('button.ant-btn.sds-button.regular.sds-base-button.primary');
                if (acceptButton) {
                    acceptButton.click();
                    console.log('Accept button clicked successfully.');
                } else {
                    console.log('Accept button not found.');
                }
                """
            # Execute the JavaScript on the current page
            self.driver.execute_script(post_script)
            print("Executed click via JavaScript.")
        except Exception as e:
            print(f"An error occurred while trying to execute JavaScript click: {e}")

    def publish_button(self):
        try:
            # JavaScript to find the specific div and click it
            post_script = """
                var agreeButton = document.querySelector('button.ant-btn.sds-button.css-1jnwztg');
                if (agreeButton) {
                    agreeButton.click();
                    console.log('Button clicked successfully.');
                } else {
                    console.log('Button not found.');
                }
                """
            # Execute the JavaScript on the current page
            self.driver.execute_script(post_script)
            print("Executed click via JavaScript.")
        except Exception as e:
            print(f"An error occurred while trying to execute JavaScript click: {e}")