from varinitialize import *
from arglist import *

def isFunctionDef(line):
    result =  parse("define {:w}({}) {:w}",line)
    if result == None:
        return False
    return True
    
def functionParse(line):
    vars = parse("define {:w}({}) {}",line)
    name = vars.fixed[0]
    typename = vars.fixed[2]
    #parse argument list
    parsed_argument_list = arglistParse(line)
    return typename+" " + name + "("+ passed_argument_list  + "){"
