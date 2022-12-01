import os
from pytube import YouTube
import get_frames
from delete_data import delete_img, delete_vid
from snake_case import snake
from get_vid_ids import get_ids

### MAIN ###

# Admin input, comes from YTscrape script:
game = "Valorant"
query = "gameplay no commentary"
n_videos = 6
max_lenght = 0 # Implement: check lenght of video and skip if it is over max_lenght (timedate or just plain secs)
max_images = 2000 # Implement
cloud = False

# Creating video id list:
print("\n")
id_list = get_ids(game, query)
id_list = id_list[:n_videos] # to correct: should limit no. of videos in funct, not at this stage
print(f"Downloading and performing image extraction on {n_videos} videos:\n")

# Snake Case for use in folder names later:
game_snk = snake(game)

vid_path = "/home/julian/code/mauro-vb/game-shazam/scraping/temp_videos/"
img_path = f"/home/julian/code/mauro-vb/game-shazam/scraping/imgs/{game_snk}/"

# Check if it exists
itExist = os.path.exists(img_path)
if not itExist:
    # Create a new directory because it does not exist
    os.makedirs(img_path)
    print(f"New directory created for {game} images.\n")


# Downloading video and extracting frames for each downloaded video
for each in id_list:
    count_videos = 1
    try:
        print(f"Downloading video {each}...\t\t{count_videos}/{n_videos}\n")
        yt = YouTube(f'https://www.youtube.com/watch?v={each}')
        yt.streams.filter(
            progressive=True,
            file_extension='mp4').order_by('resolution').asc().first().download(
                output_path = vid_path,
                filename=f'{game_snk}_{each}.mp4',
                skip_existing = True, timeout = None, max_retries = 0)

                # Ordered by resolution, taking just the first, no timeout
                # These features could be changed by admin if needed

        count_videos += 1
        print("Extracting frames...\n")
        get_frames.extract_frames(f"{vid_path}{game_snk}_{each}.mp4",
                                   img_path, ident=each, gamename=game)



    except:
        continue

print("---------------------\n")
print(f"Finished generating images for '{game}' gameplay.\n")

if cloud == True:

    print("You have selected 'upload to cloud' instantly.")
    print("Feature unfinished. Will delete files without uploading.")
    print("Please interrupt.")
    breakpoint()

    # Call upload_img: bucket creation, uploading, etc.
    #print(f"Finished uploading '{game}' images to Google Cloud\n")


    # Call delete_data: delete local images and videos.
    delete_vid(path=vid_path)
    delete_img(path=img_path)
    print(f"\nFinished deleting local images and videos for '{game}'.\n")

else:

    #CALL delete_data: delete local images videos, keep images
    delete_vid(path=vid_path)
    print(f"Finished deleting local videos for '{game}'. Kept images.\n")

print("---------------------\n")
print("SCRAPING PROCESS FINISHED")
