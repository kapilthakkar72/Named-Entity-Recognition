import sys

if(len(sys.argv) != 2):
	print "usage: python accuracy_check.py <file_name>"
	sys.exit(0)

args = sys.argv
ip_file_name = args[1]

ip_file_object = open(ip_file_name)
ip_file = ip_file_object.readlines()

for line in ip_file:
	if(line.strip() != ""):
		tokens = line.split()
		print tokens[0]
	else:
		print ""

ip_file_object.close()