import requests
from dotenv import load_dotenv
import os
import json
import pytest
import requests
load_dotenv()
token = os.environ.get("OPENAI_SECRET_KEY") # whisper api key



def test_streamlit_app_is_up():
    url = os.environ.get("STREAMLIT_URL")
    response = requests.get(url)
    assert response.status_code == 200

    
def test_incorrect_file_format():
    # upload a text file instead of an mp3 file
    url = os.environ.get("API_URL") + "/search_video_ids"
    files = {'file': ('download.png', open('data/images/download.png', 'rb'))}
    response = requests.post(url, files=files)
    
    # check whether the app returns the correct error message
    assert response.status_code == 422


def test_whisper_api_up():
    headers = {
      'Authorization': 'Bearer ' + token
    }
    payload={'model': 'whisper-1','response_format':'json'}
    url = "https://api.openai.com/v1/audio/transcriptions"
    response = requests.request("POST", url, headers=headers, data=payload)

    response_json = response.json()
    print(response_json)
    assert response.status_code == 400


def test_search_video_ids_output():
    url = os.environ.get("API_URL") + "/search_video_ids"
    transcript = {"transcript": "sample transcript"}

    response = requests.post(url, json=transcript)

    assert response.status_code == 200

    assert "video" in response.json()

    assert isinstance(response.json()["video"], list)

    assert all(isinstance(video_id, int) for video_id in response.json()["video"])



def test_merge_videos_output():
    url = os.environ.get("API_URL") + "/video_merge"
    videos = {"video_list": ["10021"]}

    response = requests.post(url, json=videos)

    assert response.status_code == 200

    # Check response format
    assert "key_name" in response.json()
    assert isinstance(response.json()["key_name"], str)

