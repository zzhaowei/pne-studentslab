

def count_bases(seq):
    a = 0
    c = 0
    t = 0
    g = 0
    for i in range(0, len(seq)):
        if seq[i] == "A":
            a += 1
        elif seq[i] == "C":
            c += 1
        elif seq [i] == "T":
            t += 1
        else:
            g += 1

    total = a + c + g + t

    return total, a, c, t, g


def count_bases_file(list):
    total_all = 0
    a_all = 0
    c_all = 0
    t_all = 0
    g_all = 0
    for seq in list:
        total, a, c, t, g = count_bases(seq)
        total_all += total
        a_all += a
        c_all += c
        t_all += t
        g_all += g


    return total_all, a_all, c_all, t_all, g_all

f = open("dna.txt", "r")
lines = f.readlines()
txt_list = ["AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]
total, a, c, t, g = count_bases_file(txt_list)
print("Total length: " ,total)
print("A:" , a ,
"\nC:" , c ,
"\nT:" , t ,
"\nG:" , g)


print(lines)
f.close()
# open("dna.txt", "r") as f:
    #lines = f.readlines()



total_number = 0

bases = {"A": 0, "C": 0, "T" : 0 , "G": 0}
for sequence in lines:
    sequence = sequence.strip()
    total_number += len(sequence)

    for base in sequence:
        if base in bases:
            bases[base] += 1

print(total_number)
for base, count in bases.items():
    print(f' {base}: {count}')

