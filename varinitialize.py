from parse import *
from tokenparser import *
from arglist import *
#from typeclass import *
import re
def isDeclaration(string):
    result = parse("{:w}:{} = {}",string)
    if result == None:
        result = parse("{:w}:{}",string)
        if result == None:
            return False
    return True
def isTypeToken(string):
    result = parse("({}){}",string).fixed
    if result == None:
        result = [string]
        return result
    else:
        return ' '.join(','.join(arglistParse(result[0]))) + result[1]
    
