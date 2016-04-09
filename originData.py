import numpy as np

# Params = Name of File
# number of header lines
def loadData(filename, headerLines):
	import os
	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
	ch = []
	start = []
	end = []
	name = []
    
	with open( os.path.join(__location__, filename), 'r') as f:
        
		for line in f:
			if(headerLines > 0):
				headerLines -= 1
				continue
			p = line.split(",")
			ch.append(int(p[0][1:-1]))
			start.append(int(p[1][1:-1]))
			end.append(int(p[2][1:-1]))
			name.append(int(p[3][7:-2]))
	return ch, start, end, name


ch, start, end, name = loadData("or.txt", 1)

print "name : (chr) start end"

for f in range(len(ch)):
	print name[f], ": (", ch[f], ")" , start[f], end[f], "\n"
	print "length of sequence", end[f]-start[f]
	print "\n"
