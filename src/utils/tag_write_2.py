import os
import random

def add_random_hashtags_to_subfolders(base_folder, hashtags, num_tags=3):
    # Walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(base_folder):
        # Skip the base folder itself, only consider subfolders
        if dirpath != base_folder:
            # Generate a random selection of hashtags
            random_hashtags = random.sample(hashtags, num_tags)
            # Create the content to write to the file
            hashtag_content = "\n".join(random_hashtags)
            tags_file_path = os.path.join(dirpath, "#tags.txt")
            # Open the tags file in write mode or create it if it doesn't exist
            with open(tags_file_path, "w") as tags_file:
                tags_file.write(hashtag_content + "\n")

# Example usage
# base_folder = "J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/Social-Media-Posting-Automation/videos"
base_folder = 'videos'
hashtags = [
    "#BittersweetLove", "#ComplexLove", "#IntrospectiveMusic", "#RomanticVibes", 
    "#ChilloutMusic", "#MelancholicSounds", "#DreamyBeats", "#ElectronicMusic", 
    "#ElectronicaVibes", "#Synthpop", "#AmbientMusic", "#IndiePop", 
    "#LoveAndLoss", "#FatalKiss", "#SocietalJudgment", "#MusicAndMetaphors", 
    "#Yearning", "#MidHighVocals", "#MusicStorytelling", "#ElectronicPop",
    # General Music Hashtags
    "#NewMusic", "#MusicFriday", "#NowPlaying", "#IndiePop", "#ElectronicMusic",
    # Genre-Specific
    "#Electropop", "#Synthpop", "#ChilloutVibes", "#AmbientSounds", "#DreamyTunes",
    # Mood-Based
    "#MellowMonday", "#ChillVibes", "#RomanticMood", "#IntrospectiveLyrics", "#BittersweetMelodies",
    # Thematic
    "#LoveSongs", "#SocietyReflections", "#IntimateMusic", "#ConflictInLove", "#ModernRomance",
    # Production
    "#SynthesizerSounds", "#ElectronicBeats", "#136BPM", "#BFlatMinor", "#VocalHarmony",
    # Engagement
    "#MusicRecommendation", "#ListenNow", "#AddToPlaylist", "#MusicDiscovery", "#NewArtist"
]
add_random_hashtags_to_subfolders(base_folder, hashtags)
