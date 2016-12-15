import tokenparser as tp




class Module:

    def __init__(self,linelist):

        self.contents = linelist

        self.submodules = []

        self.submodulespaces = {}

        self.parentmodule = None

        self.scopedvariables = []

        self.parsedcontents = []

    def createSubModule(self,mod,place):
    	print 'creating sm!'

        self.submodules.append(mod)
        #print self.submodules[len(self.submodules)-1]
		
        self.submodulespaces[place] = mod
        self.submodules[len(self.submodules)-1].parentmodule = self

    def internalParse(self):
        print 'called'
        for i in range(0,len(self.contents)):
        
            line = self.contents[i]
            
            if i in self.submodulespaces:
                
                old_state = self.submodulespaces[i]
                
                self.submodulespaces[i].internalParse()
                
                self.submodules[self.submodules.index(old_state)] = self.submodulespaces[i]

                self.parsedcontents.append(self.submodules[self.submodules.index(old_state)].parsedcontents)

            parsedline = tp.parseToken(line)

            if parsedline.tokentype == 'dec' or parsedline.tokentype == 'funccall' or parsedline.tokentype == 'assign':

                parsedline += ';' #can't forget that semicolon!

            self.parsedcontents.append(parsedline.string)

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
            
            print linelist[i]
            
            internaliterator = i
            
            subparsed = []
            
            subparsed.append(linelist[i])
            
            while linelist[internaliterator].count('\t') >= tabnumber:
            

                
                subparsed.append(linelist[internaliterator] + '\n')

                returnmodule.contents.pop(internaliterator) #This removes contents that are implemented in a submodule
                       
                internaliterator += 1

                
            
            returnmodule.createSubModule(makeModule(subparsed,tabnumber),internaliterator)
            
            if linelist[internaliterator].count('\t') < tabnumber-1:
            
                return returnmodule
                
            i = internaliterator
            
        i += 1
        
    print returnmodule.contents
    
    return returnmodule
    
mod = makeModule(linelist,0)

mod.internalParse()

print mod.submodulespaces

print mod.parsedcontents

