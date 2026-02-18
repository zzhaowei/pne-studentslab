FOLDER = "sequences/"
FILENAME = "U5.fa"

from Seq0 import seq_read_fasta
file = FOLDER + FILENAME
print("Dna file name:", FILENAME, "\nThe first 20 bases are:" , seq_read_fasta(file)[0 : 20])

