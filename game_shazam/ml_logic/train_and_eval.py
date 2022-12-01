from game_shazam.ml_logic.params import LOCAL_DATA_PATH
from game_shazam.ml_logic.registry import save_model, load_model
from game_shazam.ml_logic.preprocessor import *
from game_shazam.ml_logic.model import *


def main():
        train_data_generator = get_data_generator(os.path.join(LOCAL_DATA_PATH, "train"))
        val_data_generator = get_val_generator(os.path.join(LOCAL_DATA_PATH, "val"))

        #test_data = get_val_generator(os.path.join(LOCAL_DATA_PATH, "test"))
        #model = load_model()
        #evaluate_data_gen(model, test_data)
        #print(train_data_generator.class_indices)
        model = initialize_big_model()

        model = compile_model(model)

        train_model(model, train_data_generator, val_data_generator)

        save_model(model)

main()
