import os.path


def showPhilosophersPage():
	page = open(os.path.dirname(__file__) + "/pages/philosophers.html")
	return page.read()
