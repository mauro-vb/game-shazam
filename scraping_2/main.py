import os
from scraping_2.video_ids import get_ids
from scraping_2.sampling import extract_frames
from scraping_2.vid_downloader import save_video_locally, delete_video
from scraping_2.duration import get_duration, seconds_to_hours

from scraping_2.params import GAMES, VID_PATH, FRAMES_PATH, FRAMES_PER_G, MAX_DURATION

def main():

    # Iterate over list of games we want to scrape
    for game in GAMES:
        # get game IDs
        ids = get_ids(game)

        # define variables for each game
        snake_game = '_'.join(game.replace('_', ' ').split()).lower()

        frames_folder = os.path.join(FRAMES_PATH,snake_game,'')

        itExist = os.path.exists(frames_folder)
        if not itExist:
        # Create a new directory because it does not exist
            os.makedirs(frames_folder)
            print(f"New directory created for {game} images.\n")

        indx = 0
        current_frames = len(os.listdir(os.path.join(FRAMES_PATH,snake_game)))
        while FRAMES_PER_G > current_frames:

            c_id = ids[indx]
            c_duration = get_duration(c_id)

            if seconds_to_hours(c_duration) < MAX_DURATION:
                # download
                downloaded = save_video_locally(c_id,VID_PATH,snake_game)
                # get frammes
                if downloaded:
                    current_frames += extract_frames(vid_path=VID_PATH,vid_id=c_id,frames_path=frames_folder,vid_duration=c_duration)
                    delete_video(VID_PATH,vid_id=c_id)
                else:
                    pass

            indx += 1
        print('--------------------')
        print(f"\nDOWNLOADED {current_frames} FRAMES FOR '{game}'")

main()
