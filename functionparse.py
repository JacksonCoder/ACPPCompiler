from varinitialize import *
def functionParse(line):
	if search("define {:w}",line) == None:
		return "Error... not a function!"
	args = findall("{:w},",line)
	
	ret = []
	for a in args:
		ret.append(a.fixed[0])
	endvar = search("{:w})",line)
	if endvar != None: ret += endvar.fixed[0]
	return ret
		