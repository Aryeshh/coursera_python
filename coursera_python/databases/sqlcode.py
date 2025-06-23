import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Create the Counts table if it doesn't exist
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)
''')

# Open the mbox.txt file
fh = open('coursera_python\mbox.txt')

# Read through each line in the file
for line in fh:
    if not line.startswith('From: '): 
        continue
    # Extract the email address
    pieces = line.split()
    email = pieces[1]
    # Split the email to get the domain (organization)
    org = email.split('@')[1]
    
    # Check if the organization is already in the database
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    
    # If the org is already in the database, update its count
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    
# Commit the changes to the database
conn.commit()

# Show the top organizations
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the cursor and connection
cur.close()
