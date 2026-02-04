a = 0
b = 1
i = 1
seq = []
seq.append(a)
seq.append(b)
while i < 10:
    c = a + b
    a = b
    b = c
    seq.append(c)
    i += 1
print(seq)



