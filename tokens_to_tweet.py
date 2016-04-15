import sys

if(len(sys.argv) != 2):
	print "usage: python tokens_to_tweet.py <file_name>"
	sys.exit(0)

args = sys.argv
ip_file_name = args[1]

ip_file_object = open(ip_file_name)
ip_file = ip_file_object.readlines()

tweet = ""
for line in ip_file:
	if(line.strip() != ""):
		if(line.strip().find(".") == -1 and line.strip().find(",") == -1 and line.strip().find(";") == -1 and line.strip().find("?") and line.strip().find('"') == -1 ):
			tweet = tweet + " " + line.strip()
		else:
			tweet = tweet + line.strip()
	else:
		print tweet.strip()
		tweet = ""

ip_file_object.close()