from game_shazam.ml_logic.params import LOCAL_REGISTRY_PATH
from game_shazam.model_target.cloud_model import save_cloud_model
from game_shazam.model_target.local_model import save_local_model

import os
import shutil
import time
import glob
from google.cloud import storage

from tensorflow.keras import Model, models


def save_model(model: Model = None,
               params: dict = None,
               metrics: dict = None) -> None:
    """
    persist trained model, params and metrics
    """

    timestamp = time.strftime("%Y%m%d-%H%M%S")

    if os.environ.get("MODEL_TARGET") == 'local':
        save_local_model(params, metrics, model, timestamp)

    elif os.environ.get("MODEL_TARGET") == 'gcs':
        save_cloud_model(model, timestamp)

    else:
        raise ValueError(f'{os.environ.get("MODEL_TARGET")} not know')

    return None

def load_model(save_copy_locally=False):


    if os.environ.get("MODEL_TARGET") == "local":
        # get latest model version
        model_directory = os.path.join(os.environ.get("LOCAL_REGISTRY_PATH"), "models")

        results = glob.glob(f"{model_directory}/*")
        if not results:
            return None

        model_path = sorted(results)[-1]
        print(f"- path: {model_path}")

        model = models.load_model(model_path)
        print("\n✅ model loaded from disk")

        return model

    if os.environ.get("MODEL_TARGET") == "gcs":
        client = storage.Client()
        blobs = client.list_blobs(os.environ.get("BUCKET_NAME"))
        pickle_folder = os.path.join(os.environ.get("LOCAL_REGISTRY_PATH"), "loaded_models", os.environ.get("GCS_MODEL"))
        print(pickle_folder)
        print(os.getcwd())
        if not os.path.isdir(pickle_folder):
            os.mkdir(pickle_folder)
            print('created folder')
            os.mkdir(os.path.join(pickle_folder, 'assets'))
            os.mkdir(os.path.join(pickle_folder, 'variables'))
        print(os.getcwd())
        for blob in blobs:
            blob.download_to_filename(os.path.join(os.environ.get("LOCAL_REGISTRY_PATH"), "loaded_models", blob.name))

        model = models.load_model(os.path.join(os.environ.get("LOCAL_REGISTRY_PATH"), "loaded_models", os.environ.get("GCS_MODEL")))

        if not save_copy_locally:
            shutil.rmtree(os.path.join(os.environ.get("LOCAL_REGISTRY_PATH"), "loaded_models", os.environ.get("GCS_MODEL")))

        return model
