import os

GAMES_DICT  = {'Among Us': 0,
               'Apex Legends': 1,
               'Fortnite': 2,
               'Forza Horizon': 3,
               'Free Fire': 4,
               'Genshin Impact': 5,
               'God of War': 6,
               'Minecraft': 7,
               'Roblox': 8,
               'Terraria': 9
            }

IMG_SIZE = (224,224)
IMG_VECTOR = (224,224,3)

LOCAL_DATA_PATH = os.path.expanduser(os.environ.get("LOCAL_DATA_PATH"))
LOCAL_REGISTRY_PATH = os.path.expanduser(os.environ.get("LOCAL_REGISTRY_PATH"))

N_CATS = os.path.expanduser(os.environ.get("N_CATS"))
