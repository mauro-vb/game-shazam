
from pytube import YouTube
import time
import os
from scraping_2.params import FRAMES_PATH
import fnmatch
import sys

# def progress(chunk: bytes, bytes_remaining: int):
#     print("got into function")
#     contentsize = chunk.filesize
#     size = contentsize - bytes_remaining

#     print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
#     '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')


def save_video_locally(vid_id:str,vidPath:str,game_name:str) -> str:
    '''
    Saves video onto specified repository
    '''
    downloaded = False
    start_time = time.time()
    filename = f'{vid_id}.mp4'
    if any(fnmatch.fnmatchcase(file, vid_id + '*.jpg') for file in os.listdir(os.path.join(FRAMES_PATH,game_name))):
        print(vid_id, ' was already in folder.\n')


    else:
        print("---------------------\n")
        print(f"Downloading video {vid_id}...\n")
        yt = YouTube(f'https://www.youtube.com/watch?v={vid_id}')

        downloaded = False
        while downloaded == False:
            try:
                #get filesize externally
                # file_size = yt.streams.filter(progressive=True,
                # file_extension='mp4').order_by('resolution').asc().first(
                #     ).filesize

                #actually download
                video = yt.streams.filter(progressive=True,
                                file_extension='mp4').order_by('resolution').asc().first()

                video.download(output_path = vidPath,
                                        filename=filename,
                                        skip_existing = True,
                                        timeout = None,
                                        max_retries = 0)

                print(f'Succesfully downloaded {vid_id} (time: {time.time() - start_time})\n')
                downloaded = True
            except:
                print(f"Error downloading {vid_id}. Moving to next one if possible.\n")
                pass

    return downloaded

def delete_video(vid_path:str, vid_id:str) -> None:
    '''
    Deletes file given its path
    '''

    path_to_vid = os.path.join(vid_path,f'{vid_id}.mp4')

    try:
        os.remove(path_to_vid)
        print(f'Removed video successfully (id: {vid_id})\n')
    except:
        print(f'Could not remove video (id: {vid_id})\n')
        pass

    return None
