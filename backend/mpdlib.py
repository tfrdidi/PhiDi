import sys, re
from mechanize import Browser, urljoin
from bs4 import BeautifulSoup

linkSearchPrefix = "href="

def get_next_target(page):
    start_link = page.find(linkSearchPrefix)
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url

def getForwardingLink(uri):
	#print uri
	validTagsFirstParagraph = ["b","a","i"]

	mech = Browser()
	response = mech.open(uri)

	soup = BeautifulSoup(response)

	contentResultSet = soup.find_all("div", id="mw-content-text")[0].findChildren(recursive=False)

	for tag in contentResultSet:
		if(tag.name == "p" and len(tag.getText())>5 and tag.findChild().name in validTagsFirstParagraph):
			#print "FirstChild: " + str(tag.findChild())
			#print "_____________________________" + tag.getText()
			stringFirstParagraph = str(tag)
			break

	#print stringFirstParagraph

	indexFirstOpeningBracket = stringFirstParagraph.find("(")

	indexFirstLink = stringFirstParagraph.find(linkSearchPrefix)
	

	if(indexFirstLink < 0):
		print "Erron on: " + uri + " No links found, please try another site"
	else:
		if(indexFirstOpeningBracket<0):
			#print "KLICK indexFirstOpeningBracket<0"
			#print get_next_target(stringFirstParagraph)
			return get_next_target(stringFirstParagraph)
		else:
			if(indexFirstLink<indexFirstOpeningBracket):
				#print "KLICK  indexFirstLink < indexFirstClosingBracket"
				return get_next_target(stringFirstParagraph)

			else:
				#print "Find new link position"
				stringFirstParagraph = stringFirstParagraph[indexFirstOpeningBracket:]
				indexFirstClosingBracket = stringFirstParagraph.find(")")
				stringFirstParagraph = stringFirstParagraph[indexFirstClosingBracket:]
				return get_next_target(stringFirstParagraph)
