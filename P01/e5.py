from Seq1 import Seq
s1 = Seq()
s2 = Seq("TATAC")
s3 = Seq("invalid Sequence")

print(f"Sequence1: {s1} \nA: {s1.count_base("A")}    C: {s1.count_base("C")}   G: {s1.count_base("G")}    T: {s1.count_base("T")}"
      f"\nSequence2: {s2}\nA: {s2.count_base("A")}    c: {s2.count_base("C")}    G: {s2.count_base("G")}    T: {s2.count_base("T")}"
      f"\nSequence3: {s3}\nA: {s3.count_base("A")}    C: {s3.count_base("C")}    G: {s3.count_base("G")}    T: {s3.count_base("T")}")



