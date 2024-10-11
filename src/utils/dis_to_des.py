import os

def rename_files(base_folder, old_name, new_name):
    # Walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(base_folder):
        # Check each file in the current directory
        for filename in filenames:
            if filename.lower() == old_name.lower():  # Case-insensitive comparison
                old_file_path = os.path.join(dirpath, filename)
                new_file_path = os.path.join(dirpath, new_name)
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed {old_file_path} to {new_file_path}")

# Example usage
# 
base_folder = "J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/Social-Media-Posting-Automation/videos"
# base_folder = 'J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/SONG PROMO/Templates/COMPLETE'
rename_files(base_folder, "discription.txt", "description.txt")
