import streamlit as st
from PIL import Image
import requests
import os
from io import BytesIO
import time
# from dotenv import load_dotenv



####################################

# Set page tab display
st.set_page_config(
   page_title="Game Shazam",
   page_icon= '🎮',
   layout="centered",
   initial_sidebar_state="expanded",
)

# Example local Docker container URL
# url = 'http://api:8000'
# Example localhost development URL
url = 'http://127.0.0.1:8000/'
# load_dotenv()
# url = "https://gameshazam-govpopgxwq-ew.a.run.app"
# os.getenv('API_URL')


# App title and description
st.markdown("<h1 style='text-align: center; color: white;'>GAME SHAZAM</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Some cool tagline</h2>", unsafe_allow_html=True)
st.markdown("")

st.markdown('''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus quis erat lectus. Donec lacinia nulla volutpat, sodales urna ac,
            pretium dui. Donec nulla elit, vestibulum sed aliquam ac, malesuada sit amet justo.
            ''')

st.markdown("---")

### Select a model


### Upload image
st.markdown("### Please upload a screenshot 👇")
user_upload = st.file_uploader('Upload an image')


# PREDICT to fill later
# img_user = Image.open(user_upload)
# prediction = predict(img, index_to_class_label_dict, model, k=5)
# top_prediction = prediction[0][0]
# available_images = all_image_files.get(
#     'train').get(top_prediction.upper())
# examples_of_species = np.random.choice(available_images, size=3)
# files_to_get_from_s3 = []

show_wiki = False

if user_upload is not None:

  col1, col2 = st.columns(2)

  with col1:
    ### Display the user's image
    # img_resized = img_user.resize((336, 336))
    st.image(Image.open(user_upload), caption="Here's your screenshot ☝️")


  with col2:
    with st.spinner("Processing..."):
      time.sleep(1)
      ### Get bytes from the file buffer
      img_bytes = user_upload.getvalue()
      print(type(img_bytes))

      ### Make request to  API
      res = requests.post(url + "predict", files={'img': img_bytes})

      if res.status_code == 200:
        show_wiki = True
        ### Display a table with potential answerss
        st.markdown("Placeholder answer")

      else:
        show_wiki = True # JUST FOR TESTING, REMOVE!!!
        st.markdown("Something's gone wrong!")
        print(f"status code is:{res.status_code}")
        print(f"content is {res.content}")


if show_wiki == True:
    st.markdown("Placeholder for wikipedia entry")
