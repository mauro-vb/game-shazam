import os
from pytube import YouTube
import get_frames
from delete_data import delete_img, delete_vid
from snake_case import snake
from get_vid_ids import get_ids
from isoduration import parse_duration

### MAIN ###

# Admin input, comes from YTscrape script:
def main(game:str,n_videos:int,cloud=False):
    game = game
    n_videos = n_videos
    cloud = False
    max_duration = parse_duration('PT20H').time

    # Creating video id list:
    print("\n")
    id_list,len_list = get_ids(game)
    id_list = id_list[:n_videos] # to correct: should limit no. of videos in funct, not at this stage
    len_list = len_list[:n_videos]
    print(f"Downloading and performing image extraction on {n_videos} videos:\n")

    # Snake Case for use in folder names later:
    game_snk = snake(game)

    vid_path = os.path.join(os.getcwd(),'data','tmp','')
    img_path = os.path.join(os.getcwd(),'data','scraped',game_snk,'')

    # Check if it exists
    itExist = os.path.exists(img_path)
    if not itExist:
        # Create a new directory because it does not exist
        os.makedirs(img_path)
        print(f"New directory created for {game} images.\n")


    # Downloading video and extracting frames for each downloaded video
    id_len_dict = dict(zip(id_list,len_list))

    for key,value in id_len_dict.items():

        duration = parse_duration(value)
        if int(duration.time.hours) < (max_duration.hours):
            count_videos = 1
            try:
                print(f"Downloading video {key}...\t\t{count_videos}/{n_videos}\n")
                yt = YouTube(f'https://www.youtube.com/watch?v={key}')
                yt.streams.filter(
                    progressive=True,
                    file_extension='mp4').order_by('resolution').asc().first().download(
                        output_path = vid_path,
                        filename=f'{game_snk}_{key}.mp4',
                        skip_existing = True, timeout = None, max_retries = 0)

                        # Ordered by resolution, taking just the first, no timeout
                        # These features could be changed by admin if needed

                print("Extracting frames...\n")
                get_frames.extract_frames(f"{vid_path}{game_snk}_{key}.mp4",
                                        img_path, ident=key, gamename=game)
                count_videos += 1


            except:
                continue

    if cloud == True:

        print("You have selected 'upload to cloud' instantly.")
        print("Feature unfinished. Will delete files without uploading.")
        print("Please interrupt.")
        breakpoint()

        # Call upload_img: bucket creation, uploading, etc.
        #print(f"Finished uploading '{game}' images to Google Cloud\n")


        # Call delete_data: delete local images and videos.
        delete_vid(path=vid_path)
        delete_img(path=img_path)
        print(f"\nFinished deleting local images and videos for '{game}'.\n")

    else:

        #CALL delete_data: delete local images videos, keep images
        delete_vid(path=vid_path)
        print(f"Finished deleting local videos for '{game}'. Kept images.\n")

    print("---------------------\n")
    print("SCRAPING PROCESS FINISHED")


games = ['among us',
         'apex legends',
         'fortnite',
         'forza horizon',
         'free fire',
         'genshin impact',
         'minecraft',
         'roblox',
         'terraria'
         ]

speed_games = ['god of war']

main('gta',1)
# for game in games:
#     main(game,5)
