#!/usr/bin/python
#
# lwatta
# Purpose: Open a host list and edit host files based on details in that list.
# Open hosts.txt read in host a and ip a, then go open hosta.yaml and change ip address in the file.
# most of the file should already be correct. I just need to change the ip.

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
# file input needed for rw of file
import fileinput
netmask = "255.255.255.192"
gateway= "10.23.194.195"
# Define files to be used
novashow = open('./host.txt', 'r')
x=0
listoflists = []
record = []
print "hello"
record = []
# Loop through novahow info and print out data
for line in novashow.readlines():
	temp = line.split()
	file = temp[0] + ".yaml"
        for templine in fileinput.input(file,inplace=True):
		if "ip_address" in templine:
			print "      ip_address: %s" % temp[1]
		elif "gateway" in templine:
			print "      gateway: %s" % gateway
		elif "netmask" in templine:
			print "      netmask: %s" % netmask
		else:
# Below the comma tells print not to print a newline
			print templine,

	fileinput.close()

		
#print (len(listoflists))
#output = open('./output', 'w')
#for item in listoflists:
#        stringconvert= ",".join(item)
#        stringconvert= stringconvert.translate(None, '\'\]\[')
#        output.write("%s" % stringconvert)

#output.close()

