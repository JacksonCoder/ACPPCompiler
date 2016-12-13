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

    def __init__(self,linelist):

        self.contents = linelist

        self.submodules = []

        self.submodulespaces = {}

        self.parentmodule = None

        self.scopedvariables = []

        self.parsedcontents = []

    def createSubModule(self,mod,place):

        self.submodules.append(mod)

        self.submodulespaces[place] = mod

        self.submodules[len(self.submodules)-1].parentmodule = self

    def internalParse(self):
        print len(self.contents)
        for i in range(0,len(self.contents)):
            line = self.contents[i]
            print line
            if i in self.submodulespaces:
                
                self.submodules = self.submodulespaces[i].internalParse()

                self.parsedcontents.append(self.submodules[i].parsedcontents)

            parsedline = tp.parseToken(line)

            if parsedline.tokentype == 'dec' or parsedline.tokentype == 'funccall' or parsedline.tokentype == 'assign':

                parsedline += ';' #can't forget that semicolon!

            self.parsedcontents.append(parsedline.string)
        return self

print "What file do you want to read from?"

readfile = open(raw_input(),'r')

#print "What file do you want to write to?"

#writefile = open(raw_input(),'w')

contents = readfile.read()

linelist = contents.split('\n')

#seperate linelist into modules

def makeModule(linelist,tabnumber):

    i = 0
    
    returnmodule = Module(linelist)

    while i < len(linelist)-1:

        if linelist[i].count('\t') > tabnumber:

            tabnumber += 1
            
            internaliterator = 0
            
            subparsed = []
            print 'in1'

            while linelist[internaliterator].count('\t') >= tabnumber:

                subparsed.append(linelist[internaliterator] + '\n')

                returnmodule.contents.pop(internaliterator) #This removes contents that are implemented in a submodule
                internaliterator += 1
            print 'in'
            returnmodule.createSubModule(makeModule(subparsed,tabnumber),internaliterator)
            if linelist[internaliterator].count('\t') < tabnumber-1:
                return returnmodule
            i = internaliterator
        i += 1
    print returnmodule.contents
    return returnmodule
mod = makeModule(linelist,0)
mod.internalParse()
print mod.submodules
print '\n'.join(mod.parsedcontents)
