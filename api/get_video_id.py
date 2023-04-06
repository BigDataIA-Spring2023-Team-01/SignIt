

from typing import List
from fastapi import FastAPI
from pydantic import ValidationError, BaseModel
import pandas as pd

app = FastAPI()

df = pd.read_csv("features_df.csv")

class Transcript(BaseModel):
    transcript: str

@app.post("/search_video_ids")
def search_video_ids(transcript: Transcript):
    try:
        words = transcript.transcript.split()
        video_ids = []
        for word in words:
            matching_row = df.loc[df['word'] == word.lower()]
            if not matching_row.empty:
                video_ids.append(matching_row.iloc[0]['video_id'])
            else:
                letters = list(word.lower())
                for letter in letters:
                    matching_row = df.loc[df['word'] == letter]
                    if not matching_row.empty:
                        video_ids.append(matching_row.iloc[0]['video_id'])
        print(video_ids)
        return {'video':video_ids}
    except ValueError as e:
        return {"error": str(e)}

