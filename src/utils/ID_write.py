import os

def increment_hex(hex_str):
    # Increment hexadecimal string
    return "{:04X}".format(int(hex_str, 16) + 1)

def write_unique_ids_to_subfolders(base_folder, initial_id='1000'):
    # Initialize the starting ID
    current_id = initial_id

    # Get a list of directories directly under the base_folder
    directories = next(os.walk(base_folder))[1]
    # Sort directories numerically
    directories.sort(key=lambda x: int(x))

    # Assign unique IDs to each directory
    for dirname in directories:
        id_file_path = os.path.join(base_folder, dirname, "ID.txt")
        with open(id_file_path, "w") as id_file:
            id_file.write(current_id)
        
        # Increment ID after writing to the file
        current_id = increment_hex(current_id)

# Example usage
base_folder = "J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/Social-Media-Posting-Automation/videos"
write_unique_ids_to_subfolders(base_folder)




