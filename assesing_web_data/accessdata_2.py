import urllib.request
from bs4 import BeautifulSoup

def sol(start_url, count, position):
    url = start_url
    
    for _ in range(count):
        print(f'Retrieving: {url}')
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Find all anchor tags
        tags = soup.find_all('a')
        
        # Check if the position is within the range of available links
        if position - 1 < len(tags):
            # Get the URL at the specified position
            url = tags[position - 1].get('href', None)
        else:
            print("Position is out of range. No more links to follow.")
            return None

    # Return the last name found
    last_name = tags[position - 1].text
    return last_name


# User inputs
start_url = input('Enter URL: ')   #http://py4e-data.dr-chuck.net/known_by_Sheridan.html
count = int(input('Enter count: '))
position = int(input('Enter position: '))
    
# Follow the links and get the last name
last_name = sol(start_url, count, position)
    
if last_name:
    print(f'The answer to the assignment is "{last_name}".')
