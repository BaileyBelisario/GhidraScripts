#Find known vuln C functions
#@author 
#@category Functions
#@keybinding 
#@menupath 
#@toolbar 


#TODO Add User Code Here

from java.awt import Color


vulnList = ['gets', 'strcpy', 'free', 'memcpy', 'alloca']

function = getFirstFunction()
functions = []
functions.append(function)

while function is not None:
	function = getFunctionAfter(function)
	functions.append(function)

finalvuln = []

for x in vulnList:
	for i in functions:
		if x == str(i):
			finalvuln.append(i)
ref = []

for x in finalvuln:
	x.setComment("Vulnerable Function")
	setBackgroundColor(x.getEntryPoint(), Color.cyan)
	ref.append(getReferencesTo(x.getEntryPoint()))

print(ref)
