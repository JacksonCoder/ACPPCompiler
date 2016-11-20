from parse import *
class ProgramState:
	def append_semicolon(self,input):
		if input[-1] != ';':
			input = input + ';'
		return input
	def var_Initialize(self,line):
		tags = []
		class_type = search("{:w}->",line).fixed[0]
		for r in findall("->{:w}",line):
			tags.append(r.fixed[0])
		type = tags[0]
		if "pointer" in class_type:
			type += '*'
		if "array" in class_type:
			size = search("[{}]",line).fixed[0]
			array = True
		else:
			array = False
		for tag in tags:
			line = line.replace(type,"")
		line = line.replace("var->","")
		line = line.replace("pointer->","")
		line = line.replace("array->","")
		line = line.replace("["+search("[{}]",line).fixed[0]+"]","")
		if array:
			return type + line + "[" + size + "]"
		else:
			return type + line
		
	def __init__(self,name):
		self.variables = []
		self.error = False
		self.name = name
	
	
def isInitialization(line_input,state):
	parts = line_input.split("=") #split it at the equals sign
	initialization = ""
	declaration = parts[0]
	if len(parts) > 1: 
		initialization = parts[1]
	
	declaration = state.var_Initialize(declaration)
	
	return state.append_semicolon(declaration + "=" + initialization)
	
	


def parsed(input,state):
	if search("var->",input) != None or search("pointer->",input) != None or search("array->",input) != None:
		return isInitialization(input,state)
	"""
	elif it is a function
	TODO
	implement function handling
	deadline: 
	"""
	
print "Welcome to the B compiler!"
print "Enter a line to compile it!"
line_input = raw_input()
ps = ProgramState("")
print parsed(line_input,ps)