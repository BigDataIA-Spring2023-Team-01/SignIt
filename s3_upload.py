import sqlite3
import os
import boto3
from dotenv import load_dotenv
load_dotenv()
# Connect to SQLite database and execute a query to retrieve all video IDs
conn = sqlite3.connect('data/metadata.db')
cursor = conn.cursor()
cursor.execute('SELECT DISTINCT video_id FROM word_list')
video_ids = [row[0] for row in cursor.fetchall()]

# Define the path to the folder containing the videos
videos_folder = 'data/kaggledataset/videos'

s3 = boto3.client('s3',region_name='us-east-1',
                            aws_access_key_id = os.environ.get('AWS_ACCESS_KEY'),
                            aws_secret_access_key = os.environ.get('AWS_SECRET_KEY'))
bucket_name = os.environ.get('SIGN_LANGUAGE_BUCKET')


for video_filename in os.listdir(videos_folder):
    video_id = os.path.splitext(video_filename)[0] 
    if video_id in video_ids:
        # Construct the S3 object key by removing the file extension and replacing any backslashes with forward slashes
        object_key = video_filename.split('.')[0].replace('\\', '/')
        s3.upload_file(os.path.join(videos_folder, video_filename), bucket_name, object_key)
