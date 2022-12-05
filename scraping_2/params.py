import os

GAMES = [
    'Mario Kart 8'
    ] ## I recommend 2 or 3 per run (you can have multiple instances running)
FRAMES_PER_V = 500
FRAMES_PER_G = 10000
MAX_DURATION = 10
API_KEY = 'AIzaSyDKDAE-T3VrvdN-r5yiGUPHHzf53f8yvCg'
FRAMES_PER_MINUTE = 8
VID_PATH = os.path.join(os.getcwd(),'data','tmp','')
FRAMES_PATH = os.path.join(os.getcwd(),'data','scraped')
VID_CROPPING = 12000 # in miliseconds
