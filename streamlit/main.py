import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv
import base64
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


def get_video_id(transcript):
    API_URL = "http://fastapi.latest:8000"
    url = f"{API_URL}/search_video_ids"
    response = requests.post(url,json={"transcript": transcript})
    if response.status_code == 200:
        video_list = json.loads(response.text)
        return video_list
    else:
        return []
    

def merge_videos(video_list):
    API_URL = "http://fastapi.latest:8000"
    url = f"{API_URL}/video_merge"
    response = requests.post(url,json={"video_list": video_list})
    if response.status_code == 200:
        res = json.loads(response.text)
        return res['key_name']
    else:
        return {'video': []}

# setting up the background image 
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

background(r"./data/images/Untitled-2.png")


st.title("SignIt:wind_blowing_face::ok_hand:")
st.header("Upload or Record and Transcribe Audio")

source = st.radio("Select audio source", ("Upload file", "Enter text"))

if source == "Upload file":

    uploaded_file = st.file_uploader("Upload an audio file (mp3, mp4, m4a)", type=["mp3", "mp4", "m4a"])
    upload = st.button('Upload file')

    if upload:

## Step 1 - Transcribe the audio file to text
        file_name = uploaded_file.name
        with open(os.path.join(UPLOAD_DIR, file_name), "wb") as f:
            f.write(uploaded_file.read())
        st.success("File saved successfully!")
        text = whisper(os.path.join(UPLOAD_DIR, file_name))

## Step 2 - Conver the transcript into sign language
        video_list = get_video_id(text)

## Step 3 - Merge all the sign language videos and display it to user
        with st.spinner("Running..."):
            merged_video_name = merge_videos(video_list['video'])
            video_url = f"data/archive/signlanguagevideos/{merged_video_name}"
            st.success("Sign Language created")
        st.video(video_url)
        st.text_area('',text)
elif source == "Enter text":
    user_input = st.text_input("Enter text to convert to sign language")
    translate = st.button('Translate')
    if translate:
        video_list = get_video_id(user_input)


        with st.spinner("Running..."):
            merged_video_name = merge_videos(video_list['video'])
            video_url = f"data/archive/signlanguagevideos/{merged_video_name}"
            st.success("Sign Language created")
        st.video(video_url)
        st.text_area('',user_input)

    
    