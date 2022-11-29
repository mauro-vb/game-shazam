from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
from skimage.transform import resize
from ml_logic.params import GAMES_DICT
import os


def get_data_generator(path:str,
                       rescale=1.5/10,
                       rotation_range=40,
                       width_height_shift=0.3,
                       shear_zoom_range=0.2,
                       brightness_range=0.0,
                       validation_split=0.3,
                       fill_mode='nearest',
                       batch_size=32,
                       target_size=(224,224)
                       ):
    '''Get data generator to train on'''
    # Apply data augmentation
    datagen = ImageDataGenerator(
        rescale=rescale,
        rotation_range=rotation_range,
        width_shift_range=width_height_shift,
        height_shift_range=width_height_shift,
        shear_range=shear_zoom_range,
        zoom_range=shear_zoom_range,
        brightness_range=brightness_range,
        validation_split=validation_split,
        fill_mode=fill_mode)

    data_generator = datagen.flow_from_directory(
        path,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical')

    return data_generator

def preprocess_features(path:str):

    for f in GAMES_DICT.values:
        print(f'Fetching {f} images...')
        for filename in os.listdir(f):

            n_path = os.path.join(path, f, filename)


    X_preprocessed = None

    return X_preprocessed
