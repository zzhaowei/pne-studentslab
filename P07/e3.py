import http.client
import json

SERVER = 'rest.ensembl.org'
GENE_ID = "ENSG00000207552" # MIR633
ENDPOINT = f"/sequence/id/{GENE_ID}?content-type=application/json"

conn = http.client.HTTPConnection(SERVER)
conn.request("GET", ENDPOINT)
res = conn.getresponse()
data = json.loads(res.read().decode("utf-8"))

print(f"Gene: MIR633")
print(f"Description: {data['desc']}")
print(f"Sequence: {data['seq']}")