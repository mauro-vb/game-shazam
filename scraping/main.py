import os
from pytube import YouTube
import get_frames
from snake_case import snake
from get_vid_ids import get_ids
from delete_data import delete

### MAIN ###

# Admin input:
game = "t3 arena"
n_videos = 2
run_local = False

# Creating video id list:
print("\n")
id_list = get_ids(game)
id_list = id_list[:n_videos] # to correct: should limit no. of videos in funct, not at this stage
print(f"Downloading and performing image extraction on {n_videos} videos...\n")

# Snake Case for use in folder names later:
game_snk = snake(game)


output_path = f"imgs/{game_snk}/"
# Check if it exists
itExist = os.path.exists(output_path)
if not itExist:
    # Create a new directory because it does not exist
    os.makedirs(output_path)
    print(f"New directory created for {game} images\n")


# Downloading video and extracting frames for each downloaded video
for each in id_list:

    try:
        print(f"Downloading video {each}...\n")
        yt = YouTube(f'https://www.youtube.com/watch?v={each}')
        yt.streams.filter(
            progressive=True,
            file_extension='mp4').order_by('resolution').asc().first().download(
                output_path = 'temp_videos',filename=f'{game_snk}_{each}.mp4',
                skip_existing = True, timeout = None, max_retries = 0)

                # Ordered by resolution, taking just the first, no timeout
                # These features could be changed by admin if needed

        print("Extracting frames...\n")
        get_frames.extract_frames(f'temp_videos/{game_snk}_{each}.mp4', output_path, ident=each)

    except:
        continue

print("---------------------\n")
print(f"Finished generating images for '{game}' gameplay\n")

if run_local = False:

    #CALL upload_img: bucket creation, uploading, etc.
    #print(f"Finished uploading '{game}' images to Google Cloud\n")
    breakpoint


    #CALL delete_data: delete local images and videos.
    delete()


#print(f"Finished deleting local images and videos for '{game}'\n")

print("---------------------\n")
print("SCRAPING PROCESS FINISHED")
