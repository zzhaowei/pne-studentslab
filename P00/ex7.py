from Seq0 import seq_read_fasta
from Seq0 import seq_complement

files = ["U5", "ADA", "FRAT1", "FXN"]
FOLDER = "sequences/"
type = ".fa"

for names in files:
    seq = seq_read_fasta(FOLDER + names + type)[: 20]
    print("Genes:" , names)
    print("Fragment: " , seq)
    print("Complement: ", seq_complement(seq))