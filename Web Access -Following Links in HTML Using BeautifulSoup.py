# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
cwlist = list()
n = 1
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


#Retrieve the main name form the url

# Retrieve all of the anchor tags
while n <= 7:
    tags = soup('a')
    for tag in tags:
        croppy = tag.get('href', None)
        cwlist.append(croppy)
    
    html = urllib.request.urlopen(cwlist[17], context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    if n == 7:
        croppedword = re.findall('by_([^ ]*)\.',cwlist[17])
        print(croppedword[0])
    cwlist = list()
    n = n+1
