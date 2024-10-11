import os

def add_ctas_to_description_files(base_folder, ctas):
    # Make sure the CTAs list is accessible in the order provided
    cta_index = 0
    num_ctas = len(ctas)

    # Walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(base_folder):
        # We are only interested in subdirectories of the base folder
        if dirpath != base_folder:
            # Path for the description file in each folder
            description_file_path = os.path.join(dirpath, "description.txt")

            # Open the description file in write mode (creates if doesn't exist, overwrites if does)
            with open(description_file_path, "w") as desc_file:
                # Write one CTA to the description file
                desc_file.write(ctas[cta_index] + "\n")

            # Increment the CTA index, and wrap around if it exceeds the list length
            cta_index = (cta_index + 1) % num_ctas

# Example usage
base_folder = "J:/Business/OMNI-SCIENCE_RECORDS_LLC/Marketing_Promotional/SONG PROMO/Templates/COMPLETE"
ctas = [
    "Feel the tug of 'Bittersweet Sin.' Uncover the story woven into every note. Dive into the depths of forbidden love on Spotify—link in bio!",
    "Explore the shadows of forbidden love with 'Bittersweet Sin.' Experience the melody that dances with destiny on Spotify. Click to journey through the whispers of dreams—link in bio!",
    "Every love story has its shadows. Discover yours in 'Bittersweet Sin.' Let the melody of lost chances and forbidden touches resonate with you. Stream now on Spotify—link in bio!",
    "Don’t miss the song everyone will be talking about. 'Bittersweet Sin' is waiting. Join the experience that everyone will be whispering about before it's gone. Stream exclusively on Spotify—link in bio!",
    "'Bittersweet Sin' captures the essence of love caught in a storm. Embrace the melody that reflects the beauty of imperfection and the pain of inevitability. Your journey through the heart’s echoes starts on Spotify—link in bio!",
    "Unravel the echoes of 'Bittersweet Sin.' Dive into a story of forbidden love that refuses to end. Stream now on Spotify—link in bio!",
    "Join the thousands losing themselves in the haunting melody of 'Bittersweet Sin.' Don’t be the last to experience its allure. Listen today on Spotify!",
    "Discover the song that captures the agony and ecstasy of love. 'Bittersweet Sin' awaits on Spotify. Click to experience the saga of passion!",
    "Feel every heartbeat of 'Bittersweet Sin.' Let its rhythm sync with yours. Play it loud on Spotify—link in bio!",
    "'Bittersweet Sin' is the whisper in the night you can't ignore. Surrender to the sound. Stream now on Spotify!",
    "Are you ready for a love that defies the ordinary? 'Bittersweet Sin' is streaming now. Find out why everyone can't stop talking about it—link in bio!",
    "Step into the shadow of love with 'Bittersweet Sin.' Let its story envelop you. Available now on Spotify!",
    "Catch the latest sensation before it fades. 'Bittersweet Sin' is your next obsession. Stream exclusively on Spotify!",
    "Every verse of 'Bittersweet Sin' is a confession. Every chorus, a revelation. Don’t miss out. Listen now on Spotify!",
    "Discover why 'Bittersweet Sin' is the anthem of twisted love stories. Experience it first-hand on Spotify!",
    "From whispered secrets to heart-wrenching choruses, 'Bittersweet Sin' delivers. Dive deep into the drama on Spotify now!",
    "Let 'Bittersweet Sin' pull you back in with every play. Surrender to the saga of love and loss on Spotify!",
    "Unlock the mystery of 'Bittersweet Sin.' Each listen reveals more. Explore the depths of forbidden love on Spotify!",
    "'Bittersweet Sin'—where every note is a pulse of passion. Feel the intensity on Spotify!",
    "Challenge the silence with 'Bittersweet Sin.' Let its story break the quiet of your night. Stream now on Spotify!",
    "'Bittersweet Sin' isn't just a song, it's an experience. Embark on an auditory journey that you'll never forget. Listen now on Spotify!",
    "Join the legion of fans who can’t get enough of 'Bittersweet Sin.' Become part of the movement. Listen on Spotify!",
    "Dare to explore the darker side of love with 'Bittersweet Sin.' Feel its power, now streaming on Spotify!",
    "Escape into the melodic embrace of 'Bittersweet Sin.' Let its haunting lyrics captivate you. Stream on Spotify!",
    "Confront the echoes of a forbidden love with 'Bittersweet Sin.' Uncover the truths hidden in its verses. Listen now on Spotify!",
    "Get lost in the echoes of 'Bittersweet Sin.' Experience the raw emotion and haunting beauty tonight on Spotify!",
    "Surrender to the irresistible pull of 'Bittersweet Sin.' Join the wave of listeners captivated by its allure—stream now on Spotify!",
    "Step beyond the ordinary into the extraordinary with 'Bittersweet Sin.' Discover the passion, live the drama—available now on Spotify!",
    "'Bittersweet Sin' whispers tales of love and regret. Tune in to hear what secrets it reveals—only on Spotify!",
    "Don't just listen to music—feel it with 'Bittersweet Sin.' Let each note carve a story in your heart. Stream it live on Spotify!",
    "Witness the collision of love and destiny in 'Bittersweet Sin.' Dive into the depths of desire on Spotify today!",
    "Feel the chill of 'Bittersweet Sin' as it traces the spine of forbidden love. Embrace the thrill only on Spotify!",
    "Break free with 'Bittersweet Sin' and discover the beauty of tragic love. Listen, feel, and escape—now streaming on Spotify!",
    "Join the chorus of souls haunted by 'Bittersweet Sin.' Let your voice be heard in the symphony of its followers. Play it now on Spotify!",
    "Each chord of 'Bittersweet Sin' resonates with lost dreams. Tune in to find yours on Spotify now!",
    "Embrace the melody that dances with shadows. 'Bittersweet Sin' is your ticket to a world of deep emotion—stream on Spotify!",
    "Ride the waves of 'Bittersweet Sin's' powerful ballads. Don't miss out on the song that's rewriting love rules—listen on Spotify!",
    "Experience the intoxicating pull of 'Bittersweet Sin.' It's more than a song—it's a revelation. Uncover it on Spotify!",
    "Let 'Bittersweet Sin' echo through the halls of your heart. Its powerful lyrics are waiting—discover them on Spotify!",
    "Delve into the narrative of 'Bittersweet Sin,' where every lyric tells a piece of a larger story. Explore the saga on Spotify now!",
    "Let the hauntingly beautiful melodies of 'Bittersweet Sin' sweep you off your feet. There’s no better time than now on Spotify!",
    "Challenge the silence of the night with the poignant strains of 'Bittersweet Sin.' Let its melody fill your world—streaming now on Spotify!",
    "Are you brave enough to face the bittersweet truths of love? 'Bittersweet Sin' awaits your verdict on Spotify.",
    "Join the odyssey of love and loss with 'Bittersweet Sin.' Your new favorite anthem of heartache is just a play away on Spotify!",
    "Immerse yourself in the story of 'Bittersweet Sin.' Let its music narrate the complexities of passion—now playing on Spotify!",
    "Dance under the shadow of the moon with 'Bittersweet Sin.' Feel its rhythm guide your every move—stream on Spotify!",
    "Unveil the hidden depths of 'Bittersweet Sin' and let its tales of dark romance captivate you. Listen now on Spotify!",
    "Let 'Bittersweet Sin' take you on a journey through the highs and lows of love. Experience every emotion on Spotify!",
    "Plunge into the depths of 'Bittersweet Sin' and let its current carry you away. Available for your soul on Spotify!",
    "Capture the essence of forbidden love with 'Bittersweet Sin.' Let its melody be your secret—stream it on Spotify!",
    "Revel in the haunting allure of 'Bittersweet Sin.' Let it transport you to another world of emotions. Available now on Spotify!",
    "Turn up the volume and let 'Bittersweet Sin' fill the corners of your room. Experience the sound of true passion on Spotify!"
]
add_ctas_to_description_files(base_folder, ctas)
