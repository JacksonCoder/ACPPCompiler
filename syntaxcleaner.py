from parse import *

def syntaxClean(string):
	string = string.strip('\t')
	string = string.replace(' ','')
	return string