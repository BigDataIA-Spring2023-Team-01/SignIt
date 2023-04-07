import requests
import streamlit as st


# Define the Streamlit app
def main():
    # Set the page title
    st.set_page_config(page_title="My Video App")

    # Get the video data from the API
    user_input = st.text_input("Enter text")

    video_url = "data/archive/signlanguagevideos/temp.mp4"
    st.video(video_url)
# Run the Streamlit app
if __name__ == "__main__":
    main()
