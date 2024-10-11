import os
import random

def rename_all_directories_sequentially(base_folder, start_number):
    # Fetch all directory names in the base folder, ensuring that the listing is sorted
    dir_names = sorted([d for d in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, d))])

    # Step 1: Rename to a temporary name with a random 4-digit prefix
    temp_prefixes = {dir_name: str(random.randint(1000, 9999)) + "_" for dir_name in dir_names}
    for dir_name in dir_names:
        old_path = os.path.join(base_folder, dir_name)
        temp_path = os.path.join(base_folder, temp_prefixes[dir_name] + dir_name)
        os.rename(old_path, temp_path)
        print(f"Temporarily renaming {old_path} to {temp_path}")

    # Step 2: Rename from temporary to final desired names
    temp_dir_names = sorted([d for d in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, d)) and any(d.startswith(prefix) for prefix in temp_prefixes.values())])
    new_names = range(start_number, start_number + len(temp_dir_names))
    
    for temp_dir_name, new_name in zip(temp_dir_names, new_names):
        old_path = os.path.join(base_folder, temp_dir_name)
        new_path = os.path.join(base_folder, str(new_name))
        os.rename(old_path, new_path)
        print(f"Renaming {old_path} to {new_path}")

# Example usage
base_folder = "J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/SONG PROMO/Templates/NEXTROUND"
start_number = 79
rename_all_directories_sequentially(base_folder, start_number)


