# Pseudocode for Post Manager

# Class Post:
#     Method __init__(platforms):
#         Initialize platforms list

#     Method post_video_to_all_platforms(video_directory):
#         For each platform in platforms:
#             Try:
#                 Navigate to post settings on platform
#                 Upload video from directory
#                 Add post details (description, name, ID, tags, metadata) to platform
#                 Submit post on platform
#             Catch exceptions and log errors

#     Method add_post_details(platform, video_directory):
#         Read description from file in video directory
#         Read tags from file in video directory
#         Read metadata from JSON file in video directory
#         Set post details on the platform


# post.py is a Python script that defines a Post class with methods for posting videos to multiple platforms. 
# The class has an __init__ method that initializes a list of platforms, and a post_video_to_all_platforms method that iterates over each platform, posting a video to each one. 
# The class also has an add_post_details method that reads post details from files in a video directory and sets them on the platform.
# The Post class calls the PlatformInterface method which intern calls the Platform Classes to post the video on the respective platform.

# usage of the post.py

# from tiktok_platform import TikTokPlatform
# # Import other platform classes here

# # Create instances of platform classes
# tiktok = TikTokPlatform()  # Assume this class has been properly set up
# # other_platform = OtherPlatform()

# # List of all platform instances
# platforms = [tiktok]

# # Initialize PostManager with the platforms
# post_manager = PostManager(platforms)

# # Post a video to all platforms
# video_directory = "/path/to/video_directory"
# post_manager.post_video_to_all_platforms(video_directory)


# post.py
import time
import json
# from exceptions import NetworkError, Exception
import sys
sys.path.insert(0, 'J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/Social-Media-Posting-Automation/src')
from utils.metadata_create import create_metadata_json
from utils.dir_check import check_files_and_directory


class PostManager:
    """
    Manages the process of posting videos to multiple social media platforms.
    """
    
    def __init__(self, platform_manager):
        # Initialize the PostManager with a list of platforms
        self.platform_manager = platform_manager

    def post_video_to_all_platforms(self, video_directory):
        # Iterate over each platform and post the video
        for platform in self.platform_manager.get_all_platforms():
            try:
                print(f"Starting post process on {platform.__class__.__name__}...")
                # Navigate to the post settings on the platform
                time.sleep(1)
                platform.navigate_to_post_settings()
                # Upload the video from the specified directory
                time.sleep(1)
                platform.upload_video(video_directory)
                # Add post details to the platform
                time.sleep(1)
                self.add_post_details(platform, video_directory)
                # Submit the post on the platform
                time.sleep(1)
                platform.submit_post()
                print(f"Posted successfully on {platform.__class__.__name__}.")
            except FileNotFoundError as e:
                print(f"File not found during posting on {platform.__class__.__name__}: {e}")
            except NetworkError as e:
                print(f"Network issue on {platform.__class__.__name__}: {e}")
            except Exception as e:
                print(f"Failed to post on {platform.__class__.__name__}: {e}")

    def add_post_details(self, platform, video_directory):
        # Create or update the metadata.json from individual data files        
        # If metadata.json does not exist, create it
        # Check the existence of files and directory once and store the result
        files_present = check_files_and_directory(video_directory)

        if not files_present:
            print('Some files are missing.')
            # Try to recover or handle the missing files situation here
        else:
            print("All files are present")
            platform.add_post_details(video_directory)
