# -*- coding: utf-8 -*-
import sys, re, mpdlib
from mechanize import Browser, urljoin
from bs4 import BeautifulSoup

baseURI = "https://de.wikipedia.org"
wikiSuffix = "/wiki/"
target = "Philosophie"
#uri = urljoin(baseURI,wikiSuffix)
maxDistance = 20

if len(sys.argv) == 1:
	path = urljoin(wikiSuffix,"mallorca")
elif len(sys.argv) > 1:
	path = urljoin(wikiSuffix,sys.argv[1])
elif len(sys.argv) > 2:
	maxDistance=sys.argv[2]
elif len(sys.argv) > 3:
	target=sys.argv[3]


for i in range(maxDistance):
	print path[len(wikiSuffix):] + " distance="+str(i)
	if(path == wikiSuffix+target):
		print "Target reached in distance: " + str(i+1)
		i = maxDistance
	path = mpdlib.getForwardingLink(urljoin(baseURI,path))