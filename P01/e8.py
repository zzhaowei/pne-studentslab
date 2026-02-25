from Seq1 import Seq
s1 = Seq()
s2 = Seq("TATAC")
s3 = Seq("invalid Sequence")

print(f"Sequence1: (Length:{s1.len()}) {s1}"
      f"\nReverse: {s1.rev()}"
      f"\nComplement: {s1.complement()}"
      f"\nSequence2: (Length:{s2.len()}) {s2}"
      f"\n:Reverse {s2.rev()}"
      f"\nComplement: {s2.complement()}"
      f"\nSequence3:( Length:{s3.len()}) {s3}"
      f"\nReverse: {s3.rev()}"
      f"\nComplement: {s3.complement()}")