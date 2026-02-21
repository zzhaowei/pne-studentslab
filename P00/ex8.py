from Seq0 import seq_read_fasta,  most_frequent_base, FOLDER, type


files = ["U5", "ADA", "FRAT1", "FXN"]

for names in files:
    seq = seq_read_fasta(FOLDER + names + type )
    most_frequent = most_frequent_base(seq)
    print(f"Gene {names}: Most frequent Base: {most_frequent}")
