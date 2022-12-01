
from pytube import YouTube
import time
import os

def save_video_locally(vid_id:str,vidPath:str) -> str:
    '''
    Saves video onto specified repository
    '''
    start_time = time.time()
    filename = f'{vid_id}.mp4'

    print(f"\nDownloading video {vid_id}...\n")

    yt = YouTube(f'https://www.youtube.com/watch?v={vid_id}')

    yt.streams.filter(progressive=True,
                      file_extension='mp4').order_by('resolution').asc().first(
                          ).download(
                              output_path = vidPath,
                              filename=filename,
                              skip_existing = True,
                              timeout = None,
                              max_retries = 0)

    print(f'Video {vid_id} succesfully downloaded (time: {time.time() - start_time})')

    return None

def delete_video(vid_path:str) -> None:
    '''
    Deletes file given its path
    '''
    os.remove(vid_path)

    return None
