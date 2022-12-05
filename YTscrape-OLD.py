from scraping_2.clear_screen import clear

print("\n\n\n")
print('''
 ██████╗  █████╗ ███╗   ███╗███████╗        ███████╗██╗  ██╗ █████╗ ███████╗ █████╗ ███╗   ███╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝        ██╔════╝██║  ██║██╔══██╗╚══███╔╝██╔══██╗████╗ ████║
██║  ███╗███████║██╔████╔██║█████╗          ███████╗███████║███████║  ███╔╝ ███████║██╔████╔██║
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝          ╚════██║██╔══██║██╔══██║ ███╔╝  ██╔══██║██║╚██╔╝██║
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗        ███████║██║  ██║██║  ██║███████╗██║  ██║██║ ╚═╝ ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝        ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                                                ''')

print('''
+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+
|Y|O|U|T|U|B|E| |S|C|R|A|P|E|R| |T|O|O|L|
+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+
''')

print("\n\n")

game = input("Enter name of the game: ")
print("\n")
clear()

query = input("Enter additional query, for example:'gameplay', 'gameplay no commentary', 'speedrun', etc: ")
print("\n")

n_videos = input("Enter number of videos to download: ") #LIMIT TO INT
print("\n")

max_lenght = input("Enter maximum video lenght in minutes: ") #LIMIT TO INT
print("\n")

img_per_vid = input("Enter number of images per video: ") #LIMIT TO INT
print("\n")

# CREATE CORRECT FLOW OF IFS

img_total = input("Enter total number of images desired: ") #LIMIT TO INT
print("\n")

method = input("Choose method to capture images: Enter 'random' for random sampling, 'seconds' to capture a frame every X seconds: ")
print("\n") #LIMIT TO THOSE CHOICES

interval = input("Enter number of interval seconds between frame captures: ")
print("\n") #LIMIT TO INT

locloud = input("Type 'local' if you want to save the images locally, 'cloud' to save them to Google Cloud: ")
print("\n\n") #LIMIT TO THOSE CHOICES


## VERSION NUEVA, POST MAURO:

# press S to start, H for help / about
# en help ponemos 'game shazam' v1.0 by nuestros nombres
# y abajo una explicacion de que es y como funciona muy resumidamente
# luego press S to start, Q to quit

# Promtear al usuario para que pase una lista de juegos, poner "warning! no pasar mas de 3 o 4"
# que apriete enter cada vez que termine, y que al poner enter dos veces (o sea no text
# en la ultima linea o algo asi, se considere al lista cerrada.

# please input your query: (examples "gamplay, gamplay no commentary, speedrun, etc")

# how many captures do you want per game? (current training set: 20k)
# how many frames per minute? recommended --> 10 (one each 6 seconds)

# do you want to set a special path for your data (y/n)
# otherwise your data will be saved to

# number of seconds to trim (from beginning AND end):


GAMES = ["Age of Empires 2 de"] ## I recommend 2 or 3 per run (you can have multiple instances running)
FRAMES_PER_V = 1000
FRAMES_PER_G = 10000
MAX_DURATION = 5
API_KEY = "AIzaSyAWT_IeNUwTTDs5IK389or1YKJlukCA8FU"
FRAMES_PER_MINUTE = 8
VID_PATH = os.path.join(os.getcwd(),'data','tmp','')
FRAMES_PATH = os.path.join(os.getcwd(),'data','scraped')
VID_CROPPING = 120000 # in miliseconds (edited)
