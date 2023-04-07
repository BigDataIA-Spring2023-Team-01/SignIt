import requests
from dotenv import load_dotenv
import os
import json
import pytest
import requests
token = os.environ.get("OPENAI_SECRET_KEY") # whisper api key



def test_incorrect_file_format():
    # upload a text file instead of an mp3 file
    url = 'http://ec2-18-234-225-32.compute-1.amazonaws.com:8501/'
    files = {'file': ('download.jpeg', open('download.jpeg', 'rb'))}
    response = requests.post(url, files=files)
    
    # check whether the app returns the correct error message
    assert response.status_code == 403


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

    
# def test_asl_service_up():
#     response = requests.get("http://localhost:8000")
#     assert response.status_code == 200
