from parse import *

import tokenparser as tp

def isDeclaration(string):

    result = parse("{:w}:{} = {}",string)
    
    if result == None:

        result = parse("{:w}:{}",string)

        if result == None:

            return False
	print 'its a declaration!' + string
    return True

def declarationParse(string):

    result = parse("{:w}:{}={}",string)

    if result == None:

        result = parse("{:w}:({}){}<{}>",string)

        if result == None: # no internal AND templatized parameters

            result = parse("{:w}:({}){}",string)

            if result == None: #no internal parameters

                result = parse("{:w}:{}<{}>",string)

                if result == None: #just var declaration

                    result = parse("{:w}:{}",string)

                    name = result.fixed[0]

                    vartype = result.fixed[1]

                    return tp.Token(

                            vartype + ' ' + name,

                            "dec"

                            )

                name = result.fixed[0]

                vartype = result.fixed[1]

                templateargs = result.fixed[2]

                return tp.Token(

                        vartype + '<' + templateargs + '>' + ' ' + name,

                        "dec"

                        )
            name = result.fixed[0]
            
            specialargs = result.fixed[1]
            
            vartype = result.fixed[2]
            
            return tp.Token(
            		
            		specialargs + vartype + name, #fix this later
            		'dec'
            		)
    return tp.Token(
    result[1] + ' ' + result[0] + '=' + result[2],
    'dec'
    )   

def isType(string):

    result = parse("({}){}",string).fixed

    if result == None:

        result = [string]

        return result

    else:

        return ' '.join(','.join(arglistParse(result[0]))) + result[1]

    

