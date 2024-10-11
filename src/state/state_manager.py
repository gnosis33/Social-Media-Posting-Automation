
# Pseudocode for State Manager

# Class StateManager:
#     Method __init__(state_file):
#         Load state data from file

#     Method get_last_post_time():
#         Return last post time from state data

#     Method get_current_video():
#         Return current video directory from state data

#     Method update_state(current_directory):
#         Determine next video directory
#         Update state data with next directory
#         Write updated state to file

#     Method update_last_post_time():
#         Update last post time in state data with current time
#         Write updated state to file

# state_manager.py file is responsible for managing the state of the application, such as the last post time and the current video directory.
# The StateManager class loads the state data from a file and provides methods to retrieve and update the state information.
# The get_last_post_time method returns the last post time from the state data.
# The get_current_video method returns the current video directory from the state data.
# The update_state method determines the next video directory, updates the state data with the next directory, and writes the updated state to the file.
# The update_last_post_time method updates the last post time in the state data with the current time and writes the updated state to the file.
# The state manager helps in maintaining the application's state across different runs and ensures that the application can resume from where it left off.
# The state data is stored in a file to persist the state information between runs.
# The state manager is used by other modules to retrieve and update the state information as needed.

# state_manager.py
import os
import json
import time

class StateManager:
    def __init__(self, state_file):
        """
        Initialize the StateManager object.

        Args:
            state_file (str): The path to the state file.
        """
        self.state_file = state_file
        self.video_folder = 'J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/Social-Media-Posting-Automation/videos'
        self.state_data = self.load_state()

    def load_state(self):
        """
        Load the state data from the state file.

        Returns:
            dict: The loaded state data.
        """
        try:
            with open(self.state_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Initialize default state if file not found
            return self.initialize_state()

    def initialize_state(self):
        """
        Initialize the state data with the first directory in the videos folder.

        Returns:
            dict: The initialized state data.
        """
        dirs = sorted(os.listdir(self.video_folder), key=int)
        if dirs:
            first_directory = dirs[0]
        else:
            first_directory = ""

        return {
            "last_post_time": 0,
            "current_video_directory": first_directory,
            "previous_video_directory": "",
            "next_video_directory": dirs[1] if len(dirs) > 1 else ""
        }

    def update_video_directories(self):
        """
        Update the video directory pointers in the state data.

        This method shifts the current video directory to the previous,
        moves the next directory to current, and updates the next directory
        to the one following the new current directory in the list, unless there
        is no next directory available.
        """
        dirs = sorted(os.listdir(self.video_folder), key=int)  # Ensure directories are sorted
        current_directory = self.state_data['current_video_directory']

        try:
            current_index = dirs.index(current_directory)
        except ValueError:
            current_index = -1  # handle the case where the directory is not found

        # Set the previous directory
        previous_dir = current_directory if current_index != -1 else ""

        # Update the current directory to the next one, or keep it if no next directory is set
        next_dir = self.state_data['next_video_directory']
        current_dir = next_dir if next_dir and next_dir in dirs else current_directory

        # Find the index of the new current directory
        try:
            new_current_index = dirs.index(current_dir)
        except ValueError:
            new_current_index = -1

        # Determine the next directory after the new current
        if new_current_index != -1 and new_current_index + 1 < len(dirs):
            next_next_dir = dirs[new_current_index + 1]
        else:
            next_next_dir = "1"

        # Assign the updated directories back to the state data
        self.state_data['previous_video_directory'] = previous_dir
        self.state_data['current_video_directory'] = current_dir
        self.state_data['next_video_directory'] = next_next_dir


    def get_last_post_time(self):
        """
        Get the last post time from the state data.

        Returns:
            int: The last post time.
        """
        return self.state_data.get('last_post_time', 0)

    def get_current_video_directory(self): ### THIS FUCKING BASTARD ###
        """
        Get the current video directory from the state data.

        Returns:
            str: The current video directory.
        """
        current_directory = self.state_data.get('current_video_directory', '')
        # Normalize the path to handle mixed slashes correctly
        return os.path.normpath(os.path.join(self.video_folder, current_directory))

    def update_state(self):
        """
        Update the state data by moving to the next video directory and write the updated state to the file.
        """
        self.update_video_directories()
        self.write_state_to_file()

    def update_last_post_time(self):
        """
        Update the last post time in the state data with the current time and write the updated state to the file.
        """
        print("updating state...")
        self.state_data['last_post_time'] = int(time.time())
        print(f"updated: {self.state_data}")
        self.write_state_to_file()

    def write_state_to_file(self):
        """
        Write the state data to the state file.
        """
        try:
            with open(self.state_file, 'w') as file:
                json.dump(self.state_data, file)
        except IOError as e:
            print(f"Failed to write state data to file {self.state_file}: {e}")

    def print_dir_list(self):
        dirs = sorted(os.listdir(self.video_folder), key=int)
        print(dirs)



# # Create an instance of the StateManager
# state_manager = StateManager('J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/Social-Media-Posting-Automation/data/state.json')

# # Update the video directories and write changes to the state file
# state_manager.update_state()

