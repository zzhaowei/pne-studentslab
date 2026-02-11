dna = "ATGCGATCGATCGATCGATCGA"

def find_subset(dna):
    i = 0
    count = 0
    while i < len(dna):
        if i == dna.find("ATC"):
            count += 1
            dna = dna[i+2 : ]
            i = 0
        else:
            i+= 1
    return count

def find_subset2(dna):
    i = 0
    count = 0
    while i < len(dna):
        if dna[i : i + 3] == "ATC":
            count += 1
            i += 1
        else:
            i += 1
    return count
print("Length: " , len(dna))
print("The first 5: ", dna[0:5])
print("The last 3: ", dna[-4 : -1])
print("Lowercase: ", dna.lower())
print("ATC count:" , find_subset2(dna))
print("RNA: ", dna.replace("T" , "U"))
















