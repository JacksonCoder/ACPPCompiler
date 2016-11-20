from parse import *
class ProgramState:
	def append_semicolon(self,input):
		if input[-1] != ';':
			input = input + ';'
		return input
	def var_Initialize(self,line):
		tag = []
		for r in findall("->{:w}",line):
			tag.append(r.fixed[0])
		return tag

	def __init__(self,name):
		self.variables = []
		self.error = False
		self.name = name
def append_semicolon(input):
	if input[-1] != ';':
		input = input + ';'
	return input	
	
def isInitialization(line_input,state):
	"""
	TODO
	Make sure to seperate initialization part from declaration part
	Parse string before/after "=" sign
	Also modulate following code into functions
	Deadline: Saturday, November 19, 2016
	(Good luck to myself)
	"""
	tags = state.var_Initialize(line_input)
	type = tags[0]
	if "pointer" in line_input:
		type += '*'
	if "array" in line_input:
		size = search("[{}]",line_input).fixed[0]
		array = True
	else:
		array = False
	for tag in tags:
		line_input = line_input.replace(type,"")
	line_input = line_input.replace("var->","")
	line_input = line_input.replace("pointer->","")
	line_input = line_input.replace("array->","")
	line_input = line_input.replace("["+search("[{}]",line_input).fixed[0]+"]","")
	line_input = append_semicolon(line_input)
	if array:
		return type + line_input + "[" + size + "]"
	else:
		return type + line_input

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