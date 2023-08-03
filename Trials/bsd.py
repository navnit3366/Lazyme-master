from bs4 import BeautifulSoup
import requests
import re
import os
import sys
from urllib2 import urlopen
from urllib import quote_plus as qp

goog_url = "https://www.google.co.in/search?q="
query=raw_input("Enter band:")
query=query+" top tens"
url = goog_url + qp(query)
print url
req = requests.get(url)
result = req.content
link_start = result.find("http://www.thetoptens.com")
link_end = result.find("&amp",link_start)
link = result[link_start:link_end]
ctr=1
print link
req=requests.get(link)
data=req.content
#print data
s2=''
s3=''
soup=BeautifulSoup(data,"html.parser")
print "Top 10:"
for s2 in soup.findAll("div", {"id" : re.compile('i[0-9]*')}):
    s3=s2.find("b").text
    s3 = s3.encode('utf-8')
    if(ctr!=1):
       print(s3+'\n')
    ctr=ctr+1
    if ctr == 12:
       break