import sys

if(len(sys.argv) != 3):
	print "usage: python accuracy_check.py <system_predicted_file> <gold_set_file>"
	sys.exit(0)

args = sys.argv
op_file_name = args[2]
ip_file_name = args[1]

ip_file_object = open(ip_file_name)
op_file_object = open(op_file_name)

ip_file = ip_file_object.readlines()
op_file = op_file_object.readlines()

n = min(len(ip_file),len(op_file))

total = 0.0
correct_predicted = 0.0

i=0
while(i < n):
	predicted = ip_file[i]
	gold = op_file[i]
	# Split
	if(gold.strip() == ""):
		i=i+1
		continue
	gold_tokens = gold.split()
	predicted_tokens = predicted.split()
	# Compare
	total = total +1
	if(gold_tokens[1] == predicted_tokens[1]):
		correct_predicted = correct_predicted +1
	i=i+1

ip_file_object.close()
op_file_object.close()


print "Total:" + str(total)
print "Correct Predicted:" + str(correct_predicted)
print "F-Score:" + str(correct_predicted/total)