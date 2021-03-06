
import re
from os import path
from collections import defaultdict, OrderedDict


def count_top_10(file):
	'''
	count_top_10 will count the top 10 ip addresses
	in a log file that shows the error code in the 
	second argument. 
	'''
	if not path.isfile(file):
		print ('Error: cannot find file', file)
		exit(1)
	ip_lst, code_lst = [], []
	d = OrderedDict()
	with open (file, 'r') as f: 
		for line in f: 
			reg1 = r'(^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*"\s(\d{3})\s'
			match = re.search(reg1, line)
			if match:
				ip = match.group(1)
				code = match.group(2)
			
			# Get list of ips and codes 
			ip_lst.append(ip)
			code_lst.append(code)
			
			# Make a dic from the regex 
			# d2 = match.dictgroup()

			for x in ip_lst: 
				d[x] = ip_lst.count(x)
		
		print (sorted(d.values()))
		print(d)
		# for k, v in d.items():
		# 	print (k, v) 
		# print ("----")
		# for i in range(len(ip_lst)):
		# 	print (ip_lst[i], code_lst[i])
		# # print (d)

# print (lst) 
count_top_10('apache.log')

