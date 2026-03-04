from client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

c = Client("212.128.255.87", 8080)

genes = ["U5", "FRAT1", "ADA"]

for names in genes:
    print(f"Sending the {names} Gene to the server...")


    s = Seq()
    s.read_fasta(f"sequences/{names}.fa")  # Or however you load genes in P01


    seq = str(s)
    response = c.talk(seq)

    # 5. Print the server's response
    print(f"Server response: {response}")