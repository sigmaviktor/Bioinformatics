#!/usr/bin/env python3

"""
Read a FASTA file and print counts per letter for each record.

Usage:

    fastalettercount.py fastafile
"""

# >gi|229599677|ref|YP_002860617.1| hypothetical protein BAA_B0002 [Bacillus anthracis str. A0248]
# MTYVKLFQFRGNQIHVDIVQDFQRQYPEYPREADVLRHAIVLLDEKMREGKGQDDVSLLKKEVKDLKQSV
# NTMKQQMDVLIKLNMELIAQSGSNLSLEKLEQEVKSEIASSVTKKSEGKFPRTVKREPIEENVQEHQRIQ

# Read the FASTA file and for each record
# collect the sequence
# Then for the record count each letter
# Print the result
# Each record starts with a '>'

import sys

def process_record(record):
    amino_acids = "ARNDCEQGHILKMFPSTWYV"
    """Count each letter in ONE FASTA record"""
    # join the lines in the record (list)
    # for each type of letter, count the number
    rec = "".join(record)
    for amino_acid in amino_acids:
        print(amino_acid, rec.count(amino_acid))
    print("*"*20)


def process_fasta(fastafile):
    """Process all records from a FASTA file"""
    # For each record in the file
    # Process the record

    # Read the file until a new record starts
    # and collect the lines

    # For each line in the file
    # If line starts with '>' there's a new record
    record = []
    for line in fastafile:
        if line.startswith('>'):
            # If there is a record
            # process the record
            # Start a new record
            if record:
                process_record(record)
            record = []
        else:
            record.append(line)
    #process the last record
    process_record(record)


def main():
    #check arguments
    if len(sys.argv) != 2:
        print("filename is missing")
        sys.exit()
    # Get the filename
    # Open the file
    filename = sys.argv[1]
    openedfile = open(filename)

    # Process the records
    process_fasta(openedfile)

    # Close the file
    openedfile.close()

    return


main()
