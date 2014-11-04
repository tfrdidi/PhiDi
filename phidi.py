# -*- coding: utf-8 -*-
import phidilib


baseURI = "https://de.wikipedia.org"
wikiSuffix = "/wiki/"
target = "Philosophie"
maxDistance = 20



def getSampleDistance():
	return getDistanceTo("Mallorca")
	

def getDistanceTo(articleName):
	subPath = wikiSuffix + articleName
	distance = -1
	targetNotReached = True

	while(targetNotReached and (distance < maxDistance)):
		if(subPath == wikiSuffix + target):
			targetNotReached = False
		else:
			subPath = phidilib.getForwardingLink(baseURI + str(subPath))
		distance += 1
	return distance

def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

def testFileAccess():
	f = open ("test", w)
	f.write("Upsala")
	f.close
	f = open ("test", r)
	return f.readline()