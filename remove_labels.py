import sys

if(len(sys.argv) != 3):
	print "usage: python remove_labels.py <file_name> <label_file>"
	sys.exit(0)

args = sys.argv
ip_file_name = args[1]

ip_file_object = open(ip_file_name)
ip_file = ip_file_object.readlines()

file = open(args[2],'w')

for line in ip_file:
	if(line.strip() != ""):
		tokens = line.split()
		print tokens[0]
		file.write(tokens[1] + "\n" ) 
	else:
		print ""
		file.write("\n" ) 

ip_file_object.close()
file.close()