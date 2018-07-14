import sys
import random

for line in sys.stdin:
	if 'header' not in vars():
		header = line.strip()
		print header
	else:
		info = line.strip()
		if random.randint(1,100) == 1:
			print info
