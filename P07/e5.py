import http.client
import json
import termcolor
from Seq1 import Seq

SERVER = 'rest.ensembl.org'
GENES = {
    "FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060", "RNU6-269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052", "ANK2": "ENSG00000145362"
}

def analyze_gene(name, ensembl_id):
    conn = http.client.HTTPConnection(SERVER)
    endpoint = f"/sequence/id/{ensembl_id}?content-type=application/json"

    try:
        conn.request("GET", endpoint)
        response = conn.getresponse()

        if response.status == 200:
            data = json.loads(response.read().decode("utf-8"))
            sequence_str = data['seq']
            description = data['desc']

            s = Seq(sequence_str)
            counts = s.count()

            print()
            termcolor.cprint(f"Gene: {name}", "green")
            print(f"Description: {description}")
            print(f"Total length: {s.len()}")

            for base in "ACGT":
                num = counts.get(base, 0)
                percentage = (num / s.len()) * 100
                print(f"  {base}: {num} ({percentage:.1f}%)")

            most_freq = max(counts, key=counts.get)
            print(f"Most frequent base: {most_freq}")
        else:
            termcolor.cprint(f"Error fetching {name}: {response.status}", "red")

    except Exception as e:
        print(f"Connection Error for {name}: {e}")
    finally:
        conn.close()


print()
termcolor.cprint("Starting Analysis of All Genes in the Dictionary...", "yellow")

for gene_name, gene_id in GENES.items():
    analyze_gene(gene_name, gene_id)

print()
termcolor.cprint("Process finished with exit code 0", "white")