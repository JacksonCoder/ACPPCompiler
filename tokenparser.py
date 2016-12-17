from loopparser import *

import varinitialize as vi

import functionparse as fp

import syntaxcleaner as sc
class PositionInfo:

   def  __init__(self):

        self.line = 0 #line number

        self.type = '' 

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

