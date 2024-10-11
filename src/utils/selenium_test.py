from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9988")

# Path to your chromedriver (make sure it matches your Chrome version)
service = Service(executable_path='chromedriver\\chromedriver.exe')

# Start the driver with the configured options
driver = webdriver.Chrome(service=service, options=options)

# Now you can control the already-open Chrome with Selenium
driver.get("http://www.tiktok.com")
