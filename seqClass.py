#import necessary libraries
import sys, re
from argparse import ArgumentParser

#Define the goal of the function
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
# Define parsers
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
# Make sequence in upper case
args.seq = args.seq.upper()
# Research special letters to identify if it is DNA or RNA
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
	if re.search('U', args.seq):
		print ('The sequence is not DNA nor RNA')
	else:
		print ("The sequence is DNA")
    elif re.search('U', args.seq):
	print ("The sequence is RNA")
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

# Research a motif
if args.motif:
    args.motif = args.motif.upper()
    print(f'BLABLA Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND XoXoXo")
    else:
        print("NOT FOUND bliblibli")
