import os

def append_to_empty_files(base_folder):
    # Traverse all directories in the base folder
    for dir_name in os.listdir(base_folder):
        dir_path = os.path.join(base_folder, dir_name)
        if os.path.isdir(dir_path):
            file_path = os.path.join(dir_path, '@name.txt')
            # Check if the file exists
            if os.path.exists(file_path):
                # Check if the file is empty
                if os.stat(file_path).st_size == 0:
                    with open(file_path, 'a') as file:
                        file.write('@Giphy')
                    print(f"Appended '@Giphy' to {file_path}")

# Example usage
base_folder = "J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/SONG PROMO/Templates/NEXTROUND"
append_to_empty_files(base_folder)
