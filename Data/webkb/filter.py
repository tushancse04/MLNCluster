import os
files = [f for f in os.listdir(".") if os.path.isfile(f)]
for f in files:
	if "test-" in f or "train-" in f:
		lines = ""	
		ifile = open(f)
		for l in ifile:
			if "!" not in l:
				lines += l
		ifile.close()
		ifile = open(f,'w')
		ifile.write(lines)
		ifile.close()
