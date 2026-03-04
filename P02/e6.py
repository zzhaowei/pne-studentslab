from client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

c1 = Client("212.128.255.87", 8080)
c2 = Client("212.128.255.87", 8081)

s = Seq()
s.read_fasta("sequences/FRAT1.fa")
seq = str(s)
print(f"Gene FRAT1: {seq}")

c1.talk("Sending the FRAT1 Gene to the server, in fragment of 10 bases.")
c2.talk("Sending the FRAT1 Gene to the server, in fragment of 10 bases.")
i = 0
while i < 10:
    if i % 2 == 0:
        print(f"fragment {i+1}: {seq[i * 10 : (i + 1) * 10]}")
        c1.talk(f"fragment {i+1}: {seq[i * 10 : (i + 1) * 10]}")
        i += 1
    else:
        print(f"fragment {i + 1}: {seq[i * 10: (i + 1) * 10]}")
        c2.talk(f"fragment {i + 1}: {seq[i * 10: (i + 1) * 10]}")
        i += 1




