from client0 import Client
PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

c = Client("127.0.0.1", 8080)

print("\n\ntesting PING ...")
response = c.talk("PING")
print(f"Server response: {response}")


print("\n\ntesting GEt ...")
for i in range(5):
    gen = c.talk("GET " + str(i))
    print(f"Gen{i}: {gen}")

sequence = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
info = c.talk("INFO " + sequence)
print("\n\ntesting INFO ...")
print(info)


comp = c.talk("COMP " + sequence)
print("\n\ntesting COMP ...")
print(comp)

reverse = c.talk("REV " + sequence)
print("\n\ntesting REV ...")
print(reverse)


print("\n\ntesting GENE ...")
ada = c.talk ("GENE " + "ADA")
frat1 = c.talk ("GENE " + "FRAT1")
u5 = c.talk("GENE " + "U5")
fxn = c.talk("GENE " + "FXN")
rnu6 = c.talk("GENE " + "RNU6_269P")
print(f"ADA: {ada}")
print(f"FRAT1: {frat1}")
print(f"U5: {u5}"
      f"\nFXN: {fxn}"
      f"\nRNU6_269P: {rnu6}")

