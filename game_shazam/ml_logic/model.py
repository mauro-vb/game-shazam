from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.callbacks import EarlyStopping
from game_shazam.ml_logic.params import IMG_VECTOR, N_CATS
from tensorflow.keras.applications.vgg16 import VGG16

def initialize_model():
    '''Initialize Neural Network'''

    print('\n   INITIALIZING MODEL\n')

    model = models.Sequential()

    ### Convolution & MaxPooling
    # 1
    model.add(layers.Conv2D(16, kernel_size=4, activation='relu', padding='same', input_shape=IMG_VECTOR))
    model.add(layers.MaxPool2D(pool_size=(2, 2)))
    # 2
    model.add(layers.Conv2D(32, kernel_size=3, padding='same', activation='relu'))
    model.add(layers.MaxPool2D(pool_size=(2, 2)))
    # 3
    model.add(layers.Conv2D(64, kernel_size=3, padding='same', activation='relu'))
    #model.add(layers.Conv2D(64, kernel_size=3, padding='same', activation='relu'))
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
    model.add(layers.Dense(N_CATS, activation='softmax'))

    return model

def compile_model(model, learning_rate=0.001):
    '''
    Compile the neural network
    '''
    print('\n   COMPILING MODEL\n')
    optimizer = optimizers.Adam(learning_rate=learning_rate)
    model.compile(loss='categorical_crossentropy',optimizer=optimizer,metrics=['accuracy'])
    return model

def train_model(model,
                data_generator,
                val_generator,
                patience=25,
                epochs=150,
                steps_per_epoch=2):
    """
    Fit model and return a the tuple (fitted_model, history)
    """
    print('\n   TRAINING MODEL\n')
    es = EarlyStopping(monitor='accuracy',
                       patience=patience,
                       restore_best_weights=True,)

    history = model.fit(data_generator,
                        validation_data=val_generator,
                        steps_per_epoch=steps_per_epoch,
                        validation_steps=2,
                        epochs=epochs,
                        verbose=1,
                        callbacks=[es])
    print('\n   MODEL WAS TRAINED\n')
    return model, history

def evaluate_data_gen(model,data_gen):
    '''Evaluates model through a data generator'''


    metrics = model.evaluate(data_gen,
                             verbose=1,
                             return_dict=True)

    loss = metrics["val"]
    accuracy = metrics["accuracy"]

    print(f"\n✅ model evaluated: loss {round(loss, 2)} mae {round(accuracy, 2)}")

    return metrics

def initialize_VGG16_model(trainable=True):

    model = VGG16(weights="imagenet", include_top=False, input_shape=IMG_VECTOR)
    model.trainable = trainable
    flatten_layer = layers.Flatten()
    dense_layer = layers.Dense(200, activation='relu')
    prediction_layer = layers.Dense(N_CATS, activation='softmax')


    model = models.Sequential([
        model,
        flatten_layer,
        dense_layer,
        prediction_layer
    ])

    return model

def initialize_big_model(trainable=True):

    print('\n   INITIALIZING MODEL\n')

    model = VGG16(weights="imagenet", include_top=False, input_shape=IMG_VECTOR)
    model.trainable = trainable

    model = models.Sequential()

    ### Convolution & MaxPooling
    # 1
    model.add(layers.Conv2D(16, kernel_size=4, activation='relu', padding='same', input_shape=IMG_VECTOR))
    model.add(layers.MaxPool2D(pool_size=(2, 2)))
    # 2
    model.add(layers.Conv2D(32, kernel_size=3, padding='same', activation='relu'))
    model.add(layers.MaxPool2D(pool_size=(2, 2)))
    # 3
    model.add(layers.Conv2D(64, kernel_size=3, padding='same', activation='relu'))
    #model.add(layers.Conv2D(64, kernel_size=3, padding='same', activation='relu'))
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
    model.add(layers.Dense(N_CATS, activation='softmax'))

    return model
