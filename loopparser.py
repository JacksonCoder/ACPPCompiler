from parse import *
'''
Handles parsing of if/while/for statements and adds a few more...
In progress
---------------------------
'''
def ifLoop(line):
    #basic checking here
    if "if" not in line:
        print "Error... this shouldn't have happened"
    #get boolean argument
    argvalue = search("if {}",line).fixed[0]
    if argvalue == None:
        print "Error... 'if' function needs a argument"
    return "if (" + argvalue + "){"
def whileLoop(line): 
    #basic checking here
    if "while" not in line:
        print "Error... this shouldn't have happened"
    #get boolean argument
    argvalue = search("while {}",line).fixed[0]
    if argvalue == None:
        print "Error... 'while' function needs a argument"
    return "while (" + argvalue + "){"
def forLoop(line):
    if search("for {},{},{}",line) != None:
        #do for loop regular stuff
