import sys
from argparse import ArgumentParser

# Set up parser variable and add seq argument to it.
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Set args as the output of the parser script
args = parser.parse_args()

# Convert to uppercase
args.seq = args.seq.upper()

# Check if sequence contains non DNA/RNA letters
if any(letter not in 'ACGTU' for letter in args.seq):
    print('ERROR: The sequence contains non-DNA/RNA letters.')
    sys.exit(1)

# Check if sequence contains U and T simultaneously
if 'T' in args.seq and 'U' in args.seq:
    print('ERROR: The sequence contains both T and U.')
    sys.exit(1)

# Set up count variables
counts = {}

sequence_length = len(args.seq)

# Set up loop to check the letters and increase count per letter
for letter in args.seq:
	if letter in counts:
		counts[letter] += 1
	else:
		counts[letter] = 1

# Print the type of sequence
print('The sequence is DNA' if "T" in args.seq else 'The sequence is RNA' if "U" in args.seq else 'The sequence is DNA or RNA')

# Print the counts of nucleotides
for letter, count in counts.items():
	print(f"%{letter}: {count / sequence_length * 100:.2f}%")
