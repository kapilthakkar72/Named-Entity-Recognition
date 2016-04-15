import sys

if(len(sys.argv) != 3):
	print "usage: python accuracy_check.py <system_predicted_file> <tweet_file>"
	sys.exit(0)

args = sys.argv
op_file_name = args[2]
ip_file_name = args[1]

ip_file_object = open(ip_file_name)
op_file_object = open(op_file_name)

ip_file = ip_file_object.readlines()
op_file = op_file_object.readlines()

n = min(len(ip_file),len(op_file))

for i in range(0,n):
	print ip_file[i].strip() + " " + op_file[i].strip()

ip_file_object.close()
op_file_object.close()