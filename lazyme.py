from bs4 import BeautifulSoup
import requests
import re
import os
import sys
from urllib2 import urlopen
from urllib import quote_plus as qp
import youtube_dl
import pafy
def song_dwnld(url):
	#url= "https://www.youtube.com/watch?v=yKNxeF4KMsY"  -- test purpose
	video=pafy.new(url)
	print (video.title)
	best=video.getbestaudio()
	#dwnld=best.download() --to just dwnld best audio in m4a
	audiostreams = video.audiostreams
	i=1
	for a in audiostreams:
	    print(i,a.bitrate, a.extension, a.get_filesize())
	    i=i+1
	print "Enter which one to dwnld"
	i=int(raw_input())
	dwnld=audiostreams[i].download() #download whatever quality song file you want

def yout_url(query):
    you_url = "https://www.youtube.com/results?search_query=" #searching in youtube
    #query=raw_input("Enter song :") --- test purpose
    url = you_url + qp(query)
    #print url ---just checking if youtube urls are right
    req = requests.get(url)
    result = req.content
    soup=BeautifulSoup(result,"html.parser")
    link=""
    for link in soup.find_all('a'):
        if  "watch" in (link.get('href')):
           fin_you="https://www.youtube.com"+link.get('href')
           return(fin_you) # -- return youtube link for supplying to pafy
           break
        
            
def band_top():
	goog_url = "https://www.google.co.in/search?q="
	query=raw_input("Enter band:")
	band_name=query
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
	text_file = open("Output.txt", "w")
	text_file.write(str(data))
	text_file.close()
	s2=''
	s3=''
	soup=BeautifulSoup(data,"html.parser")
	print "Top 10:"
	for s2 in soup.findAll("div", {"id" : re.compile('i[0-9]*')}):
	    s3=s2.find('b').text
	    s3 = s3.encode('utf-8')
	    if(ctr!=1):
	       dwn_url=yout_url(s3+band_name)
	       song_dwnld(dwn_url)
	    ctr=ctr+1
	    if ctr == 12:
	       break

def movie_ost():
	goog_url="https://www.google.co.in/search?q="
	movie_name=raw_input('Enter movie name:') 
	query=goog_url+qp(movie_name)
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
	    dwn_url=yout_url(fin_son+movie_name)
	    song_dwnld(dwn_url)

def main():
    print "1 for Movie OR 2 for Band:"
    ct=raw_input()
    if ct=='1':
    	movie_ost()
    else:
        band_top()	

if  __name__ =='__main__':main()