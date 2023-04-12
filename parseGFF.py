#! /usr/bin/env python3

# import modules
import argparse
import csv
from Bio import SeqIO


# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script parses a GFF file")

# add positional (required) arguments
parser.add_argument("gff", help="Name of the GFF file to parse", type=str)
parser.add_argument("fasta", help="Name of the FASTA file to parse", type=str)

# parse the actual arguments
# access argument values via `args` variable
args = parser.parse_args()

# open the GFF file
with open(args.gff) as gff_file:

	# create a csv reader object
	reader = csv.reader(gff_file,delimiter='\t')

	# loop over all the lines in the file
	for line in reader:

		# skip blank lines
		if not line:
			continue
		
		# if it's not a blank line, do this:
		else:

			# give variable names to the columns
			organism 		= line[0]
			source 			= line[1]
			feature_type 	= line[2]
			start 			= int(line[3])
			end 			= int(line[4])
			strand			= line[6]
			feature_attr	= line[8]

			# calculate the length of the feature and assign to column 5
			line[5]	= str(end - start + 1)
			# give variable name to column 5
			feature_length = line[5]

			# join the list into a variable called new_line and print to output
			new_line = '\t'.join(line)
			print(new_line)
			
			# # print(feature_type + '\t' + str(feature_length))






