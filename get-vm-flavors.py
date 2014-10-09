#!/usr/bin/python
import argparse
import string
import os
import urllib
import httplib
import re
import sys, traceback
import time
import json
import logging

# Define files to be used
novashow = open('./nova_list_all', 'r')
x=0
listoflists = []
record = []
print "hello"
record = ["Instance ID", "User ID", "Tenant Name", "Tenant-ID", "Flavor", "VM Name", "Host", "Config Drive\n"]
listoflists.append(record)
record = []
# Loop through novahow info and print out data
for line in novashow.readlines():
#	print (line)
	temp = line.split("| ")
	print "Instance ID  %s" % temp[1]
	record.append(temp[1])
#	print "User ID %s" % temp[1]
#	print "Tenant ID %s" % temp[3]
	found=0
        for templine in open('./keystone-user-list').readlines():
		if temp[2] in templine:
			print "have userid %s" % temp[2]
			ttemp = templine.split()
			print "have username %s" % ttemp[3]
                        record.append(ttemp[3])
			found = 1
			break

	if found == 0:
		print "did not find userid. Insert id number"
		record.append(temp[2])		
	found =0
        for templine in open ('./keystone-tenant-list').readlines():
		if temp[3] in templine:
			print "have tenantid %s" % temp[3]
			ttemp = templine.split()
			print "have tenant name %s" % ttemp[3]
                        record.append(ttemp[3])
			record.append(temp[3])
			found =1
			break
	if found == 0:
		print "did not find tenant id. Insert id number"
		record.append(temp[3])		
		record.append(temp[3])		

	found =0
        for templine in open ('./nova-flavor-list').readlines():
		if temp[4] in templine:
			print "have flavor %s" % temp[3]
			ttemp = templine.split()
			print "have flavor name %s" % ttemp[3]
			found =1
                        record.append(ttemp[3])
	if found == 0:
		print "did not find flavor id. Insert id number"
		record.append(temp[4])		

	print "name ID %s" % temp[5]
	record.append(temp[5])
	print "host is %s" % temp[6]
	record.append(temp[6])
	print "config drive is %s " % temp[7]
	record.append(temp[7])
	listoflists.append(record)
	x = x+1
	record = []

		
#print (len(listoflists))
output = open('./output', 'w')
for item in listoflists:
        stringconvert= ",".join(item)
        stringconvert= stringconvert.translate(None, '\'\]\[')
        output.write("%s" % stringconvert)

output.close()

