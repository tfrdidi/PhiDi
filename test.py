import sys
sys.path.insert(0, 'libs')
from phiDi import phidi

def method(parameter):    
	return parameter

def callPhiDi(articleName):
	return phidi.getSampleDistance()

def django():
	return "hallo"