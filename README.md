#### Sequence / Motif finder !

This Python script finds out if a given sequence is a DNA or RNA, then looks for motifs within the sequence.

## Prerequisite

- Python 3.x
- argparse library

## Arguments

-s, --seq: Input sequence (required)
-m, --motif: Motif to search for within the sequence (optional)

## Usage

python seqClass.py -s ATCGATCG
Output : The sequence is DNA

## Notes

The script converts your input sequence to uppercase.
The script identifies the sequence type (DNA or RNA) based on the presence of specific nucleotides.
If a motif is provided, the script searches for it within the sequence.
