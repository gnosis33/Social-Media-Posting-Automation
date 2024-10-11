import os
import sys
sys.path.insert(0, 'J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/Social-Media-Posting-Automation/src')
from utils.metadata_create import create_metadata_json

def check_files_and_directory(video_directory):
    # Check if the directory exists
    if not os.path.exists(video_directory):
        print(f"Directory not found: {video_directory}")
        return False

    # Check for @name.txt file
    name_file_path = os.path.join(video_directory, '@name.txt')
    if not os.path.isfile(name_file_path):
        print(f"File not found: {name_file_path}")
        return False
    
    # Check for description.txt file
    description_file_path = os.path.join(video_directory, 'description.txt')
    if not os.path.isfile(description_file_path):
        print(f"File not found: {description_file_path}")
        return False
    
    # Check for #tags.txt file
    tags_file_path = os.path.join(video_directory, '#tags.txt')
    if not os.path.isfile(tags_file_path):
        print(f"File not found: {tags_file_path}")
        return False
    
    # check for ID.txt file
    id_file_path = os.path.join(video_directory, 'ID.txt')
    if not os.path.isfile(id_file_path):
        print(f"File not found: {id_file_path}")
        return False

    # Check for metadata.json file
    metadata_file_path = os.path.join(video_directory, 'metadata.json')
    if not os.path.isfile(metadata_file_path):
        print(f"File not found: {metadata_file_path}")
        print("Creating metadata.json file...")
        create_metadata_json(video_directory)
        return True

    print("All required files and directories are present.")
    return True

# Example usage
video_directory = 'J:\\Business\\OMNI-SCIENCE_RECORDS_LLC\\Marketing_Promotional\\Social-Media-Posting-Automation\\videos\\1'
check_files_and_directory(video_directory)
