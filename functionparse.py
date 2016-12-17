import arglist

from parse import *

import tokenparser as tp

import variousparsetools

def isFunctionDefwithArgs(line):

    result =  parse("{:w}({}):{:w}",line)

    if result == None:

        return False

    return True

def isFunctionDefwithoutArgs(line):

    result =  parse("{:w}():{:w}",line)

    if result == None:

        return False

    return True

def functionParse(line):
    vars = parse("{:w}({}):{}",line)

    name = vars.fixed[0]

    typename = vars.fixed[2]

    return tp.Token(typename+" " + name + "("+ arglist.arglistParse(vars.fixed[1]).string  + "){","funcwa")

def functionParsenoArgs(line): 

    vars = parse("{:w}({}):{}",line)

    name = vars.fixed[0]

    typename = vars.fixed[2]

    return typename+" " + name + "("+ arglist.arglistParse(vars.fixed[1])  + "){"

