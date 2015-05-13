#!/usr/bin/python

import random
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("numtags", help="number of tags to generate", type=int)
parser.add_argument("prefixes", help="file containing prefix words, one per line")
parser.add_argument("colors", help="file containing colors, one per line")
parser.add_argument("current", help="file with list of currently existing tags, if any")
parser.add_argument("-u", "--uppercase", help="output tags in uppercase", action="store_true")
args = parser.parse_args()

currentlist = args.current
colorlist = args.colors
prefixlist = args.prefixes

prefixes = []
colors = []
existing = []
output = []

with open(prefixlist) as f:
	prefixes = f.read().splitlines()

with open(colorlist) as f:
	colors = f.read().splitlines()

with open(currentlist) as f:
	existing = [re.split('\s_,|/]+', tag) for tag in f.read().splitlines()]


def generate_tag(n):
	tag = []
	while len(output) < n:
		tag = [ random.choice(prefixes), random.choice(colors) ]
#		print "Trying " + str(tag)
		if tag not in existing:
#			print "OK"
			output.append(tag)
#		else:
#			print "Failed, exists!"
			 

generate_tag(args.numtags)

#	print existing

for i in output:
	if args.uppercase:
		print i[0].upper() + "_" + i[1].upper()
	else:
		print i[0] + "_" + i[1]
