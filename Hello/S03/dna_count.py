from itertools import count


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

seq = input("Enter a DNA sequence:")
total, a, c, t, g = count_bases(seq)

print("Total length: " ,total)
print("A:" , a)
print("C:" , c)
print("T:" , t)
print("G:" , g)
