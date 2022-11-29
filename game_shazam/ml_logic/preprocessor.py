from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
from skimage.transform import resize
from game_shazam.ml_logic.params import GAMES_DICT, IMG_SIZE, IMG_VECTOR
import os
import cv2


def get_data_generator(path:str,
                       rescale=1.5/10,
                       rotation_range=40,
                       width_height_shift=0.3,
                       shear_zoom_range=0.2,
                       validation_split=0.3,
                       fill_mode='nearest',
                       batch_size=32,
                       target_size=IMG_SIZE
                       ):
    '''Get data generator to train on'''
    print('\n   GETTING DATA GENERATOR\n')

    # Apply data augmentation
    datagen = ImageDataGenerator(
        rescale=rescale,
        rotation_range=rotation_range,
        width_shift_range=width_height_shift,
        height_shift_range=width_height_shift,
        shear_range=shear_zoom_range,
        zoom_range=shear_zoom_range,
        validation_split=validation_split,
        fill_mode=fill_mode)

    data_generator = datagen.flow_from_directory(
        path,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical')

    return data_generator

def get_test_generator(path:str,
                       rescale=1.5/10,
                       rotation_range=40,
                       width_height_shift=0.3,
                       shear_zoom_range=0.2,
                       fill_mode='nearest',
                       batch_size=32,
                       target_size=IMG_SIZE):

    datagen = ImageDataGenerator(
        rescale=rescale,
        rotation_range=rotation_range,
        width_shift_range=width_height_shift,
        height_shift_range=width_height_shift,
        shear_range=shear_zoom_range,
        zoom_range=shear_zoom_range,
        fill_mode=fill_mode)

    data_generator = datagen.flow_from_directory(
        path,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical')

    print('\n   GOT A TEST SET DATA GENERATOR\n')

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
