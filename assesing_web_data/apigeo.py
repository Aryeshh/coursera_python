
import urllib.request, urllib.parse
import json, ssl

# API Endpoint
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: 
        break

    parms = dict()
    parms['q'] = address.strip()

    # Build the complete API request URL
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)

    # Open the URL and fetch data
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    print('Retrieved', len(data), 'characters')

    try:
        # Parse the JSON data
        js = json.loads(data)
    except json.JSONDecodeError:
        js = None
        print("Failed to parse JSON")

    # Check if valid response and JSON structure
    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        continue

    if len(js['features']) == 0:
        print('==== Object not found ====')
        continue

    # Retrieve plus_code from the JSON if available
    if 'plus_code' in js['features'][0]['properties']:
        plus_code = js['features'][0]['properties']['plus_code']
        print('Plus Code:', plus_code)
    else:
        print('No Plus Code found')

    break