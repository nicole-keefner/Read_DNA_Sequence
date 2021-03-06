Author: Nicole Keefner

General Description: Be able to read in a DNA sequence(s) and produce a folder containing 4 files- the sequence, a table, a graph, and a calculated value. These files are meant to be run through Python.

README.md: File that describes the contents of the Read_DNA_Sequence directory.

seq.py: File that creates a Seq class that accepts a DNA sequence with 5 methods: 1) counts theoretically possible kmers of size k, 2) counts observed kmers of size k, 3) creates a pandas dataframe of kmer sizes, number of theoretically possible kmers of that size, and observed kmers of that size, along with total possible and observed kmers, 4) produces a graph of the kmer size on the x-axis and the proportion of observed/possible kmers on the y-axis, 5) calculates the linguistic complexity of the sequence (i.e. total observed kmers/total possible kmers).

seq_complexity.py: File that creates a main function that reads in a file that is similar to the example file (nd2.fasta), and makes a folder for each species. Within each species folder, this function uses the seq.py script to output 4 files: 1) new fasta file that contains only the sequence for that species, 2) png file that contains a graph of the kmer size on the x-axis and the proportion of observed/possible kmers on the y-axis for that species, 3) csv file of the dataframe of kmer size, observed kmers, and possible kmers, and their totals for that species, and 4) txt file that contains the calculated linguistic complexity (i.e. total observed kmers/total possible kmers) and the unique bases in the sequence for that species. When there are bases in the sequence that are not A, T, G, or C, the txt file will have a third line with a warning message to indicate to the user that this sequence has a different base and that observed kmers may exceed possible kmers. To run the script and produce the folders with these files, type python seq_complexity.py “filename” in the anaconda command line. For example: python seq_complexity.py nd2.fasta

test_seq.py: Test file that checks to make sure the methods within the seq.py file are working correctly. To run the test, type py.test test_seq.py in the anaconda command line.

nd2.fasta: Example fasta file for which the first line is a species name proceeded by a “>”, the second line is a DNA sequence, and the third line contains no relevant information.
