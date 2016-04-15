import json
import sys
from pprint import pprint

if(len(sys.argv) != 2):
	print "usage: python accuracy_check.py <file_name>"
	sys.exit(0)


args = sys.argv
file_name = args[1]

tweets = []
for line in open(file_name, 'r'):
    tweets.append(json.loads(line))

for tweet in tweets:
	print tweet['original'].encode('utf-8')

'''for i in range(0,len(data)):
	tweet = data[i]["original"]
	print tweet'''