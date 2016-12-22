from loopparser import *

import varinitialize as vi

import functionparse as fp

import syntaxcleaner as sc

class ParseLevel:
	
	def __init__(self):
	    
	    self.types = ['top','front','back','lowest','comment']
	    
	    self.type = ''
class PositionInfo:

   def  __init__(self):

        self.parselevel = ParseLevel()

class Token:

    def __init__(self,string,tokentype):

        self.string = string

        self.tokentype = tokentype

def parseToken(token):
    token = sc.syntaxClean(token)
    print 'parsing ' + token
    if fp.isFunctionDefwithArgs(token):

        return fp.functionParse(token)

    if fp.isFunctionDefwithoutArgs(token):

        return fp.functionParsenoArgs(token)

    if vi.isDeclaration(token):

        return vi.declarationParse(token)
    print 'returning'
    return Token(
            token,
            'name'
            )

'''

    if vi.isType(line):

        return vi.typeParse(line)

'''

