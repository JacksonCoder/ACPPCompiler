from loopparser import *

import varinitialize as vi

import functionparse as fp

class PositionInfo:

   def  __init__(self):

        self.line = 0 #line number

        self.type = '' 

class Token:

    def __init__(self,string,tokentype):

        self.string = string

        self.tokentype = tokentype

def parseToken(line):

    if fp.isFunctionDefwithArgs(line):

        return fp.functionParse(line)

    if fp.isFunctionDefwithoutArgs(line):

        return fp.functionParsenoArgs(line)

    if vi.isDeclaration(line):

        return vi.declarationParse(line)

    return Token(
            line,
            'name'
            )

'''

    if vi.isType(line):

        return vi.typeParse(line)

'''

