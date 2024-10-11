Social Media Automation Tool
This tool was created for OMNI-SCIENCE RECORDS LLC to automate social media posting.

⚠️ Important Notice
This tool will not function out-of-the-box as uploaded to GitHub. You will need to perform additional setup to make it work for your specific use case. Feel free to modify the code to suit your own social media automation needs.

💻 How It Works
The tool uses Selenium to automate browser interactions and post to various social media platforms. To bypass common barriers such as Captcha and Two-Factor Authentication (2FA), it uses a dedicated Chrome instance that maintains login credentials across sessions.

🛠️ ChromeDriver Version Compatibility
Please note that the ChromeDriver provided in this project is only compatible with Chrome version 129.0.6668.90. If you are using a different version of Chrome, the tool may not function correctly.

How to Check Your Chrome Version
Open Google Chrome.
Click on the three-dot menu in the top-right corner of the browser.
Go to Help > About Google Chrome.
A new tab will open, showing your current Chrome version.
If your Chrome version does not match 129.0.6668.90, you will need to download the corresponding version of ChromeDriver from the official ChromeDriver site: "https://googlechromelabs.github.io/chrome-for-testing/"

🛠️ Setup and Configuration
Chrome Automation Instance: A dedicated instance of Chrome is used for automation, which already contains the required login credentials. You can configure this in the code by specifying your own Chrome user data directory.

Example command to launch the Chrome instance with remote debugging:

bash:
chrome.exe --remote-debugging-port=9988 --user-data-dir="J:\Business\OMNI-SCIENCE_RECORDS_LLC\Marketing_Promotional\Social-Media-Posting-Automation\chromedata"
Make sure to replace the file path with the location of your own Chrome user data directory.

Bypassing Captcha & 2FA: This setup works by keeping you logged into your social media accounts, bypassing the need to deal with Captcha or 2FA during automation. Ensure you use a separate Chrome profile dedicated to automation to prevent accidental logouts.

⚙️ How It Functions
The tool relies on several key files to automate the social media posting process efficiently:

Hashtags (#tags.txt):

Hashtags are crucial for optimizing the reach of your posts.
The tool reads from the #tags.txt file, which contains a list of hashtags to be used in post descriptions.
Ensure this file is updated with relevant hashtags for your posts.
Video ID Tracking (ID.txt):

To avoid reposting the same video multiple times, the tool tracks previously posted videos using the ID.txt file.
This file logs the video IDs of all posted content. If you're adding new content, be sure to update this file.
Post Descriptions (description.txt):

The text content of your social media posts is stored in description.txt, which includes any relevant descriptions, hashtags, and promotional information.
This file can be customized based on the platform and the post’s content.
Tagging/Referencing Usernames (@name.txt):

The tool allows you to tag other social media users in your posts by referencing the @name.txt file.
Add the social media handles you want to tag here, and the tool will automatically include them in your posts where appropriate.
🔧 Utilities Folder
In the utilities folder, you will find several tools designed to streamline the process of creating and managing the necessary data files for automation:

Mass Data Creation:

Tools to automate the creation and mass addition of data to files like #tags.txt, ID.txt, @name.txt, and description.txt. These utilities help speed up the process of populating large volumes of data for multiple posts.
Video Folder Naming Tools:

Additional tools are available to help with properly naming video folders to keep the automation process organized and structured.
🎥 Example Videos
Example videos demonstrating how the tool works are included in the videos folder within the GitHub repository. These videos showcase the automation process of posting to social platforms with the necessary hashtags, descriptions, and tagged users.

📦 Dependencies
The tool relies on several Python libraries, which are listed in the requirements.txt file. It's highly recommended to install these in a virtual environment to avoid conflicts with other Python projects.

⚙️ Setting Up a Virtual Environment
Navigate to your project folder and create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
.\venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the dependencies listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
📋 Requirements
The required libraries are listed in requirements.txt and include:

numpy: For numerical operations (if needed).
pandas: For handling CSV files and data management.
selenium: For automating browser interaction.
loguru: For advanced logging functionality (optional, you can use Python's built-in logging).
simplejson: For reading and writing JSON files (you may also use Python’s built-in json library).
python-dateutil: For managing dates and times.
requests: For making HTTP requests to web services (useful for API interactions).
python-dotenv: For loading environment variables from a .env file.
pyautogui: For automating GUI interactions (optional, Selenium can handle most automation).
keyboard: For simulating keyboard inputs (optional, Selenium can handle keyboard events).
pygetwindow: For getting information about windows and controlling them.
🚀 Getting Started
Clone the repository to your local machine.
Set up your Chrome automation instance as outlined above.
Install the necessary dependencies (see instructions above on setting up a virtual environment).
Update the necessary files (#tags.txt, ID.txt, description.txt, @name.txt) with your own data.
Review the example videos in the videos folder to understand the process flow.
Run the script using the following command:
bash:
python automate_social_media.py
Make sure to review and customize the code based on the specific platforms you intend to post to. Different platforms may require unique workarounds or slight adjustments for best performance.