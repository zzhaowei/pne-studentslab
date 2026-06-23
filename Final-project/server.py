import http.server
import socketserver
import urllib.request
import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8080

class Seq:
    def __init__(self, strbases = None):
        bases = "ACGT"
        if strbases is None:
            self.strbases = "Null"
        else:
            for base in strbases:
                if base not in bases:
                    self.strbases = "ERROR"
                    return
            self.strbases = strbases

    def len(self):
        return 0 if self.strbases in ["Null", "ERROR"] else len(self.strbases)

    def count(self):
        bases = ["A", "C", "G", "T"]
        res_dict = {}
        for base in bases:
            if self.strbases != "Null" and self.strbases != "ERROR":
                res_dict[base] = self.strbases.count(base)
            else:
                res_dict[base] = 0
        return res_dict


class Client:
    def __init__(self):
        self.base_url = "https://rest.ensembl.org"

    def get_json(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        req = urllib.request.Request(url, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            print(f"ensembl api error [{endpoint}]: {e}")
            return None


client = Client()


class FinalProjectHandler(http.server.BaseHTTPRequestHandler):

    def read_html_file(self, filename):
        template_path = Path(__file__).parent / "html" / filename
        contents = template_path.read_text(encoding='utf-8')
        return j.Template(contents)

    def send_html_response(self, rendered_content, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(rendered_content.encode('utf-8'))

    def send_error_html(self, msg):
        template = self.read_html_file("error.html")
        rendered = template.render(message=msg)        
        self.send_html_response(rendered)

    def do_GET(self):
        url_path = urlparse(self.path)
        path = url_path.path 
        arguments = parse_qs(url_path.query)

        if path == '/' or path == '/index' or path == '/index.html':
            template = self.read_html_file("index.html")
            rendered = template.render()
            self.send_html_response(rendered)
            return

        elif path == '/listSpecies':
            if 'spec_lim' in arguments:
                limit = arguments['spec_lim'][0]
            else:
                limit = None

            data = client.get_json("/info/species")
            if not data or 'species' not in data:
                self.send_error_html("Could not retrieve species list from Ensembl.")
                return
            
            species_names = sorted([sp['display_name'] for sp in data['species']])

            if limit:
                try:
                    species_names = species_names[:int(limit)]
                except ValueError:
                    pass

            template = self.read_html_file("listSpecies.html")
            rendered = template.render(species_list=species_names)
            self.send_html_response(rendered)
            return

        elif path == '/karyotype':
            if 'species' in arguments:
                species = arguments['species'][0]
            else:
                species = ""

            if not species:
                self.send_error_html("please enter a species")
                return

            data = client.get_json(f"/info/assembly/{species.replace(' ', '%20')}")
            if not data or 'karyotype' not in data:
                self.send_error_html(f"Species '{species}' not found.")
                return

            template = self.read_html_file("karyotype.html")
            rendered = template.render(species=species, chromosomes=data['karyotype'])
            self.send_html_response(rendered)
            return

        elif path == '/chromosomeLength':
            if 'species' in arguments: species = arguments['species'][0]
            else: species = ""
            
            if 'chromosome' in arguments: chromosome = arguments['chromosome'][0]
            else: chromosome = ""

            if not species or not chromosome:
                self.send_error_html("please enter species /chromosome ")
                return

            data = client.get_json(f"/info/assembly/{species.replace(' ', '%20')}")
            if not data or 'top_level_region' not in data:
                self.send_error_html(f"Specant find : '{species}' .")
                return

            length = None
            for region in data['top_level_region']:
                if region.get('name') == str(chromosome) and region.get('coord_system') == 'chromosome':
                    length = region.get('length')
                    break

            if length is None:
                self.send_error_html(f"Chromosome '{chromosome}' not found for '{species}'.")
                return

            template = self.read_html_file("chromosomeLength.html")
            rendered = template.render(chromo=chromosome, species=species, length=length)
            self.send_html_response(rendered)
            return

        elif path == '/geneLookup':
            if 'gene' in arguments: gene = arguments['gene'][0]
            else: gene = ""

            if not gene:
                self.send_error_html("please enter a gene.")
                return

            data = client.get_json(f"/lookup/symbol/human/{gene}")
            if not data or 'id' not in data:
                self.send_error_html(f"gene lookup of '{gene}'  failed.")
                return

            template = self.read_html_file("geneLookup.html")
            rendered = template.render(gene=gene, species="human", gene_id=data['id'])
            self.send_html_response(rendered)
            return

        
        elif path == '/geneSeq':
            if 'gene' in arguments: gene = arguments['gene'][0]
            else: gene = ""

            if not gene:
                self.render_error("please enter a gene")
                return

            lookup_data = client.get_json(f"/lookup/symbol/human/{gene}")
            if not lookup_data or 'id' not in lookup_data:
                self.render_error(f"Could not find stable ID for gene '{gene}'.")
                return
            gene_id = lookup_data['id']

            seq_data = client.get_json(f"/sequence/id/{gene_id}")
            if not seq_data or 'seq' not in seq_data:
                self.send_error_html(f"Could not retrieve DNA sequence for '{gene}'.")
                return
            
            raw_sequence = seq_data['seq']

            template = self.read_html_file("geneSeq.html")
            rendered = template.render(gene_id=gene, sequence=raw_sequence)     
            self.send_html_response(rendered)                 
            return

        elif path == '/geneCalc':
            if 'gene' in arguments: gene = arguments['gene'][0]
            else: gene = ""

            if not gene:
                self.send_error_html("please enter a gene")
                return

            lookup_data = client.get_json(f"/lookup/symbol/human/{gene}")
            if not lookup_data or 'id' not in lookup_data:
                self.send_error_html(f"Could not find stable ID for gene '{gene}'.")
                return
            gene_id = lookup_data['id']

            seq_data = client.get_json(f"/sequence/id/{gene_id}")
            if not seq_data or 'seq' not in seq_data:
                self.send_error_html(f"Could not retrieve DNA sequence for '{gene}'.")
                return
            
            raw_sequence = seq_data['seq']

            seq_obj = Seq(raw_sequence)
            total_len = seq_obj.len()
            counts = seq_obj.count()
            try:
                metrics = {
                    "len": total_len,
                    "A": f"{(counts.get('A', 0) / total_len) * 100:.2f}%",
                    "C": f"{(counts.get('C', 0) / total_len) * 100:.2f}%",
                    "T": f"{(counts.get('T', 0) / total_len) * 100:.2f}%",
                    "G": f"{(counts.get('G', 0) / total_len) * 100:.2f}%"
                }
            except ZeroDivisionError:
                self.send_error_html(f"there is a zero division error for the length.")
            
            template = self.read_html_file("geneCalc.html")
            rendered = template.render(metrics=metrics)
            self.send_html_response(rendered)
            return

        elif path == '/geneInfo':
            if 'gene' in arguments: gene = arguments['gene'][0]
            else: gene = ""

            if not gene:
                self.send_error_html("Missing 'gene' parameter.")
                return

            lookup_data = client.get_json(f"/lookup/symbol/human/{gene}")
            if not lookup_data or 'id' not in lookup_data:
                self.send_error_html(f"Could not find information for gene '{gene}'.")
                return

            info = {
                "molecule": lookup_data.get('biotype', 'N/A'),
                "location": f"Chromosome {lookup_data.get('seq_region_name', 'N/A')}",
                "start_base": lookup_data.get('start', 0),
                "end_base": lookup_data.get('end', 0),
                "len": abs(lookup_data.get('end', 0) - lookup_data.get('start', 0)) + 1,
                "strand_orientation": "Forward (+)" if lookup_data.get('strand', 1) == 1 else "Reverse (-)",
                "reference_version": lookup_data.get('assembly_name', 'GRCh38')
            }
            
            template = self.read_html_file("geneInfo.html")
            rendered = template.render(info=info)
            self.send_html_response(rendered)
            return
        elif path == '/geneList':
            if 'chromo' in arguments: chromo = arguments['chromo'][0].strip()
            else: chromo = ""
            
            if 'start' in arguments: start = arguments['start'][0].strip()
            else: start = ""
            
            if 'end' in arguments: end = arguments['end'][0].strip()
            else: end = ""

            if not chromo or not start or not end:
                self.send_error_html("please enter chromosome/ start / end(all three).")
                return

            endpoint = f"/overlap/region/human/{chromo}:{start}-{end}?feature=gene"
            
            data = client.get_json(endpoint)
            if data is None:
                self.send_error_html(f"Ensembl error or invalid chromosome '{chromo}:{start}-{end}'.")
                return

            overlap_map = {}
            for item in data:
                gene_name = item.get('display_name')
                if not gene_name:
                    gene_name = item.get('external_name', item.get('id'))
                
                classification = item.get('biotype', 'Unknown')
                
                if gene_name:
                    overlap_map[gene_name] = classification

            template = self.read_html_file("geneList.html")
            rendered = template.render(overlap_map=overlap_map)
            self.send_html_response(rendered)
            return
        else:
            self.send_error_html("Resource Endpoint non-existent. Check url parameters.")

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), FinalProjectHandler) as httpd:
        print(f"server running at: http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nserver closed")