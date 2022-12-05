import os
from scraping_2.video_ids import get_ids
from scraping_2.sampling import extract_frames
from scraping_2.vid_downloader import save_video_locally, delete_video
from scraping_2.duration import get_duration, seconds_to_hours
#from scraping_2.params import GAMES, VID_PATH, FRAMES_PATH, FRAMES_PER_G, MAX_DURATION

def scrape(
    games: list,
    query: str,
    frames_per_g: int,
    max_duration: int,
    api_key: str,
    frames_per_minute: int,
    vid_path: str,
    frames_path: str,
    vid_cropping: float):

    # Iterate over list of games we want to scrape
    for game in games:
        # get game IDs
        ids = get_ids(game=game,query=query, api_key=api_key)

        # define variables for each game
        snake_game = '_'.join(game.replace('_', ' ').split()).lower()

        frames_folder = os.path.join(frames_path,snake_game,'')

        itExist = os.path.exists(frames_folder)
        if not itExist:
        # Create a new directory because it does not exist
            os.makedirs(frames_folder)
            print(f"New directory created for {game} images.\n")

        indx = 0
        current_frames = len(os.listdir(os.path.join(frames_path,snake_game)))
        while frames_per_g > current_frames:

            c_id = ids[indx]
            c_duration = get_duration(c_id)

            if (seconds_to_hours(c_duration) < max_duration) and (seconds_to_hours(c_duration)>0.08):
                # download
                downloaded = save_video_locally(c_id,vid_path,snake_game)
                # get frames
                if downloaded:
                    current_frames += extract_frames(vid_path=vid_path,vid_id=c_id,frames_path=frames_folder,vid_duration=c_duration)
                    delete_video(vid_path,vid_id=c_id)

                else:
                    pass
            indx += 1

        print('--------------------\n')
        print(f"FINISHED SCRAPING WITH {current_frames} FRAMES FOR '{game}'\n")
