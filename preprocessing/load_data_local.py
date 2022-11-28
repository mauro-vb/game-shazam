import os
from matplotlib.pyplot import imread

def load_data(path, raw_data_folder = 'raw', nb_imgs=1100):
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

        for i in range(nb_imgs):

            try:
                n_path = os.path.join(path,raw_data_folder, f, f'image_{i}.png')

                X.append(imread(n_path)[:, :, :3])

                y.append(f)

            except:
                print(os.path.join(path, f, f'image_{i}.png'), ' is missing!')

    return X, y
