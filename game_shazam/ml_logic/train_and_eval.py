from game_shazam.ml_logic.preprocessor import *
from game_shazam.ml_logic.model import *

train_path = '/Users/mauro/code/game-shazam/data/train_val/train'
val_path = '/Users/mauro/code/game-shazam/data/train_val/val'

def main():
        #breakpoint()
        train_data_generator = get_data_generator(train_path)
        val_data_generator = get_val_generator(val_path)

        model = initialize_model()
        model = compile_model(model)

        train_model(model, train_data_generator, val_data_generator)

        #metrics = evaluate_data_gen(model, val_data_generator)

        #print(metrics)

main()
