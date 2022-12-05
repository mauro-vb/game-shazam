from interface_yts.clear_screen import clear
from interface_yts.help_about import help_call
from interface_yts.fauxbar import animation
from interface_yts.clean_inputs import no_empty, only_num
from interface_yts.under_construction import underconstr
from readchar import readkey, key
from scraping_2.main import scrape
import os

clear()
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

print("\n\n\n")
print("        PRESS 'S' TO START, 'H' FOR HELP/ABOUT")
print("        OR 'E' TO EXIT")
print("\n\n\n")

# START or HELP
while True:
    keypress1 = readkey()
    if keypress1 == "h":
        help_call()
        print("Press 'S' to start, 'E' to exit.")
    elif keypress1 == "s":
        break
    elif keypress1 == "e":
        clear()
        os._exit(1)

# DO THE MAIN PROGRAM
clear()
print("Press 'K' to enter your Youtube Data API key, 'D' to use the default one.")
print("For more information on Youtube API keys, please check the Help function in the main menu.")
print("\n")

while True:
    keypress2 = readkey()
    if keypress2 == "k":
        user_api_key = input("Enter your API key: ")
        clear()
        underconstr()
        print("\nFeature under construction. \n")
        os._exit(1)
    elif keypress2 == "d":
        user_api_key = os.environ.get("YOUTUBE_API_KEY")
        break

# USER INPUTS GAME LIST
print('''Enter a list of titles to retrieve screenshots from.
Press ENTER after each title. Input a single asterisk ("*") to finish.
(Warning! For better performance, do not exceed 4 titles)''')
print("\n")

inp_list = []
while True:
    prompt = "==> "
    inp = input(prompt)
    if inp == "*":
        break
    else:
        inp_list.append(inp)

clear()

# Clean inp list of empty values
inp_list = no_empty(inp_list)

print(f"Your list of games is: {inp_list}\n")

# OTHER INPUT METHOD
# print("Enter a list of titles to retrieve screenshots from, separated by commas, as such:")
# print("'Fortnite, Plants vs. Zombies 2, Minecraft, Counter Strike: Global Offensive,'")
# print("(Warning! For better performance, do not exceed 4 titles)")
# print("\n")
# input_string = input()
# game_list = input_string.split(",")
# game_list = [game.strip() for game in game_list]

# USER INPUTS QUERY

print('''Please enter a query to perform the search.
For example: 'gameplay', 'gameplay no commentary', 'speedrun', etc.:  ''')
print("\n")
user_query = input()
print("\n")
print("How many frame captures per game?  ")
frames_per_game = int(only_num(input("(Current dataset average is 10 000):  ")))
print("\n")
print("How many frames per minute?  ")
frames_per_minute = int(only_num(input("(Current dataset average is 8):  ")))
print("\n")
vid_cropping = int(only_num(input("Enter number of seconds to trim from both\nthe beginning and the end of each video:  ")))
vid_cropping = vid_cropping*1000
print("\n")
upper_limit = int(only_num(input("Enter max lenght of video (in hs) to extract frames from: ")))
print("\n")
print("Do you want to set a specific path to save your data (Y/N)?")
print(f"Otherwise it will be saved to: '{os.path.join(os.getcwd(),'data')}'")
print("\n")

while True:
    keypress5 = readkey()
    if keypress5 == "y":
        gen_path = input("Enter a path to save your data: ")
        customized_vid_path = os.path.join(gen_path, 'tmp')
        customized_frames_path = os.path.join(gen_path, 'scraped')
    elif keypress5 == "n":
        gen_path = os.path.join(os.getcwd(),'data')
        break

clear()
print("Ready for scraping. Your current settings are:")
print("\n")
print(f"Titles: \t\t\t\t {inp_list}")
print(f"Query: \t\t\t\t\t '{user_query}'")
print(f"Frames per game: \t\t\t {frames_per_game}")
print(f"Frames per minute: \t\t\t {frames_per_minute}")
print(f"Trimming (beginning and end): \t\t {vid_cropping/1000}s")
print(f"Path: \t\t\t\t\t {gen_path}")
print("\n")
print("To start scraping, press 'S'. To start over, press 'O'")

while True:
    keypress6 = readkey()
    if keypress6 == "o":
        clear()
        underconstr()
        print("\nFeature under construction. \n")
        os._exit(1)
    elif keypress6 == "s":
        clear()
        break

# CALLING SCRAPE FUNCTION FROM MAIN with faux animation
print("Preparing to scrape...")
animation()
clear()

scrape_again = True

while True:

    scrape(
        games = inp_list,
        query = user_query,
        frames_per_g = frames_per_game,
        max_duration = upper_limit,
        api_key = user_api_key,
        frames_per_minute = frames_per_minute,
        vid_path = os.path.join(os.getcwd(),'data','tmp'),
        frames_path = os.path.join(os.getcwd(),'data','scraped'),
        vid_cropping = vid_cropping)

    print(f'''You can check your files at:
    {gen_path}\n''')
    print("Do you wish to scrape again with the same settings? (Y/N)")
    keypress7 = readkey()
    if keypress7 == "y":
        clear()
    elif keypress7 == "n":
        print("\n")
        break

os._exit(1)
