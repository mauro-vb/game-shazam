import random as rd
import cv2
import os
from scraping_2.params import FRAMES_PER_MINUTE, VID_CROPPING

def extract_frames(vid_path:str,frames_path:str,vid_id:str,vid_duration):
    '''
    saves frames from a video path,
    saving it as id of video
    and returns number of frames extracted
    '''

    path_to_vid = os.path.join(vid_path,f'{vid_id}.mp4')
    vidcap = cv2.VideoCapture(path_to_vid)

    start = VID_CROPPING
    end = vid_duration * 1000 - VID_CROPPING

    n_samples = int((vid_duration / 60) * FRAMES_PER_MINUTE)

    frames = rd.sample(range(start,end+1),n_samples)
    count = 0

    for f in frames:
        try:
            vidcap.set(cv2.CAP_PROP_POS_MSEC, f)
            _,image = vidcap.read()
            cv2.imwrite(frames_path + f"{vid_id}_frame%d.jpg" % count, image)
            count += 1
        except:
            continue

    print(f"Finished extracting {count} frames from video of {vid_duration} seconds.\n@ {frames_path}\n")

    return count
