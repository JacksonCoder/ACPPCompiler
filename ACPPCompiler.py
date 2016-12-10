import tokenparser as tp

#Main controller

class ParseController:

    #This is the subcontainer with all the file parse functions and the arrays of internal data

    def __init__(self):

        pass

    def processLine(self,line):

        token = tp.parseToken(line)

       # if token.type != 'func':

        #    token.string += ';'

        return token

class Module:

    def __init__(self,line):

        self.contents = line.split('\n')

        self.submodules = []

        self.submodulespaces = []

        self.parentmodule = None

        self.scopedvariables = []

        self.parsedcontents = []

    def createSubModule(self,mod,place):

        self.submodules.append(mod)

        self.submodulespaces.append(place)

        submodules[len(submodules)-1].parentmodule = self

    def internalParse(self):
        unparsedlist = contents

        for i in range(0,len(unparsedlist)):
            line = unparsedlist[i]

            if i in self.submodulespaces:

                

            parsedline = tp.parseToken(line)

            if parsedline.type == 'dec' or parsedline.type = 'funccall' or parsedline.type = 'assign':

                parsedline += ';' #can't forget that semicolon!

            self.parsedcontents.append(

print "What file do you want to read from?"

readfile = open(raw_input(),'r')

#print "What file do you want to write to?"

#writefile = open(raw_input(),'w')

contents = readfile.read()

linelist = contents.split('\n')

#seperate linelist into modules

def makeModule(linelist):

    tabnumber = 0

    result = ''

    i = 0

    returnmodule = Module(linelist)

    while i < len(linelist)-1:

        if linelist[i].count('\t') > tabnumber:

            result = ''

            tabnumber += 1
            
            internaliterator = 0

            while linelist[i].count('\t') == tabnumber

                result += linelist[i] + '\n'

                internaliterator += 1

                returnmodule.contents.pop(internaliterator) #This removes contents that are implemented in a submodule

            if linelist[i].count('\t') > tabnumber:
                
            returnmodule.createSubModule(parseModule(linelist[i:internaliterator],i)

            elif linelist[i].count('\t') < tabnumber-1:

                return returnmodule
        i += 1

    #iterate through the list
def run():
    finalmodule = makeModule(linelist)
    finalmodule.internalParse()
    print '\n'.join(finalModule.parsedcontents)
