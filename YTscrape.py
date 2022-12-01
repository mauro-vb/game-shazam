from scraping.clear_screen import clear

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
