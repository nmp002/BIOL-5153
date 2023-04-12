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

		# skip blank lines
		if not line.strip():
			continue
		
		# if it's not a blank line, do this:
		else:
			# remove the linebreak (white space) from the end of the line
			line.rstrip()

			# split line on tab character
			# this creates a list consisting of the line columns
			columns 		= line.split('\t')

			# give variable names to the columns
			organism 		= columns[0]
			source 			= columns[1]
			feature_type 	= columns[2]
			start 			= int(columns[3])
			end 			= int(columns[4])
			strand			= columns[6]
			feature_attr	= columns[8]

			# calculate the length of the feature and assign to column 5
			columns[5]	= str(end - start + 1)
			# give variable name to column 5
			feature_length = columns[5]

			new_line = '\t'.join(columns)
			print(new_line)
			
			# print(feature_type + '\t' + str(feature_length))






