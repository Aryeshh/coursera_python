import json
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Set up database schema
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER PRIMARY KEY,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Prompt for the JSON file name
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# Read and parse the JSON data
str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    # Assuming the JSON structure is: [ "Name", "Course Title", role ]
    name = entry[0]
    title = entry[1]
    role = entry[2]  # Extract role

    print((name, title, role))  # Added role to print statement

    # Insert user data
    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES ( ? )''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = cur.fetchone()[0]

    # Insert course data
    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title,))
    course_id = cur.fetchone()[0]

    # Insert member data with role
    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) 
                   VALUES ( ?, ?, ? )''', (user_id, course_id, role))

# Commit changes and close connection
conn.commit()
conn.close()
