import requests
import streamlit as st

# Set the URL for the API endpoint
API_URL = "http://fastapi.latest:8000"

# Define a function to get the video data from the API
def get_video_id(transcript):
    url = f"{API_URL}/search_video_ids"
    response = requests.post(url,json={"transcript": transcript})
    if response.status_code == 200:
        return response.text
    else:
        return []

# Define the Streamlit app
def main():
    # Set the page title
    st.set_page_config(page_title="My Video App")

    # Get the video data from the API
    user_input = st.text_input("Enter text")

    # Display the video data in a table
    res = get_video_id(user_input)
    st.write(res)
# Run the Streamlit app
if __name__ == "__main__":
    main()
