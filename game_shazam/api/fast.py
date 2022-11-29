from fastapi import FastAPI, File, UploadFile
from game_shazam.ml_logic.registry import load_model
from game_shazam.ml_logic.preprocessor import preprocess_features
from game_shazam.ml_logic.params import GAMES_DICT
import numpy as np
from matplotlib.pyplot import imread

app = FastAPI()
app.state.model = load_model()


@app.get("/")
async def root():
    return {"status": "ok"}


@app.post("/predict/")
async def create_file(img: UploadFile=File(...)):
    ### Receiving and decoding the image
    contents = await img.read()

    nparr = np.fromstring(contents, np.uint8)
    np_img = imread(nparr)
    pr_img = preprocess_features(np_img)
    pred = app.state.model.predict(pr_img)
    for i, p in enumerate(pred):
        if p == 1:
            return dict(prediction=GAMES_DICT[i])

@app.post("/predict_proba/")
async def create_file(img: UploadFile=File(...)):
    ### Receiving and decoding the image
    contents = await img.read()

    nparr = np.fromstring(contents, np.uint8)
    np_img = imread(nparr)
    pr_img = preprocess_features(np_img)
    pred = app.state.model.predict_proba(pr_img)
    proba = dict()
    for i, p in enumerate(pred):
        proba[GAMES_DICT[i]] = p
    return proba
