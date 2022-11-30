import os

GAMES_DICT  = {
    0: 'AmongUs',
    1: 'ApexLegends',
    2: 'Fortnite',
    3: 'ForzaHorizon',
    4: 'FreeFire',
    5: 'GenshinImpact',
    6: 'GodofWar',
    7: 'Minecraft',
    8: 'Roblox',
    9: 'Terraria'
    }

IMG_SIZE = (224,224)
IMG_VECTOR = (224,224,3)

LOCAL_DATA_PATH = os.path.expanduser(os.environ.get("LOCAL_DATA_PATH"))
LOCAL_REGISTRY_PATH = os.path.expanduser(os.environ.get("LOCAL_REGISTRY_PATH"))

N_CATS = os.path.expanduser(os.environ.get("N_CATS"))
