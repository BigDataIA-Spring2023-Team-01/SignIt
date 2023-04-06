# import sqlite3

# # database connection
# conn = sqlite3.connect('data.db')
# cursor = conn.cursor()

# #input sentence from user
# sentence = "The deaf community faces unique challenges in communicating with the hearing world. Sign language is one of the most important and powerful tools that allow them to communicate and interact. However, not everyone knows how to communicate through sign language. That's where technology comes in. With advancements in AI and machine learning, it has become possible to create solutions that bridge the communication gap. One such solution is the use of sign language recognition systems that can translate sign language into text or speech. The WLASL-processed dataset provides a comprehensive list of sign language words, making it easier for developers to create these solutions. By leveraging the power of technology and the insights from this dataset, we can create a world where the deaf community can communicate more effectively and be more integrated into society."

# # split sentence into individual words
# words = sentence.split()

# # looping through each word and querying the database for the corresponding video_id
# video_ids = []
# for word in words:
#     cursor.execute("SELECT video_id FROM your_table WHERE word=?", (word,))
#     result = cursor.fetchone()
#     if result:
#         video_ids.append(result[0])

# # print the video_ids
# print(video_ids)

# # close the database connection
# conn.close()

import streamlit as st
import pandas as pd

@st.cache(persist=True)
def load_data():
    return pd.read_csv('features_df.csv')

def get_video_id(word, data):
    """
    Get the video id corresponding to a word from the data.
    """
    try:
        # Check if the word exists in the data
        return data.loc[data['word'] == word, 'video_id'].item()
    except ValueError:
        # If the word is not found, split it into letters and get the video id for each letter
        letters = list(word)
        video_ids = []
        for letter in letters:
            try:
                video_id = data.loc[data['word'] == letter, 'video_id'].item()
                video_ids.append(video_id)
            except ValueError:
                pass
        return video_ids

def main():

    st.write('Enter a transcript and get the corresponding video ids for the words.')
    
    # Load the data
    data = load_data()
    
    # Get user input
    transcript = st.text_input('Enter transcript:')
    words = transcript.split()
    
    # Get video ids for each word
    video_ids = [get_video_id(word, data) for word in words]
    
    # Display the video ids
    st.write('Video IDs:')
    for vid in video_ids:
        st.write(vid)
        
if __name__ == '__main__':
    main()

