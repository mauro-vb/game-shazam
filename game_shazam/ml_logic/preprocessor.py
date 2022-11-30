from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
from skimage.transform import resize
from game_shazam.ml_logic.params import GAMES_DICT, IMG_SIZE, IMG_VECTOR
import os
import cv2
from keras.utils import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input

data_gen = ImageDataGenerator()

def get_data_generator(path:str,
                       #rescale=1./10,
                       #rotation_range=40,
                       #width_height_shift=0.3,
                       #shear_zoom_range=0.2,
                       #validation_split=0.3,
                       #fill_mode='nearest',
                       batch_size=16,
                       target_size=IMG_SIZE
                       ):
    '''Get data generator to train on'''
    print('\n   GETTING DATA GENERATOR\n')

    data_generator = data_gen.flow_from_directory(
        path,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical')

    return data_generator

def get_val_generator(path:str,
                    #    rescale=1./10,
                    #    rotation_range=40,
                    #    width_height_shift=0.3,
                    #    shear_zoom_range=0.2,
                    #    fill_mode='nearest',
                       batch_size=32,
                       target_size=IMG_SIZE):

    data_generator = data_gen.flow_from_directory(
        path,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical')

    print('\n   GOT A VAL SET DATA GENERATOR\n')

    return data_generator

def preprocess_features(path:str):

    data = []

    for f in GAMES_DICT.values:
        print(f'Fetching {f} images...')
        for filename in os.listdir(f):

            n_path = os.path.join(path, f, filename)
            img = cv2.imread(n_path)
            data.append(img)

    resize_v = np.vectorize(resize(IMG_VECTOR))
    data = resize_v(np.array(data))

    print('\n   DATA HAS BEEN PREPROCESSED\n')
    return data

def prep_for_pred(path:str):

    my_image = load_img(path, target_size=IMG_SIZE)
    #preprocess the image
    my_image = img_to_array(my_image)
    my_image = my_image.reshape((1, my_image.shape[0], my_image.shape[1], my_image.shape[2]))
    my_image = preprocess_input(my_image)

    return my_image
