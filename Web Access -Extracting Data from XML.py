import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_372589.xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

counter = 0

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address

    #print(parms)

    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)


    #print(urllib.parse.urlencode(parms))
    #print(url)

    #url = 'www.py4e-data.dr-chuck.net/comments_372589.xml'
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    #print(uh)

    data = uh.read()
    #print(data)
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    #print(tree)

    results = tree.findall('comments')
    for i in results[0]:
        lat = i.find('name').text
        lng = i.find('count').text
        #lng = results[0].find('comment').find('count').text
        #location = results[0].find('formatted_address').text
        counter += int(lng)
        #print('lat', lat, 'lng', lng)
        #print(location)

    print('sum of nums =',counter)
