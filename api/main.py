from fastapi import FastAPI
import pandas as pd
app = FastAPI()

videos = [
    {"name": "video1.mp4", "duration": 120},
    {"name": "video2.mp4", "duration": 180},
    {"name": "video3.mp4", "duration": 90},
]

@app.get("/videos")

async def get_videos():
    df = pd.read_csv('data/features_df.csv')
    return df
