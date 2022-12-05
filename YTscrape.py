from interface_yts.clear_screen import clear
from interface_yts.help_about import help_call
from readchar import readkey, key
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
        print("        PRESS 'S' TO START, 'E' TO EXIT")
    elif keypress1 == "s":
        break
    elif keypress1 == "e":
        os._exit(1)

# DO THE MAIN PROGRAM
clear()
print("\n")
print("Press 'K' to enter your Youtube Data API key, 'D' to use the default one.")
print("For more information on Youtube API keys, please check the Help function in the main menu.")
print("\n")

while True:
    keypress2 = readkey()
    if keypress2 == "k":
        print("\n")
        user_api_key = input("Enter your API key: ")
        print("Feature not implemented")
        os._exit(1)
    elif keypress2 == "d":
        break


# USER INPUTS GAME LIST
# print("\n")
# print("Enter a list of titles to retrieve screenshots from, separated by commas, as such:")
# print("'Fortnite, Plants vs. Zombies 2, Minecraft, Counter Strike: Global Offensive,'")
# print("(Warning! For better performance, do not exceed 4 titles)")
# print("\n")
# input_string = input()
# game_list = input_string.split(",")
# game_list = [game.strip() for game in game_list]

# OTHER INPUT METHOD
# print("\n")
# print("Prompt: nombre y enter, dos enter para terminar")
# print("(Warning! For better performance, do not exceed 4 titles)")
# while True:
#     inp_list = []
#
#     try:
#
#         inp = input()
#         inp_list.append(inp)
#         keypress3 = readkey()
#        if keypress3 == key.ENTER:
#             break
# poner except?
# luego imprimir la lista para ver que onda, poner mensaje de comprbacion tipo 'esta es tu lista'




## VERSION NUEVA, POST MAURO:
# Promtear al usuario para que pase una lista de juegos, poner "warning! no pasar mas de 3 o 4"
# que apriete enter cada vez que termine, y que al poner enter dos veces (o sea no text
# en la ultima linea o algo asi, se considere al lista cerrada.

# please input your query: (examples "gamplay, gamplay no commentary, speedrun, etc")

# how many captures do you want per game? (current training set: 10k)
# how many frames per minute? recommended --> 10 (one each 6 seconds)

# do you want to set a special path for your data (y/n)
# otherwise your data will be saved to
# mostrar el path

# number of seconds to trim (from beginning AND end):

# please confirm your settings: mostrar todas las variables
# press s to start scraping, o to start over

# parameters saved at the end? checke if is better to save them at end or send them to other file

# GAMES = ["Age of Empires 2 de"] ## I recommend 2 or 3 per run (you can have multiple instances running)
# FRAMES_PER_V = 1000
# FRAMES_PER_G = 10000
# MAX_DURATION = 5
# API_KEY = "AIzaSyAWT_IeNUwTTDs5IK389or1YKJlukCA8FU"
# FRAMES_PER_MINUTE = 8
# VID_PATH = os.path.join(os.getcwd(),'data','tmp','')
# FRAMES_PATH = os.path.join(os.getcwd(),'data','scraped')
# VID_CROPPING = 120000 # in miliseconds (edited)
