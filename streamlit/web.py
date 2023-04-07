import streamlit as st
import requests
import json
import os
import base64


UPLOAD_DIR = "data/audio_files"
if not os.path.exists(UPLOAD_DIR):
            os.makedirs(UPLOAD_DIR)



def whisper(file_path):
    token = os.environ.get('OPENAI_SECRET_KEY')
    url = 'https://api.openai.com/v1/audio/transcriptions'
    audio_format = 'm4a'
    # Set your API key as a header
    headers = {
        'Authorization': 'Bearer ' + token
    }
    payload={"model": "whisper-1"}
    
    # Read in your local audio file as binary data
    with open(file_path, 'rb') as f:
        audio_data = f.read()
    data = {
    'file': (f'audio.{audio_format}', audio_data),
    }
    
    # Send a POST request to the Whisper API with your audio data
    response = requests.request('POST',url, headers=headers, data=payload, files=data)

    # Print the transcription result
    print(response.text)
    return(response.text)

# Streamlit app

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

background(r"C:\Users\user\OneDrive\Desktop\Untitled-2.png")

st.title("Upload or Record and Transcribe Audio")

    # Get user input: upload file or record audio
source = st.radio("Select audio source", ("Upload file", "Record audio"))

if source == "Upload file":
    # Allow user to upload an audio file
    uploaded_file = st.file_uploader("Upload an audio file (mp3, mp4, m4a)", type=["mp3", "mp4", "m4a"])
 # Save uploaded file
    if uploaded_file is not None:
            # Get file name
        file_name = uploaded_file.name

            # Save file to directory
        with open(os.path.join(UPLOAD_DIR, file_name), "wb") as f:
            f.write(uploaded_file.read())
        st.success("File saved successfully!")
        text=whisper('../data/audio_files/'+ file_name)
        st.text_area('',text)
    else:
        st.warning("No file uploaded.")

        # Display the transcribed text
        
else:
    # Allow user to record audio using the microphone
    duration = st.slider("Recording Duration (in seconds)", 1, 10, 3)
    if st.button("Start Recording"):
        st.write("Recording...")
        audio_path = "recorded_audio.m4a"
        cmd = f"ffmpeg -hide_banner -loglevel panic -t {duration} -f avfoundation -i :0 -ac 2 {audio_path}"
        os.system(cmd)
        st.write("Finished Recording!")
        
        # Transcribe the recorded audio using Whisper API
        transcription = transcribe_audio("recorded_audio.m4a")

        # Display the transcribed text
        if transcription is not None:
            st.subheader("Transcribed text:")
            st.text_area("", value=transcription, height=200)
        else:
            st.error("Transcription failed. Please try again later.")
