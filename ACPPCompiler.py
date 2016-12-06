from functionparse import *
from tokenparser import *
print "using regular expressions!"
print "Welcome to the A-C++ compiler!"
print "Enter a line to compile it!"
line_input = raw_input()
print "Work in progress"
print parseToken(line_input).string
