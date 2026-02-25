from pathlib import Path
class Seq:
    def __init__(self, strbases = None):
        bases = "ACGT"

        if strbases is None:
            self.strbases = "Null"
            print("NULL sequence created")

        else:
            for base in strbases:

                if base not in bases:
                    self.strbases = "ERROR"
                    print("INVALID sequence!")
                    return


            self.strbases = strbases
            print("Valid sequence created")





    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "Null" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):

        if self.strbases != "Null" and "ERROR":
            count = self.strbases.count(base)
            return count
        else:
            return 0

    def count(self):
        bases = ["A", "C", "G", "T"]
        dict = {}

        for base in bases:
            if self.strbases != "Null" and "ERROR":
                dict[base] = self.strbases.count(base)
            else:
                dict[base] = 0

        return dict

    def rev(self):
        if self.strbases == "Null" or self.strbases == "ERROR":
            return self.strbases
        else:
            reversed_n = self.strbases[:: -1]
            return reversed_n

    def complement(self):
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        complement_seq = ""

        if self.strbases == "Null" or self.strbases == "ERROR":
            return self.strbases

        else:
            for base in self.strbases:
                complement_seq += complement.get(base, base)
            return complement_seq

    def read_fasta(self,filename):
        file_contents = Path(filename).read_text()
        file_contents = file_contents.split("\n")
        body = "".join(file_contents[1:])
        self.strbases = body
        return self.strbases

    def most_frequent_base(self):
        bases = ["A", "C", "G", "T"]
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for base in self.strbases:
            if base in counts:
                counts[base] += 1
        most_frequent = max(counts, key=counts.get)
        return most_frequent






