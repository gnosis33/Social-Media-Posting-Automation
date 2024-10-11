# Pseudocode for Utility Functions

# Function check_for_exit():
#     Check if exit condition (e.g., escape key) is met

# Function time_to_post(last_post_time, wait_time):
#     Calculate if current time is greater than last post time plus wait time

# Function get_current_time():
#     Return current date and time

# Function sleep_until_next_check():
#     Sleep for a specified interval before re-checking conditions

# utility.py file contains utility functions that are used by other modules in the application.
# The check_for_exit function checks if an exit condition, such as pressing the escape key, is met.
# The time_to_post function calculates if the current time is greater than the last post time plus the wait time.
# The get_current_time function returns the current date and time.
# The sleep_until_next_check function pauses the execution for a specified interval before re-checking the conditions.
# These utility functions help in managing the flow of the application and performing common tasks such as checking for exit conditions and waiting for the next check interval.
# The utility functions are reusable and can be called from different modules to perform specific tasks.

# utility.py

import time
import keyboard

class Utility:
    """
    Utility class for common functions.
    """
    def __init__(self, config):
        self.config = config

    def check_for_exit(self):
        """
        Check if exit condition (e.g., escape key) is met.
        """
        if keyboard.is_pressed('esc'):
            return True

    def time_to_post(self, last_post_time, wait_time):
        """
        Calculate if current time is greater than last post time plus wait time.
        """
        if time.time() >= last_post_time + wait_time:
            return True

    def get_current_time(self):
        """
        Return current date and time.
        """
        return time.time()

    def sleep_until_next_check(self):
        """
        Sleep for a specified interval before re-checking conditions.
        """
        time.sleep(self.config.check_interval)



