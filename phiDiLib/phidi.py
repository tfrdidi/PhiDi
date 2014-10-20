# -*- coding: utf-8 -*-
import sys, phidilib


baseURI = "https://de.wikipedia.org"
wikiSuffix = "/wiki/"
target = "Philosophie"
distance = 0
maxDistance = 20
targetNotReached = True


if len(sys.argv) == 1:
	path = wikiSuffix + "mallorca"
elif len(sys.argv) > 1:
	path = wikiSuffix + sys.argv[1]
elif len(sys.argv) > 2:
	maxDistance=sys.argv[2]
elif len(sys.argv) > 3:
	target=sys.argv[3]


while(targetNotReached and (distance < maxDistance)):
	print str(path)[len(wikiSuffix):] + " distance="+str(distance)
	if(path == wikiSuffix+target):
		print "Target reached in distance: " + str(distance)
		targetNotReached = False
	else:
		path = phidilib.getForwardingLink(baseURI + str(path))
	distance += 1