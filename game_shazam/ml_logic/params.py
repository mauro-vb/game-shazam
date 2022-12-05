import os

GAMES_DICT  = {'Dead by deadlight': 0,
               'Dota 2': 1,
               'Fortnite': 2,
               'Forza Horizon': 3,
               'Hearthstone': 4,
               'Minecraft': 5,
               'Rocket League': 6
            }

IMG_SIZE = (224,224)
IMG_VECTOR = (224,224,3)

LOCAL_DATA_PATH = os.path.expanduser(os.environ.get("LOCAL_DATA_PATH"))
LOCAL_REGISTRY_PATH = os.path.expanduser(os.environ.get("LOCAL_REGISTRY_PATH"))

N_CATS = os.path.expanduser(os.environ.get("N_CATS"))
