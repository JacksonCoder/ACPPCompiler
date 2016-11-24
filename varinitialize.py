from parse import *
def getSymbol(type):
	if type == 'pointer':
		return '*'
	if type == 'reference':
		return '&'
	return ''


def append_semicolon(input):
	if input[-1] != ';':
		input = input + ';'
	return input
		
		
def varInitialize(line):
	tags = [] #holds all tags for type
	array = False #for later...
	
	for r in findall("{:w}->",line):
		tags.append(r.fixed[0]) #appending tags
	if len(tags) == 0:
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
		print "Error... you have no name for your variable."
		return ""
	else:
		name = search("->{:w} ",line).fixed[0]
	if array:
		line = line.replace("["+search("[{}]",line).fixed[0]+"]","")
		return type + " " + name + "[" + size + "]"
	else:
		return type + " " + name
	
	
def isInitialization(line_input):
	if '=' in line_input:
		parts = line_input.split("=") #split it at the equals sign
	else:
		parts = [line_input]
	initialization = ""
	declaration = parts[0]
	if len(parts) > 1: 
		initialization = parts[1]
	
	declaration = varInitialize(declaration)
	if '=' in line_input:
		return append_semicolon(declaration + " = " + initialization)
	else:
		return append_semicolon(declaration)
	