filepath = 'input.txt'  
with open(filepath) as fp:  
	line = fp.readline()
	cnt = 1
	while line:	
		line = line.strip()
		tokens = line.split("\\")
		print(tokens)
		if len(tokens) < 5:continue
                print(tokens[4])
		line = fp.readline()
		
