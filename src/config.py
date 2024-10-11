# Pseudocode for Configuration File

# Class Config:
#     Method __init__():
#         Initialize list of platforms (e.g., ["TikTok", "OtherPlatform"])
#         Initialize login credentials for platforms from .env file
#         Initialize wait time for posting (e.g., in seconds)
#         Initialize state file path (e.g., "/data/state.json")
#         Initialize log file path (e.g., "/data/logs.txt")


#config.py file is responsible for storing the configuration settings for the application.
# The Config class initializes the list of platforms, login credentials, wait time for posting, state file path, and log file path.
# The configuration settings are used by other modules to determine the behavior of the application, such as the platforms to post to, the wait time between posts, and the file paths for state and log files.
# The configuration settings can be modified by changing the values in the Config class, allowing for flexibility in the application's behavior.

# config.py



from platforms.tiktok_platform import TikTokPlatform
from platforms.instagram_platform import InstagramPlatform
from platforms.youtube_platform import YouTubePlatform
from platforms.facebook_platform import FacebookPlatform
from platforms.snapchat_platform import SnapchatPlatform
# from platforms.twitter_platform import TwitterPlatform

from dotenv import load_dotenv
import os

class Config:
    _instance = None

    def __new__(cls):
        """Ensure only one instance of Config is created."""
        if cls._instance is None:
            print("Creating Config instance")
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        """Initialize the configuration attributes from environment variables."""
        self.platforms = {
            'TikTok': TikTokPlatform(),
            # 'Instagram': InstagramPlatform(),
            'YouTube': YouTubePlatform(),
            'Facebook': FacebookPlatform(),
            # 'Snapchat': SnapchatPlatform(),
            # 'Twitter': TwitterPlatform(),
        }
        self.wait_time = 24 * 60 * 60  # 24 hours in seconds
        self.check_interval = 5 * 60
        self.state_file_path = os.getenv('STATE_FILE_PATH', "../data/state.json")
        self.log_file_path = os.getenv('LOG_FILE_PATH', "../data/logs.txt")
        self.login_credentials = self.load_login_credentials()
        print (self.login_credentials)

    def load_login_credentials(self):
        # Load login credentials from .env file
        return {
            "TikTok": {
                "username": os.getenv('TIKTOK_USERNAME'),
                "password": os.getenv('TIKTOK_PASSWORD')
            },
            "Instagram": {
                "username": os.getenv('INSTAGRAM_USERNAME', 'instagram_user'),
                "password": os.getenv('INSTAGRAM_PASSWORD', 'instagram_password')
            },
            "YouTube": {
                "username": os.getenv('YOUTUBE_USERNAME', 'youtube_user'),
                "password": os.getenv('YOUTUBE_PASSWORD', 'youtube_password')
            },
            "Facebook": {
                "username": os.getenv('FACEBOOK_USERNAME', 'facebook_user'),
                "password": os.getenv('FACEBOOK_PASSWORD', 'facebook_password')
            },
            "Snapchat": {
                "username": os.getenv('SNAPCHAT_USERNAME', 'snapchat_user'),
                "password": os.getenv('SNAPCHAT_PASSWORD', 'snapchat_password')
            },
            # "Twitter": {
            #     "username": os.getenv('TWITTER_USERNAME', 'twitter_user'),
            #     "password": os.getenv('TWITTER_PASSWORD', 'twitter_password')
            # },
        }
    @classmethod
    def get_instance(cls):
        """Access the instance."""
        if cls._instance is None:
            cls()
        return cls._instance
    