from mechanize import Browser
from bs4 import BeautifulSoup

linkSearchPrefix = "href="
validTagsFirstParagraph = ["b", "a", "i", "li"]
mech = Browser()


def get_next_target(page):
	linkNotFound = True
	url = ""

	while(linkNotFound):
	    start_link = page.find(linkSearchPrefix)
	    if start_link < 0: 
	        return 0
	    else:
		    start_quote = page.find('"', start_link)
		    end_quote = page.find('"', start_quote + 1)
		    url = page[start_quote + 1:end_quote]
		    if url[0] <> "#" and url[3] <> "/":
		    	linkNotFound = False
		    else:
		    	page=page[end_quote+1:]
	return url


def checkParagraph(paragraph):

	indexFirstOpeningBracket = paragraph.find("(")

	indexFirstLink = paragraph.find(linkSearchPrefix)
	
	if(indexFirstLink < 0):
		return 0
	else:
		if(indexFirstOpeningBracket>0 and indexFirstLink>indexFirstOpeningBracket):
			paragraph = paragraph[indexFirstOpeningBracket:]
			indexFirstClosingBracket = paragraph.find(")")
			paragraph = paragraph[indexFirstClosingBracket:]
		return get_next_target(paragraph)


def getForwardingLink(uri):
	response = mech.open(uri)

	soup = BeautifulSoup(response)

	contentResultSet = soup.find_all("div", id="mw-content-text")[0].findChildren(recursive=False)

	for tag in contentResultSet:
		if((tag.name == "p" or tag.name == "ul") and len(tag.getText())>5 and tag.findChild().name in validTagsFirstParagraph):
			link = checkParagraph(str(tag))
			if(link > 0):
				return link



