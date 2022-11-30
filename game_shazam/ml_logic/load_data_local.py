import os
from matplotlib.pyplot import imread
import numpy as np

def load_data(path, data_folder = 'raw'):
    '''
    Function loading our data into image and target
    '''

    folders  = ['AmongUs','ApexLegends',
                'Fortnite','ForzaHorizon',
                'FreeFire','GenshinImpact',
                'GodofWar','Minecraft',
                'Roblox', 'Terraria']

    X, y = [], []

    for f in folders:
        print(f'Fetching {f} images...')
        for filename in os.listdir(f):

            try:
                n_path = os.path.join(path, data_folder, f, filename)

                X.append(imread(n_path)[:, :, :3])

                y.append(f)

            except:
                pass

    return np.array(X), np.array(y).reshape(-1,1)
