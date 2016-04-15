import sys

if(len(sys.argv) != 3):
	print "usage: python remove_labels.py <file_name> <label_file>"
	sys.exit(0)

args = sys.argv
ip_file_name = args[1]

ip_file_object = open(ip_file_name)
ip_file = ip_file_object.readlines()

ip_file_object = open(args[2])
ip_file2 = ip_file_object.readlines()

for i in range(0,len(ip_file)):
	if(ip_file[i].strip() == "" and ip_file2[i].strip()!= ""):
		print i
		break

ip_file_object.close()