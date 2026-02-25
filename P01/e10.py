from Seq1 import Seq
s1 = Seq()
s2 = Seq()
s3 = Seq()
s4 = Seq()
seq = [s1, s2, s3, s4]
files = ["sequences/U5.fa", "sequences/ADA.fa", "sequences/FRAT1.fa", "sequences/FXN.fa"]
for seqs in seq:

    for filenames in files:
        seqs.read_fasta(filenames)

    print(f"Sequence: (Length:{seqs.len()}) {seqs}"
          f"\nBase: {seqs.count()}"
          f"\nReverse: {seqs.rev()}"
          f"\nComplement: {seqs.complement()}")