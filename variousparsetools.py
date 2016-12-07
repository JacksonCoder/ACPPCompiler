from parse import *
import tokenparser as tp
def isIfStatement(string):
    result = parse("if {}",string)
    if result == None:
        return False
    return True
def isInlineIfStatement(string):
    result = parse("if {}-> {}",string)
    if result == None:
        return False
    return True
def ifStatementParse(string):
    result = parse("if {}")
    boolean_value = result.fixed[0]
    return tp.Token(
        'if (' + boolean_value + '){',
        'ifstatement'
        )
def inlineIfStatementParse(string):
    result = parse("if {}-> {}",string)
    boolean_value = result.fixed[0]
    inline_if_token = tp.parseToken(result.fixed[1])
    return tp.Token(
            'if(' + boolean_value + ') ' + inline_if_token,
            'inlineifstatement'
            )
