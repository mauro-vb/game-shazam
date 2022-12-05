from scraping_2.duration import get_duration
from googleapiclient.discovery import build
from scraping_2.params import API_KEY

def get_ids(game: str) -> list:
    '''
    Returns a list of video ids to call later
    '''

    print(f"Retrieving video IDs for '{game}'...\n")

    ids = []

    # creating youtube resource object
    youtube = build('youtube', 'v3',developerKey=API_KEY)

    # retrieve youtube video results
    response=youtube.search().list(
        part='snippet',
        maxResults='50',
        #order='title',
        q=f'{game}').execute()

    #breakpoint()
    while response:
        for item in response['items']:
            try:
                vid_id = item['id']['videoId']
                ids.append(vid_id)
            except:
                continue
        break
    print(f"\nFinished retrieving IDs for '{game}'.\n")
    print("---------------------\n")

    return ids
