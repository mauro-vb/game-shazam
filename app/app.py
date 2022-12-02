import streamlit as st
from PIL import Image
import requests
import os
from io import BytesIO
import time
import wikipedia
import json
from results import show_results
import pandas as pd

# from dotenv import load_dotenv

st.set_page_config(
   page_title="Game Shazam",
   page_icon= '🎮',
   layout="centered",
   initial_sidebar_state="expanded",
)

# Button customize
button_customization = st.markdown("""
    <style >
    .stDownloadButton, div.stButton {text-align:center}
    .stDownloadButton button, div.stButton > button:first-child {
        background-color: #262730;
        color:#FFFFFF;
        padding-left: 10px;
        padding-right: 10px;
    }

    .stDownloadButton button:hover, div.stButton > button:hover {
        background-color: #ADD8E6;
        color:#000000;
    }
        }
    </style>""", unsafe_allow_html=True)

####################################

# Example local Docker container URL
# url = 'http://api:8000'
# Example localhost development URL
# url = 'http://localhost:8000'
# load_dotenv()
url = "https://gameshazam-govpopgxwq-ew.a.run.app"
# os.getenv('API_URL')


# App title and description
st.markdown("<h1 style='text-align: center; color: white;'>GAME SHAZAM</h1>", unsafe_allow_html=True)
# st.markdown("<h2 style='text-align: center; color: white;'>Some cool tagline</h2>", unsafe_allow_html=True)
st.markdown("")

st.markdown(f'''<p style='text-align: justify; color: white;'>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus quis erat lectus. Donec lacinia nulla.</p>''', unsafe_allow_html=True)

st.markdown("---")

### Select a model

### Upload image
st.markdown("### Please upload a screenshot 👇")
user_upload = st.file_uploader("")

fake_condition = True # use to play around with response-dependant features without making call
try_wiki = False


if user_upload is not None:

    ### Get bytes from the file buffer
    img_bytes = user_upload.getvalue()
    ### Make request to  API
    with st.spinner("Processing your image..."):
        res = requests.post(url + "/predict/", files={'img': img_bytes})
        time.sleep(1)
    data = res.json()
    table_res = show_results(probabilities= data["probs"])
    first_choice = table_res._get_value(0, "Game")
    first_prob = table_res._get_value(0, "Certainty")
    runner_ups = table_res.drop(0, axis=0).set_index(keys="Game")
    dropdown_table = pd.DataFrame(table_res["Game"]+ " -------- (" +table_res["Certainty"].apply(lambda x: str(x)) + " certainty)")

    col1, col2 = st.columns(2)

    with col1:
    ### Display the user's image
    # img_resized = img_user.resize((336, 336))
        st.image(Image.open(user_upload), caption="Here's your screenshot ☝️")


    with col2:

        if res.status_code == 200:
            try_wiki = True


            # st.markdown(f'''<h3 style='text-align: justify; color: white;'>
            #  Your game is: {first_choice} \n {first_prob} certainty
            # </h3>''', unsafe_allow_html=True)

            st.markdown(f'''<h5 style='text-align: center; color: white;'>
            --- Your game is ---</h5>
            <h2 style='text-align: center; color: white;'>
            {first_choice}</h2>
            <h5 style='text-align: center; color: white;'>
            ({first_prob} certainty)</h5>''',
            unsafe_allow_html=True)



            st.markdown("")
            if st.button('''---🔍 Click here to see more guesses 🔍---'''):
                st.table(runner_ups)



            # Simple version:
            ### Display a table with potential answers
            ### Each answer has a hyperlink that displays it's wiki search below
            # st.table(show_results(probabilities= data["probs"]))

        else:
            st.markdown("Something's gone wrong!")
            print(f"status code is:{res.status_code}")
            print(f"content is {res.content}")


if try_wiki == True:

    st.markdown("")
    wikiselect = st.selectbox('Click here to see more guesses 🔍', dropdown_table)
    index_to_pass = dropdown_table.index[dropdown_table[0]== wikiselect][0]
    search_term = table_res._get_value(index_to_pass, "Game")

    search_res_list = wikipedia.search(search_term)
    wiki_sum = wikipedia.summary(search_res_list[0], sentences=10, auto_suggest=False)

    st.markdown("---")

    st.markdown(f'''<p style="
                text-align: justify; color: white;">{wiki_sum}</p>''', unsafe_allow_html=True)





    #  try to add this styling to the text above:
    #  border-style:outset; border-radius:20px, border-color:#ADD8E6; padding: 1em;
