from functionparse import *

	


def parsed(input):
	if "define" in input:
		return functionParse(input)
	elif search("->",input) != None:
		return isInitialization(line_input)
	
print "Welcome to the A-C++ compiler!"
print "Enter a line to compile it!"
line_input = raw_input()
print varInitialize(line_input)
print parsed(line_input)