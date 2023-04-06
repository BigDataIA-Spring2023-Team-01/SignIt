from fastapi import FastAPI
import pandas as pd
from pydantic import ValidationError, BaseModel

app = FastAPI()


class Transcript(BaseModel):
    transcript: str


videos = [
    {"name": "video1.mp4", "duration": 120},
    {"name": "video2.mp4", "duration": 180},
    {"name": "video3.mp4", "duration": 90},
]

@app.get("/videos")

async def get_videos():
    df = pd.read_csv('data/features_df.csv')
    return df.to_dict()




@app.post("/search_video_ids")
async def search_video_ids(transcript: Transcript):
    df = pd.read_csv("data/features_df.csv")

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
                        video_ids.append(int(matching_row.iloc[0]['video_id']))
        print(video_ids)
        return {'video': [int(id) for id in video_ids]}
    except ValueError as e:
        return {"error": str(e)}
