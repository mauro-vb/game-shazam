FROM tensorflow/tensorflow:2.10.1

COPY game_shazam /game_shazam
COPY requirements_prod.txt /requirements.txt
COPY Makefile /Makefile

RUN mkdir loaded_models

RUN apt-get update
RUN apt-get install \
  'ffmpeg'\
  'libsm6'\
  'libxext6'  -y

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn game_shazam.api.fast:app --host 0.0.0.0 --reload --port ${PORT}
