from varinitialize import *
def functionParse(line):
	if search("define {:w}",line) == None:
		return "Error... not a function!"
	args = findall("{},",line)
	
	argslist = []
	for a in args:
		argslist.append(a.fixed[0])
        if len(argslist) > 0:
	    endvar = search(",{})",line)
        else:
            endvar = search("({})",line)
	argslist.append(endvar.fixed[0])
	name = search("define {:w}(",line).fixed[0]
        typename = search(") {:w}",line).fixed[0]
        for i in range(0,len(argslist)):
            argslist[i] = varInitialize(str(argslist[i]))
            a = 0
        argsoutput = ""
        for string in argslist[0:len(argslist)-1]:
           argsoutput = argsoutput + string + ","
        argsoutput += argslist[len(argslist)-1]
        return typename+" " + name + "("+ argsoutput  + "){"
