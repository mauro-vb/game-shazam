from googleapiclient.discovery import build
from isoduration import parse_duration
from scraping_2.params import API_KEY


def get_duration(video_id:str) -> int:
    '''
    Returns length in seconds of a youtube video given its id
    '''

    youtube = build('youtube', 'v3',developerKey=API_KEY)

    response = youtube.videos().list(id=id,
                                      part='contentDetails').execute()

    length = parse_duration(response['items'][0]['contentDetails']['duration'])

    # Getting lenght in seconds
    length = length.time.hours * 3600 + length.time.minutes * 60 + length.time.seconds

    return length
