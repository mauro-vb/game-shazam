from scraping_2.duration import get_duration
import random as rd
import cv2
from scraping_2.params import FRAMES_PER_MINUTE

def extract_frames(vid_path:str,frames_path:str,vid_id:str):
    '''
    saves frames from a video path,
    saving it as id of video
    and returns number of frames extracted
    '''
    TWO_MINS = 12000
    vidcap = cv2.VideoCapture(vid_path)
    vid_duration = get_duration(vid_id)
    start = TWO_MINS
    end = vid_duration * 1000 - TWO_MINS

    frames = rd.sample(range(start,end+1),
                       (vid_duration / 60) * FRAMES_PER_MINUTE)
    count = 0

    for f in frames:
        count += 1
        try:
            vidcap.set(cv2.CAP_PROP_POS_MSEC, f)
            _,image = vidcap.read()
            cv2.imwrite(frames_path + f"{vid_id}_frame%d.jpg" % count, image)
        except:
            continue

    print("---------------------\n")
    print(f"Finished generating {count} images for video of {vid_duration} seconds.\n")

    return count
