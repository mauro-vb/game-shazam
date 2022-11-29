from game_shazam.ml_logic.preprocessor import *
from game_shazam.ml_logic.model import *

train_path = '/Users/mauro/code/game-shazam/data/train_test/train'
test_path = '/Users/mauro/code/game-shazam/data/train_test/test'

def main():
        #breakpoint()
        train_data_generator = get_data_generator(train_path)
        test_data_generator = get_test_generator(test_path)

        model = initialize_model()
        model = compile_model(model)

        train_model(model, train_data_generator)

        metrics = evaluate_data_gen(model, test_data_generator)

        print(metrics)

main()
