from varinitialize import *
from functionparse import *
from loopparser import *
class PositionInfo:
   def  __init__(self):
        self.line = 0 #line number
        self.type = '' 


def parseToken(line):
    if isFunctionDef(line):
        return functionParse(line)
    if isDeclaration(line):
       # return declarationParse(line)
       pass
    #if isFunctionCall(line):    
    return line
