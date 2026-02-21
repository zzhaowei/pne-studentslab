from pathlib import Path

FOLDER = "sequences/"
type = ".fa"

def seq_ping():
    print("OK")


def seq_read_fasta(file):
    file_contents = Path(file).read_text()
    file_contents = file_contents.split("\n")
    body = "".join(file_contents[1 : ])
    return body

def seq_len(files):

    for names in files:
        genes = seq_read_fasta(FOLDER + names + type)
        print("GENES: ",names , "--->  Lenghth: ", len(genes) )

def seq_count_base(files, bases):
    for names in files:
        genes = seq_read_fasta(FOLDER + names + type)
        print(names)
        for base in bases:
            print("BASE:", base, "--->", genes.count(base), "times.")

def seq_count(files, bases):
    dict = {}
    for names in files:
        genes = seq_read_fasta(FOLDER + names +  type)
        print(names)
        for base in bases:
            dict[base] = genes.count(base)
        print(dict)

def seq_count1(files, bases):
    dict = {}
    for names in files:
        genes = seq_read_fasta(FOLDER + names + type)
        dict[names] = {}

        for base in bases:
            dict[names][base] = genes.count(base)


    return dict

def seq_reverse(seq, n):

    reversed_n = seq[n-1 :: -1]
    return  reversed_n

def seq_complement(seq):

    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    complement_seq = ""
    for base in seq:
        complement_seq += complement.get(base, base)

    return complement_seq

def most_frequent_base(seq):

    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for base in seq:
        if base in counts:
            counts[base] += 1
    most_frequent = max(counts, key=counts.get)
    return most_frequent




