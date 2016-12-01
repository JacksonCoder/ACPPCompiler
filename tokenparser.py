from varinitialize import *
from functionparse import *
from loopparser import *

class PositionInfo:
   def  __init__(self):
        self.line = 0 #line number
        self.type = '' 


def parseToken(line):
    pos = PositionInfo()
    #check if it is a function
    #if isFunction(line,pos)
    #   get line as a parsed function and return
    #part of all of these functions is to call this function recursively
    #we return a special class object with a type and string part
