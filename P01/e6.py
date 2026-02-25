from Seq1 import Seq
s1 = Seq()
s2 = Seq("TATAC")
s3 = Seq("invalid Sequence")

print(f"Sequence1: (Length:{s1.len()}) {s1}"
      f"\nBase: {s1.count()}"
      f"\nSequence2: (Length:{s2.len()}) {s2}"
      f"\nBase: {s2.count()}"
      f"\nSequence3:( Length:{s3.len()}) {s3}"
      f"\nBase: {s3.count()}")