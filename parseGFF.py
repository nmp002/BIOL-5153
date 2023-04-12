#! /usr/bin/env python3

# import modules
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script parses a GFF file")

# add positional (required) arguments
parser.add_argument("gff", help="Name of the GFF file to parse", type=str)
parser.add_argument("fasta", help="Name of the FASTA file to parse", type=str)

# parse the actual arguments
# access argument values via `args` variable
args = parser.parse_args()

# open the GFF file
with open(args.gff) as x:

	# loop over all the lines in the file
	for line in x:
		line.rstrip()
		properties = line.split('\t')
		feature_type = properties[2]
		feature_start = int(properties[3])
		feature_end = int(properties[4])
		feature_length = feature_end - feature_start + 1
		
		print(feature_type + '\t' + str(feature_length))






