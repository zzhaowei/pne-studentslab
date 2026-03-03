
from Seq1 import Seq

s1 = Seq()
s2 = Seq()
s3 = Seq()
s4 = Seq()
seq = [s1, s2, s3, s4]

files = ["U5", "ADA", "FRAT1", "FXN"]
Folder = "sequences/"
file = ".fa"

for seqs, filenames in zip(seq, files):
    seqs.read_fasta(Folder + filenames + file)

    print(f"Gene: {filenames} (Length:{seqs.len()}) "
          f"\nBase: {seqs.count()}"
          f"\nMost frequent bases: {seqs.most_frequent_base()}")
