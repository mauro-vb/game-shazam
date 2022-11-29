## API DOCS: https://developers.google.com/youtube/v3/docs
## BE CAREFUL WITH QUOTAS, LIMIT 10 000 PER DAY

from googleapiclient.discovery import build
import os

api_key = os.getenv('YOUTUBE_API_KEY')

def get_ids(game: str):
    '''returns a list of video ids to call later
    in the main function'''

    print(f"Retrieving video IDs for '{game}'...\n")

    # empty list for storing ids
    vid_ids = []

    # creating youtube resource object
    youtube = build('youtube', 'v3',developerKey=api_key)

    # retrieve youtube video results
    response=youtube.search().list(
    part='snippet',
    q=f'{game} gameplay'
    ).execute()
    count = 0

    # iterate video response
    while response:

		# extracting required info
		# from each result object
        count+=1
        for item in response['items']:

			# extracting ids
            id = item['id']['videoId']
            vid_ids.append(id)
            print(f"Got video ID: {id}")

		# repeat again
        if 'nextPageToken' in response and count < 2:
            response = youtube.search().list(
                    part='snippet',
                    q=f'{game} gameplay'
                    ).execute()
        else:
            break
    print(f"\nFinished retrieving IDs for '{game}'\n")
    print("---------------------\n")
    return vid_ids
