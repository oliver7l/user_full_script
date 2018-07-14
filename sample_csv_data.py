import sys
import random

file_name = sys.argv[1]
with open(file_name) as f,open(file_name + '.sample','a+') as f_out:
	for line in f:
		if 'header' not in vars():
			header = line.strip()
			f_out.write(header + '\n')
		else:
			info = line.strip()
			if random.randint(1,100) == 1:
				f_out.write(info + '\n')
