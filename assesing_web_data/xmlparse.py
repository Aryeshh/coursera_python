import urllib.request
import xml.etree.ElementTree as ET

# Function to extract and sum counts from the XML data
def extract_sum_from_xml(url):
    # Retrieve the XML data from the URL
    print(f'Retrieving {url}')
    response = urllib.request.urlopen(url)
    data = response.read()
    print(f'Retrieved {len(data)} characters')

    # Parse the XML data
    tree = ET.fromstring(data)
    
    # Find all 'count' elements
    counts = tree.findall('.//count')
    
    # Compute the sum of the count values
    total_sum = sum(int(count.text) for count in counts)
    return len(counts), total_sum

# Main function
# Prompt for URL
url = input('Enter location: ')

# Extract and compute the sum
count, total_sum = extract_sum_from_xml(url)

# Display results
print(f'Count: {count}')
print(f'Sum: {total_sum}')
