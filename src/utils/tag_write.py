import os

def add_hashtags_to_subfolders(base_folder, hashtags):
    # List of hashtags to be written
    hashtag_content = "\n".join(hashtags)
    
    # Walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(base_folder):
        # Skip the base folder itself, only consider subfolders
        if dirpath != base_folder:
            tags_file_path = os.path.join(dirpath, "#tags.txt")
            # Open the tags file in append mode or create it if it doesn't exist
            with open(tags_file_path, "w") as tags_file:
                tags_file.write(hashtag_content + "\n")

# Example usage
# base_folder = "J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/Social-Media-Posting-Automation/videos"
base_folder = 'J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/SONG PROMO/Templates/COMPLETE'
hashtags = ["#bittersweetsin", "#popmusic", "#top40"]  # List your hashtags here
# hashtags = ["#edm", "#bassmusic", "#SpotifyRelease"]  # List your hashtags here
add_hashtags_to_subfolders(base_folder, hashtags)
