from loopparser import *
import varinitialize as vi
import functionparse as fp
import variousparsetools as vpt
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
    
    if vpt.isInlineIfStatement(line):

        return vpt.inlineIfStatementParse(line)

    if vpt.isIfStatement(line):

        return vpt.ifStatementParse(line)

    return line
