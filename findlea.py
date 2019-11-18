#This script is meant to find every spot there is an LEA EAX instruction for functions, 
#enabling you to know offsets for potential buffer overflows. 
#@author Bailey Belisario
#@category Functions
#@keybinding 
#@menupath 
#@toolbar 


#importing the color library to highlight the LEA's
from java.awt import Color


#	Instruction is used to find each assembly instruction and 
#	I will traverse the program with it. The load list holds
#	every LEA EAX instruction. The comment list and value lists
#	are used for the instructions and values of the LEA with EBP
#	offsets.

#test

instruction = getFirstInstruction()
LoadList = []
ValueList = []
CommentList = []

while getInstructionAfter(instruction):
	instruction = getInstructionAfter(instruction)
	if 'LEA EAX' in str(instruction):					#Check to see if LEA EAX in instruction
		
		instruction.setComment(1,"Loading Memory for Function")		#Set Comment for each LEA EAX
		setBackgroundColor(instruction.getAddress(),Color.pink)		#Set instruction to pink (easy on eyes)
		LoadList.append(instruction)
		
		x = 0
		
		while x < len(LoadList):				#Traverse LoadList to find EBP offsets
			tmp_instruction = LoadList[x]			#Temporary instruction for the EBP offset
			LoadList[x] = str(LoadList[x])			#Convert instruction to string
			LoadList[x] = LoadList[x][9:-1]			#Cut off "LEA EAX,[" to make manipulation easy
			if 'EBP' in LoadList[x]:			#Find EBP in instructions
				LoadList[x] = LoadList[x][::-1]		#	Reverse the string to and append instructions
				ValueList.append(LoadList[x])		#	to value and comment lists
				CommentList.append(tmp_instruction)
			
			x += 1


for spot in range(0,len(ValueList)):
	ValueList[spot] = ValueList[spot][:ValueList[spot].find(' ')]	#Find spot where ' ' is and cut string to that point
	ValueList[spot] = ValueList[spot][::-1]				#Reverse the string back to original form
	ValueList[spot] = int(ValueList[spot], 16)			#Convert the hex string to int decimal format



#Print out the comment with offset of bytes for LEA EAX with EBP offset

for i in range(0,len(CommentList)):
	CommentList[i].setComment(1,"Loading Memory for Function\nBytes to EBP: {}".format(abs(ValueList[i])))
	

	

		
	