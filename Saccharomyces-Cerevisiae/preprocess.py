from Bio import SeqIO
import numpy as np

chromosome_file = 'chr01.fsa'
confirmed_origins = 'chr01-confirmed.fsa'
likely_origins = 'chr01-likely.fsa'
dubious_origins = ''

def char_to_number(ch):
    if ch == 'A':
        return -1
    elif ch == 'C':
        return -2
    elif ch == 'G':
        return -3
    elif ch == 'T':
        return -4
    elif ch == 'a':
        return 1
    elif ch == 'c':
        return 2
    elif ch == 'g':
        return 3
    elif ch == 't':
        return 4

def char_to_label(value):
    if value < 0:
        return 0
    else:
        return 1

input_matrix = []
labels = []

fasta_sequences = SeqIO.parse(open(chromosome_file),'fasta')
for fasta in fasta_sequences:
    name, cerevisie_chromosome = fasta.id, str(fasta.seq)

fasta_sequences = SeqIO.parse(open(confirmed_origins),'fasta')
for fasta in fasta_sequences:
    name, replication_origin = fasta.id, str(fasta.seq)
    # just a sanity check
    if replication_origin in cerevisie_chromosome:
        # convert the replication origin to lowercase in the chromosome
        seq_row = cerevisie_chromosome.replace(replication_origin, replication_origin.lower())
        # convert the character vector to a numpy array of numbers
        input_row = np.array(map(char_to_number, seq_row))
        label = np.array(map(char_to_label, input_row))

        input_matrix.append(input_row)
        labels.append(label)

input_matrix = np.array(input_matrix)
labels = np.array(labels)
print input_matrix