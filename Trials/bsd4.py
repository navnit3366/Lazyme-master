from bs4 import BeautifulSoup
import re
import requests
import os
import sys
import pafy
from urllib2 import urlopen
from urllib import quote_plus as qp
goog_url="https://www.google.co.in/search?q="
movie_name=raw_input('Enter movie name:') 
query=goog_url+qp(movie_name)
print query
req=requests.get(query)
result=req.content
link_start = result.find("http://www.imdb.com")
link_end = result.find("&amp",link_start)
link = result[link_start:link_end]
text_file = open("Output.txt", "w")
text_file.write(str(result))
text_file.close()
link=link+"soundtrack"
req=requests.get(link)
data=req.content
soup=BeautifulSoup(data,"html.parser")
print "Movie Songs : "
for s2 in soup.findAll("div", {"id" : re.compile('sn[0-9]{7}')}):
    s3=s2.text
    s3 = s3.encode('utf-8')
    song_end=s3.find('\n')
    fin_son=s3[0:song_end]
    print fin_son

