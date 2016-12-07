import arglist
from parse import *
import tokenparser as tp
import variousparsetools
def isFunctionDefwithArgs(line):
    result =  parse("define {:w}({}) {:w}",line)
    if result == None:
        return False
    return True
def isFunctionDefwithoutArgs(line):
    result =  parse("define {:w}() {:w}",line)
    if result == None:
        return False
    return True
def functionParse(line):
    vars = parse("define {:w}({}) {}",line)
    name = vars.fixed[0]
    typename = vars.fixed[2]
    return tp.Token(typename+" " + name + "("+ arglist.arglistParse(vars.fixed[1])  + "){","funcwa")
def functionParsenoArgs(line): 
    vars = parse("define {:w}({}) {}",line)
    name = vars.fixed[0]
    typename = vars.fixed[2]
    return typename+" " + name + "("+ arglist.arglistParse(vars.fixed[1])  + "){"
