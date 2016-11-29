from parse import *

def append_semicolon(input):
	if input[-1] != ';':
		input = input + ';'
	return input
		
		
def varInitialize(line):
	tags = [] #used for templates
	array = False #boolean variable
	
	for r in findall("{:w}->",line):
		tags.append(r.fixed[0]) #appending tags
	if len(tags) == 0:
		print "Error... no type! Please assign a type to the variables."
		return ""
	type = tags[0]
	tags.remove(type)
	for tag in tags:
		if tag == 'array':
			array = True
		
	name = ""
	if search("->{:w}",line) == None:
		print "Error... you have no name for your variable."
		return ""
	else:
            lastobjectlist = []
            lastobjectiterator = findall("->{:w}",line)
            for lo in lastobjectiterator:
                lastobjectlist.append(lo)
            name = lastobjectlist[-1].fixed[0]
	
        #if supported("array") #add later, when supported function is added
        type = "std::vector"
        for tag in tags: #handles templatizing parameters
            type += "<" + tag
        for tag in tags:
            type += " >"
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
	
