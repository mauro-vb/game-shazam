import os
from scraping_2.video_ids import get_ids
from scraping_2.sampling import extract_frames
from scraping_2.vid_downloader import save_video_locally, delete_video
from scraping_2.params import GAMES, VID_PATH, FRAMES_PATH, FRAMES_PER_G

def main():

    # Iterate over list of games we want to scrape
    for game in GAMES:
        # get game IDs
        ids = get_ids(game)

        # define variables for each game
        snake_game = '_'.join(game.replace('_', ' ').split()).lower()
        current_frames = 0
        frames_foler = os.path.join(FRAMES_PATH,snake_game)

        # Iterate over ids to download, get frames and delete
        while FRAMES_PER_G < current_frames:
            for vid_id in ids:
                # download
                save_video_locally(vid_id,VID_PATH)
                # get frammes
                current_frames += extract_frames(vid_path=VID_PATH,frames_path=frames_foler)
                delete_video(VID_PATH)
        print('--------------------')
        print(f'\nDOWNLOADED {current_frames} FRAMES FOR {game}')

main()
