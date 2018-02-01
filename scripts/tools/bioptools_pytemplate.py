import sys
import os
# Function uses to quickly print a template for script bioptools.py, which allows bioptool C scripts to be
# easily accessed through a python module. Can be copied into new file.
# argument should be /path/to/bioptools/src
def printFunctionsForTools():
	biopToolsDir = sys.argv[1]
	for file in os.listdir(biopToolsDir):
    	 if file.endswith(".c"):
        	functionname = os.path.splitext(file)[0]
         	print "def "+functionname+"(toolarg):"
         	print "	return subprocess.check_output(['"+biopToolsDir+"/"+functionname+"',toolarg])"

if __name__ == "__main__":
	printFunctionsForTools()