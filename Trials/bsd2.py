from bs4 import BeautifulSoup
import requests
import re
import youtube_dl
import os
import sys
from urllib2 import urlopen
from urllib import quote_plus as qp
you_url = "https://www.youtube.com/results?search_query="
query=raw_input("Enter song :")
url = you_url + qp(query)
print url
req = requests.get(url)
result = req.content
soup=BeautifulSoup(result,"html.parser")
link=""
for link in soup.find_all('a'):
    if  "watch" in (link.get('href')):
       fin_you="https://www.youtube.com"+link.get('href')
       print(fin_you)
       break
    else:
        {}