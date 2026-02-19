from Seq0 import seq_read_fasta
from Seq0 import seq_reverse

files = ["U5", "ADA", "FRAT1", "FXN"]
FOLDER = "sequences/"
type = ".fa"

for names in files:
    seq = seq_read_fasta(FOLDER + names + type)
    print("Genes:" , names)
    print("Fragment: " , seq[0 : 20])
    print("Reversed: ", seq_reverse(seq , 20))
