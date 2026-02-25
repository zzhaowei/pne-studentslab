from Seq1 import Seq

s = Seq()
s.read_fasta("sequences/U5.fa")
print(f"Sequence: (Length:{s.len()}) {s}"
      f"\nBase: {s.count()}"
      f"\nReverse: {s.rev()}"
      f"\nComplement: {s.complement()}")