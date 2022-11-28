import os
import cv2
from matplotlib.pyplot import imread

def data_resizer(path,size):
    '''
    Function loading our data into image and target
    '''
    resize_folder = f'resized_({size[0]},{size[1]})'

    nb_imgs = 1100

    os.mkdir(os.path.join(path,resize_folder))

    folders  = ['AmongUs','ApexLegends',
                'Fortnite','ForzaHorizon',
                'FreeFire','GenshinImpact',
                'GodofWar','Minecraft',
                'Roblox', 'Terraria']

    for f in folders:

        game_folder = os.path.join(path,resize_folder,f)

        os.mkdir(game_folder)

        for i in range(nb_imgs):

            try:

                img_path = os.path.join(path, 'original', f, f'image_{i}.png')

                n_img_path = os.path.join(game_folder, f'image_{i}.png')

                image = imread(img_path)[:, :, :3]

                resized_image = resize(image,size)

                cv2.imwrite(n_img_path,resized_image*265)

            except:
                print(os.path.join(path, f, f'image_{i}.png'), ' is missing!')

    return None
