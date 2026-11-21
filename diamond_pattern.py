length = int(input("Enter your desired length: "));
total_lines = length*2-1
for line in range(total_lines):
	downward= line if line < length else total_lines-1-line
	space = length-1-downward
	star = downward*2 - 1
	print(" "*space,"*"*star)
