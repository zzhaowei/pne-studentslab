class Seq:
    def __init__(self, strbases):
        bases = "ACGT"


        for base in strbases:

            if base not in bases:
                self.strbases = "ERROR"
                print("ERROR")
                return


        self.strbases = strbases
        print("New sequence created")


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

def generate_seqs(pattern, number):
    i = 1
    list_seq = []
    while i <= number:
        list_seq.append(Seq(pattern * i))
        i += 1
    return list_seq

from ex2 import print_seqs
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
