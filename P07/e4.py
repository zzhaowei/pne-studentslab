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

print()
gene_name = input("Enter the gene name: ").upper()

# Check if the gene exists in our dictionary
if gene_name not in GENES:
    termcolor.cprint(f"Error: Gene '{gene_name}' not found.", "red")
    exit()

ensembl_id = GENES[gene_name]
ENDPOINT = f"/sequence/id/{ensembl_id}"
PARAMS = "?content-type=application/json"

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMS)
    response = conn.getresponse()

    print(f"Response received!: {response.status} {response.reason}")

    if response.status == 200:
        data = json.loads(response.read().decode("utf-8"))
        sequence_str = data['seq']
        description = data['desc']

        s = Seq(sequence_str)

        print()
        termcolor.cprint(f"Gene: {gene_name}", "green")
        print(f"Description: {description}")
        print(f"Total length: {s.len()}")

        counts = s.count()

        for base in "ACGT":
            num = counts.get(base, 0)
            percentage = (num / s.len()) * 100
            print(f"  {base}: {num} ({percentage:.1f}%)")

        most_freq = max(counts, key=counts.get)
        print(f"Most frequent base: {most_freq}")
    else:
        print(f"Error fetching gene: {response.status}")

except Exception as e:
    print(f"Connection Error: {e}")

finally:
    conn.close()