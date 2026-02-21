from Seq0 import seq_read_fasta, seq_complement, FOLDER, type


files = ["U5", "ADA", "FRAT1", "FXN"]


for names in files:
    seq = seq_read_fasta(FOLDER + names + type)[: 20]
    print("Genes:" , names)
    print("Fragment: " , seq)
    print("Complement: ", seq_complement(seq))