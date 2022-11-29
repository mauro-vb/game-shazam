from pytube import YouTube
import extract_frames
from get_vid_ids import get_ids

### MAIN ###

# Admin input:
game = "Assasin's Creed"
n_videos = 3

# Creating video id list:
print("\n")
id_list = get_ids(game)
id_list = id_list[:n_videos] # to correct: should limit no. of videos in funct, not at this stage

# Downloading video and extracting frames for each downloaded video
for each in id_list:

    try:
        print(f"Trying video {each}...\n")
        yt = YouTube(f'https://www.youtube.com/watch?v={each}')
        yt.streams.filter(
            progressive=True,
            file_extension='mp4').order_by('resolution').asc().first().download(
                output_path = 'temp_videos',filename=f'{game}_{each}.mp4',
                skip_existing = True, timeout = None, max_retries = 0)

                # Ordered by resolution, taking just the first, no timeout
                # These features could be changed by admin if needed

        print("Extracting frames...\n")
        extract_frames(f'temp_videos/{game}_{each}.mp4', f'frames/{game}/{game}', ident=each)
        print("---------------------\n")
        print(f"Finished generating images for '{game}' gameplay")

    except:
        continue
