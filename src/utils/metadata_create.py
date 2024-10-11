import json
import os

def create_metadata_json(video_directory):
    # Path configuration for each file
    name_path = os.path.join(video_directory, '@name.txt')
    tags_path = os.path.join(video_directory, '#tags.txt')
    description_path = os.path.join(video_directory, 'description.txt')
    id_path = os.path.join(video_directory, 'ID.txt')

    paths = {
        "name": name_path,
        "tags": tags_path,
        "description": description_path,
        "ID": id_path
    }

    metadata = {}
    
    try:
        # Check and read data from each file
        for key, path in paths.items():
            if os.path.exists(path):
                with open(path, 'r') as file:
                    content = file.read().strip()
                    if key == "tags":
                        metadata[key] = content.split()
                    else:
                        metadata[key] = content
            else:
                print(f"{key} file does not exist at {path}")
                return  # or continue based on how critical missing data is

        # Write metadata to a new JSON file
        metadata_path = os.path.join(video_directory, 'metadata.json')
        if os.path.exists(metadata_path):
            print(f"metadata.json exists in {video_directory}. Updating file with new data.")
        else:
            print(f"metadata.json does not exist in {video_directory}. Creating file.")

        with open(metadata_path, 'w') as file:
            json.dump(metadata, file, indent=4)
        print(f"Metadata.json created/updated successfully in {video_directory}")

    except Exception as e:
        print(f"Error processing metadata in {video_directory}: {e}")

# Example usage:
# create_metadata_json('J:\\Business\\OMNI-SCIENCE_RECORDS_LLC\\Marketing_Promotional\\Social-Media-Posting-Automation\\videos\\1')

