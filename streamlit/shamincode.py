import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


UPLOAD_DIR = "data/audio_files"
if not os.path.exists(UPLOAD_DIR):
            os.makedirs(UPLOAD_DIR)



def whisper(file_path):
    token = os.environ.get('OPENAI_SECRET_KEY')
    url = 'https://api.openai.com/v1/audio/transcriptions'
    # Set your API key as a header
    headers = {
        'Authorization': 'Bearer ' + token
    }
    payload={"model": "whisper-1"}
    
    files = {"file": open(file_path, "rb")}

    response = requests.post(url, headers=headers, data=payload, files=files)

    if response.status_code == 200:
        data = response.json()
        transcription = data["text"]
        return transcription
    else:
        return None


st.title("Upload or Record and Transcribe Audio")

source = st.radio("Select audio source", ("Upload file", "Record audio"))

if source == "Upload file":

    uploaded_file = st.file_uploader("Upload an audio file (mp3, mp4, m4a)", type=["mp3", "mp4", "m4a"])
    upload = st.button('Upload file')

    if upload:
        file_name = uploaded_file.name

        with open(os.path.join(UPLOAD_DIR, file_name), "wb") as f:
            f.write(uploaded_file.read())
        st.success("File saved successfully!")
        text = whisper(os.path.join(UPLOAD_DIR, file_name))
        st.text_area('', text)
        
elif source == "Record audio":
    st.warning("Code not implemented yet")
    
    