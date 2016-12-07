import tokenparser as tp

#Main controller
class ParseController:
    def processLine(self,line):
        token = tp.parseToken(line)
        if token.type != 'func':
            token.string += ';'
        return token
print "What file do you want to read from?"
readfile = open(raw_input(),'r')
#print "What file do you want to write from?"
#writefile = open(raw_input(),'w')
pc = ParseController
contents = readfile.read()
linelist = contents.split('\n')
for line in linelist:
 #   writefile.write(pc.processLine(line))
 print pc.processLine(line).string
