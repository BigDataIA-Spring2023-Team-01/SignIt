import csv
import sqlite3

with open('data/features_df.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

unique_data = []
seen_words = set()
for row in data:
    word = row[0]
    if word not in seen_words:
        seen_words.add(word)
        unique_data.append(row)

conn = sqlite3.connect('data/metadata.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS word_list (word TEXT, video_id TEXT, url TEXT)')

for row in unique_data:
    cursor.execute('INSERT INTO word_list VALUES (?, ?, ?)', row)

conn.commit()
conn.close()
