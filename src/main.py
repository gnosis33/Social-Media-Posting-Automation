# main.py

import json
import time
# import sys
from dotenv import load_dotenv
import os

print("Before loading .env:", os.getenv('TIKTOK_USERNAME'))
load_dotenv()  # Make sure this is pointing to the correct path if needed
print("After loading .env:", os.getenv('TIKTOK_USERNAME'))

# import time
from config import Config
from state.state_manager import StateManager
from utils.utility import Utility
from utils.metadata_create import create_metadata_json
from posting.post import PostManager
from login.login_manager import LoginManager
from platforms.platform_interface import PlatformManager #, PlatformInterface
from log.logger import Logger


# Define the path to the state file using a platform-independent method
state_file_path = os.path.join('data', 'state.json')

# Check if the state file exists
if not os.path.exists(state_file_path):
    initial_state = {
        "last_post_time": 0,
        "current_video_directory": "",
        "previous_video_directory": "",
        "next_video_directory": ""
    }
    with open(state_file_path, 'w') as file:
        json.dump(initial_state, file)

def main():
    # Initialize configuration using the singleton pattern
    config = Config.get_instance()

    # Initialize utility class with config
    utility = Utility(config)

    # Initialize platform manager with platforms from config
    print("this is the config.platforms:", config.platforms)
    platform_manager = PlatformManager(config.platforms)

    # Initialize state manager with state file from config
    print("this is the state file path:", state_file_path)
    state_manager = StateManager(state_file_path)

    # Initialize logger with log file from config
    print("this is the log file path:", config.log_file_path)
    logger = Logger(config.log_file_path)

    # Initialize post manager with platforms
    print("this is the platform manager:", platform_manager)    
    post_manager = PostManager(platform_manager)

    # Initialize login manager with platforms
    print("this is the platform manager:", platform_manager)
    # login_manager = LoginManager(platform_manager)

    # # Login to all platforms using login manager
    # print("Logging in to all platforms...")
    # # login_manager.login_to_all_platforms()
    # print("Successfully logged in to all platforms.")

    print("Starting main loop...")

    while True:
        # If check for exit condition:
        if utility.check_for_exit():
            break

        # Get current video directory from state manager
        current_video_directory = state_manager.get_current_video_directory()

        # Get last post time from state manager
        last_post_time = state_manager.get_last_post_time()

        print("this is the current video directory:", current_video_directory)
        create_metadata_json(current_video_directory)

        # If time to post (based on last post time and wait time from config):
        print("this is the last post time:", last_post_time)
        if utility.time_to_post(last_post_time, config.wait_time):
            try:
                # Post video to all platforms using post manager
                print("this is the current video directory:", current_video_directory)

                post_manager.post_video_to_all_platforms(current_video_directory)

                # Update state with current video
                print("this is the current video directory:", current_video_directory)
                state_manager.update_state()
                print("this is the state manager.update_state:", state_manager)
                # Update last post time in state manager
                print("this is the state manager.update:", state_manager)
                state_manager.update_last_post_time()
            except Exception as e:
                # Catch exceptions and log errors
                logger.log_error(str(e))

        # Sleep until next check interval
        utility.sleep_until_next_check()
        # print("this is the time.time():", time.time()) as int
        print("this is the time.time():", int(time.time()))

if __name__ == "__main__":
    main()

