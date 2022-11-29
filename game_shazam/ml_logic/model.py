from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator

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

def initialize_model():
    '''Initialize Neural Network'''

    model = models.Sequential()

    ### Convolution & MaxPooling
    # 1
    model.add(layers.Conv2D(16, kernel_size=4, activation='relu', padding='same', input_shape=(224, 224, 3)))
    model.add(layers.MaxPool2D(pool_size=(2, 2)))
    # 2
    model.add(layers.Conv2D(32, kernel_size=3, padding='same', activation='relu'))
    model.add(layers.MaxPool2D(pool_size=(2, 2)))
    # 3
    model.add(layers.Conv2D(64, kernel_size=3, padding='same', activation='relu'))
    model.add(layers.Conv2D(64, kernel_size=3, padding='same', activation='relu'))
    model.add(layers.MaxPool2D(pool_size=(2, 2)))
    # 4
    model.add(layers.Conv2D(128, kernel_size=2, activation='relu'))
    model.add(layers.MaxPool2D(pool_size=(2, 2)))

    ### Flattening
    model.add(layers.Flatten())

    ### One Fully Connected layer - "Fully Connected" is equivalent to saying "Dense"
    model.add(layers.Dense(100, activation='relu'))

    model.add(layers.Dense(50, activation='relu'))

    ### Last layer - Classification
    model.add(layers.Dense(10, activation='softmax'))

    return model

def compile_model(model, learning_rate=0.01):
    '''
    Compile the neural network
    '''
    optimizer = optimizers.Adam(learning_rate=learning_rate)
    model.compile(loss='categorical_crossentropy',optimizer=optimizer,metrics=['accuracy'])
    return model

def train_model(model,
                data_generator,
                patience=2,
                epochs=150,
                steps_per_epoch=2):
    """
    Fit model and return a the tuple (fitted_model, history)
    """
    es = EarlyStopping(monitor='accuracy',
                       patience=patience,
                       restore_best_weights=True)

    history = model.fit(data_generator,
                        steps_per_epoch=steps_per_epoch,
                        epochs=epochs,
                        verbose=1,
                        callbacks=[es])

    return model, history
