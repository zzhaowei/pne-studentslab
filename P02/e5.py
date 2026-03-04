from client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

c = Client("212.128.255.87", 8080)
s = Seq()
s.read_fasta("sequences/FRAT1.fa")
seq = str(s)
print(f"Gene FRAT1: {seq}")

c.talk("Sending the FRAT1 Gene to the server, in fragment of 10 bases.")
i = 0
while i < 4:
    print(f"fragment {i+1}: {seq[i * 10 : (i + 1) * 10]}")
    c.talk(f"fragment {i+1}: {seq[i * 10 : (i + 1) * 10]}")
    i += 1


