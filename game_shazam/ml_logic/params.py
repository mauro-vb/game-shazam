import os

GAMES_DICT  = {'Age of Empires 2': 0,
 'Among Us': 1,
 'Apex Legends': 2,
 'Borderlands 2': 3,
 'Counter-Strike: Global Offensive': 4,
 'Cuphead': 5,
 'Dead by Daylight': 6,
 'Dota 2': 7,
 'Fall Guys': 8,
 'Fifa 23': 9,
 'Fortnite': 10,
 'Forza Horizon': 11,
 'Genshin Impact': 12,
 'God of War': 13,
 'Grand Theft Auto V': 14,
 'Hades': 15,
 'Halo Infinite': 16,
 'Hearthstone': 17,
 'Inscryption': 18,
 'League of Legends': 19,
 'Mario Kart 8': 20,
 'Minecraft': 21,
 'Mortal Kombat 11': 22,
 'Overwatch 2': 23,
 'Potionomics': 24,
 'Red Dead Redemption': 25,
 'Rocket League': 26,
 'Skyrim': 27,
 'Slay The Spire': 28,
 'Splatoon 2': 29,
 'Stardew Valley': 30,
 'Street Fighter': 31,
 'Super Auto Pets': 32,
 'Super Smash Bros Ultimate': 33,
 'Terraria': 34,
 'Team Fight Tactics': 35,
 'Valorant': 36,
 'World of Warcraft': 37}

IMG_SIZE = (224,224)
IMG_VECTOR = (224,224,3)

LOCAL_DATA_PATH = os.path.expanduser(os.environ.get("LOCAL_DATA_PATH"))
LOCAL_REGISTRY_PATH = os.path.expanduser(os.environ.get("LOCAL_REGISTRY_PATH"))

N_CATS = os.path.expanduser(os.environ.get("N_CATS"))
