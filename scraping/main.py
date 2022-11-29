from pytube import YouTube
from pytube.cli import on_progress
import get_frames
from get_vid_ids import get_ids
# from PyQt5 import

# Not doing anything, call on_progress_callback=progress_funcin yt = Youtube
def progress_func(self, stream, chunk, file_handle, bytes_remaining):
    size = self.video.filesize
    progress = (float(abs(bytes_remaining-size)/size))*float(100)
    self.loadbar.setValue(progress)


### MAIN ###

# Admin input:
game = "csgo"
n_videos = 1

# Creating video id list:
print("\n")
id_list = get_ids(game)
id_list = id_list[:n_videos] # to correct: should limit no. of videos in funct, not at this stage
print(f"Downloading and performing image extraction on {n_videos} videos...\n")

# Downloading video and extracting frames for each downloaded video
for each in id_list:

    try:
        print(f"Downloading video {each}...\n")
        yt = YouTube(f'https://www.youtube.com/watch?v={each}', on_progress_callback=progress_func)
        yt.streams.filter(
            progressive=True,
            file_extension='mp4').order_by('resolution').asc().first().download(
                output_path = 'temp_videos',filename=f'{game}_{each}.mp4',
                skip_existing = True, timeout = None, max_retries = 0)

                # Ordered by resolution, taking just the first, no timeout
                # These features could be changed by admin if needed

        print("Extracting frames...\n")
        get_frames.extract_frames(f'temp_videos/{game}_{each}.mp4', f'imgs/{game}', ident=each)

    except:
        continue

print("---------------------\n")
print(f"Finished generating images for '{game}' gameplay")
