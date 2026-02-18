files = ["sequences/U5.fa", "sequences/ADA.fa", "sequences/FRAT1.fa", "sequences/FXN.fa"]
bases = ["A", "C", "T", "G"]
from Seq0 import seq_count1
print(seq_count1(files, bases))
from Seq0 import seq_count
seq_count(files, bases)