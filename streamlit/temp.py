import requests
import base64
import streamlit as st
st.set_page_config(page_title="My Video App")

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

background(r"data/images/Untitled-2.png")

# Define the Streamlit app
def main():
    # Set the page title
    

    # Get the video data from the API
    user_input = st.text_input("Enter text")

    video_url = "data/archive/signlanguagevideos/temp.mp4"
    st.video(video_url)
    st.text_area('','Hello my name is name')
# Run the Streamlit app
if __name__ == "__main__":
    main()
