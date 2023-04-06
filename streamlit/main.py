import requests
import streamlit as st

# Set the URL for the API endpoint
API_URL = "http://fastapi.latest:8000"

# Define a function to get the video data from the API
def get_videos():
    url = f"{API_URL}/videos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Define the Streamlit app
def main():
    # Set the page title
    st.set_page_config(page_title="My Video App")

    # Get the video data from the API
    videos = get_videos()

    # Display the video data in a table
    st.table(videos)

# Run the Streamlit app
if __name__ == "__main__":
    main()
