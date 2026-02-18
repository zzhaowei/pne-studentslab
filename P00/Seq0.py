from pathlib import Path

def seq_ping():
    print("OK")


def seq_read_fasta(file):
    file_contents = Path(file).read_text()
    file_contents = file_contents.split("\n")
    body = "\n".join(file_contents[1 : ])
    return body

def seq_len(files):

    for names in files:
        genes = seq_read_fasta(names)
        print("GENES: ",names , "--->  Lenghth: ", len(genes) )

def seq_count_base(files, bases):
    for names in files:
        genes = seq_read_fasta(names)
        print(names)
        for base in bases:
            print("BASE:", base, "--->", genes.count(base), "times.")

def seq_count(files, bases):
    dict = {}
    for names in files:
        genes = seq_read_fasta(names)
        print(names)
        for base in bases:
            dict[base] = genes.count(base)
        print(dict)

def seq_count1(files, bases):
    dict = {}
    for names in files:
        genes = seq_read_fasta(names)
        dict[names] = {}

        for base in bases:
            dict[names][base] = genes.count(base)


    return dict


