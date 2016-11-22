from parse import *

def getSymbol(type):
	if type == 'pointer':
		return '*'
	if type == 'reference':
		return '&'
	return ''
class ProgramState:

	def append_semicolon(self,input):
		if input[-1] != ';':
			input = input + ';'
		return input
		
		
	def varInitialize(self,line):
		tags = [] #holds all tags for type
		array = False #for later...
		
		for r in findall("{:w}->",line):
			tags.append(r.fixed[0]) #appending tags
		if len(tags) == 0:
			self.error = True
			print "Error... no type! Please assign a type to the variables."
			return ""
		type = tags[0]
		tags.remove(type)
		for tag in tags:
			type += getSymbol(tag)
			if tag == 'array':
				array = True
		
		name = ""
		if search("->{:w} ",line) == None:
			self.error = True
			print "Error... you have no name for your variable."
			return ""
		else:
			name = search("->{:w} ",line).fixed[0]
		if array:
			line = line.replace("["+search("[{}]",line).fixed[0]+"]","")
			return type + " " + name + "[" + size + "]"
		else:
			return type + " " + name
		
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
	
	declaration = state.varInitialize(declaration)
	if '=' in line_input:
		return state.append_semicolon(declaration + " = " + initialization)
	else:
		return state.append_semicolon(declaration + initialization)
	
	


def parsed(input,state):
	if search("var->",input) != None or search("pointer->",input) != None or search("array->",input) != None:
		return isInitialization(input,state)
	"""
	elif it is a function
	TODO
	implement function handling
	deadline: 
	"""
	
print "Welcome to the A-C++ compiler!"
print "Enter a line to compile it!"
line_input = raw_input()
ps = ProgramState("")
print ps.varInitialize(line_input)
print parsed(line_input,ps)