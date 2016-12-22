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
    
    def doModulePreparation(self):
		self.contents.append('}')
		for s in self.submodules:
			s.doModulePreparation()
	
    def internalParse(self):
        print self.submodulespaces
        for i in range(0,len(self.contents)):
            line = self.contents[i]
            
            if self.contents[i-1] in self.submodulespaces and i - 1 > -1:
                
                old_state = self.submodulespaces[self.contents[i-1]]
                
                self.submodulespaces[self.contents[i-1]].internalParse()
                
                self.submodules[self.submodules.index(old_state)] = self.submodulespaces[self.contents[i-1]]
                
                print self.submodules[self.submodules.index(old_state)].parsedcontents
                for a in self.submodules[self.submodules.index(old_state)].parsedcontents:
                	self.parsedcontents.append(a)
            
            parsedline = tp.parseToken(line)
            '''
            if parsedline.tokentype == 'dec' or parsedline.tokentype == 'funccall' or parsedline.tokentype == 'assign':

                parsedline += ';' #can't forget that semicolon!
            '''
            self.parsedcontents.append(parsedline.string)
            
        self.parsedcontents.append('}')

print "What file do you want to read from?"

readfile = open(raw_input(),'r')

#print "What file do you want to write to?"

#writefile = open(raw_input(),'w')

contents = readfile.read()

linelist = contents.split('\n')

#seperate linelist into modules

def makeModule(linelist,tabnumber):

    i = 0 #used as our primary list iterator
    
    returnmodule = Module([]) #The module that is returned by this recursive sequence

    while i < len(linelist): 

        if linelist[i].count('\t') > tabnumber:
            tabnumber += 1 #passed recursively
            position = returnmodule.contents[-1]
            internaliterator = i
            
            subparsed = []
            
            subparsed.append(linelist[i])
            while linelist[internaliterator].count('\t') >= tabnumber and internaliterator < len(linelist)-1:
                       
                internaliterator += 1
                subparsed.append(linelist[internaliterator])

            subparsed.pop()
            returnmodule.createSubModule(makeModule(subparsed,tabnumber),position)
            
            i = internaliterator
            returnmodule.contents.append(linelist[i])
    	else: returnmodule.contents.append(linelist[i])
        i += 1
        
    print returnmodule.contents #debug
    
    return returnmodule
    
mod = makeModule(linelist,0)

#mod.doModulePreparation()

mod.internalParse()

print '\n'.join(mod.parsedcontents)

