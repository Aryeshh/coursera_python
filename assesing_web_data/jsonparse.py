import urllib.request
import json

# Prompt for the URL
link = input('Enter location: ')
print('Retrieving', link)

# Open the URL and read the data
connection = urllib.request.urlopen(link)
raw_data = connection.read().decode()
print('Retrieved', len(raw_data), 'characters')

# Parse the JSON data
parsed_data = json.loads(raw_data)

# Extract comment counts and compute the sum
comment_section = parsed_data['comments']
total_count = sum([int(item['count']) for item in comment_section])

# Display the result
print('Count:', len(comment_section))
print('Sum:', total_count)
