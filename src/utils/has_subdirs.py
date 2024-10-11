import os

def list_directories_with_subdirs(base_folder):
    # List to store directories with subdirectories
    dirs_with_subdirs = []
    
    # Walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(base_folder):
        # Check if the current directory has subdirectories
        if dirnames:  # If dirnames list is not empty
            parent_dir = os.path.basename(dirpath)  # Get the name of the current directory
            dirs_with_subdirs.append(parent_dir)
    
    # Print directories that have subdirectories
    print("Directories with subdirectories:")
    for dir in dirs_with_subdirs:
        print(dir)

# Example usage
base_folder = "J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/SONG PROMO/Templates/COMPLETE"
list_directories_with_subdirs(base_folder)
