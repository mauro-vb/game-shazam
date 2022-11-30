from fastapi import FastAPI, File, UploadFile
from game_shazam.ml_logic.registry import load_model
from game_shazam.ml_logic.preprocessor import prep_for_pred
from game_shazam.ml_logic.params import GAMES_DICT
import numpy as np
import os

app = FastAPI()
app.state.model = load_model()


@app.get("/")
async def root():
    return {"status": "ok"}


@app.post("/predict/")
async def create_file(img: bytes =File(...)):

    with open('image.jpg','wb') as image:
        image.write(img)
        image.close()
    X = prep_for_pred('image.jpg')
    os.remove('image.jpg')
    pred = app.state.model.predict(X)
    result = dict()
    for i, p in enumerate(pred[0]):
        result[GAMES_DICT[i]] = float(p)

    best = np.max(pred)
    position = pred[0].tolist().index(best)

    response = dict(probs=result,best=GAMES_DICT[position])
    return response
