import sys

if(len(sys.argv) != 2):
	print "usage: python some_features.py <file_name>\nFirst token should be tweet token"
	sys.exit(0)

args = sys.argv
ip_file_name = args[1]

ip_file_object = open(ip_file_name)

ip_file = ip_file_object.readlines()

n = len(ip_file)

i=0
while(i < n):
	line = ip_file[i]
	tokens = line.split()
	