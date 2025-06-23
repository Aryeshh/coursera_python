import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()

# Create tables
cur.executescript('''
CREATE TABLE IF NOT EXISTS Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Open the CSV file
with open('tracks.csv', 'r') as f:
    # If there are no headers in the CSV, define them manually here
    headers = ['Track', 'Artist', 'Album', 'Length', 'Rating', 'Count', 'Genre']
    reader = csv.reader(f)
    
    # Skip the first row of data since it doesn't contain headers
    next(reader)
    
    for row in reader:
        # Use indexes according to the manually defined headers
        track_title = row[0]
        artist = row[1]
        album = row[2]
        length = row[3]
        rating = row[4]
        count = row[5]
        genre = row[6]

        # Insert artist, avoiding duplicates
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES ( ? )', (artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
        artist_id = cur.fetchone()[0]

        # Insert genre, avoiding duplicates
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES ( ? )', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
        genre_id = cur.fetchone()[0]

        # Insert album, avoiding duplicates
        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
        album_id = cur.fetchone()[0]

        # Insert track
        cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, len, rating, count) 
            VALUES ( ?, ?, ?, ?, ?, ? )''', 
            (track_title, album_id, genre_id, length, rating, count))

# Commit the changes
conn.commit()

# Close the connection
cur.close()
