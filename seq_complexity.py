#import packages
import pandas
import matplotlib.pyplot as plt
import sys
import os
from seq import *

#create main function that reads in the file, and makes a folder for each species
#within each species folder, this function uses the seq.py script to output 4 files
#1) a new fasta file that contains only the sequence for that species, 2) a png file
#that contains a graph of the kmer size on the x-axis and the proportion of observed/possible
#kmers on the y-axis for that species, 3) a csv file of the dataframe of kmer size,
#observed kmers, and possible kmers, and their totals for that species, and 4) a txt
#file that contains the calculated linguistic complexity (i.e. total observed kmers/total possible kmers)
#for that species
def main(args):

	filename = args[1]
	file = open(filename, 'r')
	lines = file.readlines()
	file.close()

	lineCount = len(lines)
	line = 0

	while line < lineCount:
		species = lines[line].strip().split('>')[1]
		sequence = lines[line+1].strip()

		os.makedirs(species)
		seq = Seq(sequence)

		fastaFile = open(os.path.join(species, species + "_dna.fasta"), 'w')
		fastaFile.write(sequence)
		fastaFile.close()


		graph = seq.createGraph()
		plt.savefig(species + '/graph.PNG')

		seq.createPandasDataFrame().to_csv(species + '/table.csv')

		uniqueBases = set(sequence)
		atgcBases = {'A', 'C', 'G', 'T'}

		lcFile = open(os.path.join(species, species + "_linquistic_complexity.txt"), 'w')
		lcFile.write(str(seq.linguisticComplexity()) + '\n')
		lcFile.write('The bases in this sequence are ')
		for base in uniqueBases:
			lcFile.write(str(base) + ' ')
		lcFile.write('\n')
		if not uniqueBases.issubset(atgcBases):
			lcFile.write('Warning: There is a base other than ATGC in this sequence.')
		lcFile.close()

		line = line + 3

if __name__ == "__main__":
	main(sys.argv)

##END##
