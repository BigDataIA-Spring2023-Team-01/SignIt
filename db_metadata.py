import csv
import sqlite3

# Read the CSV file
with open('data/features_df.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

# Remove duplicates based on the "word" column
unique_data = []
seen_words = set()
for row in data:
    word = row[0]
    if word not in seen_words:
        seen_words.add(word)
        unique_data.append(row)

# Connect to SQLite database and create a table
conn = sqlite3.connect('data/metadata.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS word_list (word TEXT, video_id TEXT, url TEXT)')

# Insert unique rows into the table
for row in unique_data:
    cursor.execute('INSERT INTO word_list VALUES (?, ?, ?)', row)

# Commit changes and close the connection
conn.commit()
conn.close()
