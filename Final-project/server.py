import http.server
import socketserver
import http.client
import json
from urllib.parse import urlparse, parse_qs
from jinja2 import Environment, FileSystemLoader

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
ENSEMBL_SERVER = "rest.ensembl.org"

env = Environment(loader=FileSystemLoader('html'))




class response:
    def __init__(self, params: dict, path: str, server: str = "rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        self.params = params
        self.PATH = path
        self.LNK = f"http://{IP}:{PORT}"
        self.conn = http.client.HTTPConnection(server)
        self.source = ""
        self.contents = ""
        self.style = ""

    def __str__(self):
        return f"Raw response, stored parameters:{str(self.params)}"

    def check_data(self):
        return [self.params, self.PATH, self.LNK, self.conn, self.source, self.contents, self.style]

    def load(self, ignore_list: bool = False):
        self.conn.request("GET", self.source)
        ens_data_raw = self.conn.getresponse().read().decode("utf-8")
        try:
            ens_data = json.loads(ens_data_raw)
        except json.decoder.JSONDecodeError:
            ens_data = ens_data_raw

        if type(ens_data) == list:
            if ignore_list:
                ens_data = ens_data[0]
        elif type(ens_data) == dict:
            if len(ens_data) == 0:
                ens_data = ("error", "return_empty")
            elif len(ens_data) == 1:
                check = None
                for e in ens_data:
                    check = e
                    break
                if check == "error":
                    ens_data = (check, ens_data[check])

        self.ens_data = ens_data

    def is_id(self):
        if "gene" not in self.params or len(self.params["gene"]) != 15:
            return False

        check = True
        for n in range(0, 4):
            if self.params["gene"][n] != "ENSG"[n]:
                check = False
                break
        if not check:
            try:
                int(self.params["gene"][4:15])
                check = True
            except ValueError:
                check = False
        return check

    def get_id(self, return_id: bool = False):
        # Fallback security check to ensure species parameter exists
        species = self.params.get("species", "homo_sapiens") or "homo_sapiens"
        self.conn.request("GET", f"/xrefs/symbol/{species}/{self.params['gene']}?content-type=application/json")
        id_raw = self.conn.getresponse().read().decode("utf-8")
        try:
            id_data = json.loads(id_raw)
            if len(id_data) != 0:
                self.id = id_data[0]["id"]
            else:
                self.id = ""
        except Exception:
            self.id = ""

        if return_id:
            return self.id

    def check_species(self):
        try:
            species = self.params["species"]
        except KeyError:
            species = ""
        if species == "":
            self.params.update({"species": "homo_sapiens"})


class listSpecies(response):
    def __init__(self, params, path, server="rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        self.source = "/info/species?content-type=application/json"


class karyotype(response):
    def __init__(self, params, path, server="rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        formatted_species = params["species"].replace("+", "%20").replace(" ", "%20")
        self.source = f"/info/assembly/{formatted_species}?content-type=application/json"


class chromosomeLenght(response):
    def __init__(self, params, path, server="rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        formatted_species = params["species"].replace("+", "%20").replace(" ", "%20")
        self.source = f"/info/assembly/{formatted_species}?content-type=application/json"


class geneLookup(response):
    def __init__(self, params, path, server="rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        self.check_species()
        self.source = f"/xrefs/symbol/{self.params['species']}/{params['gene']}?content-type=application/json"


class geneSeq(response):
    def __init__(self, params, path, server="rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        self.check_species()
        if self.is_id():
            self.id = params["gene"]
        else:
            self.get_id()
        self.source = f"/sequence/id/{self.id}?content-type=application/json"


class geneInfo(response):
    def __init__(self, params, path, server="rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        self.check_species()
        if self.is_id():
            self.id = params["gene"]
        else:
            self.get_id()
        self.source = f"/sequence/id/{self.id}?content-type=application/json"

    def create_info_table(self):
        coordinates = self.ens_data["desc"].split(":")
        self.table = {
            "molecule": self.ens_data["molecule"],
            "location": f"{coordinates[0]} {coordinates[2]}",
            "reference_version": coordinates[1],
            "start_base": coordinates[3],
            "end_base": coordinates[4],
            "len": int(coordinates[4]) - int(coordinates[3]),
            "strand_orientation": {"1": "forward", "-1": "reverse"}.get(coordinates[5], "unknown")
        }


class geneCalc(response):
    def __init__(self, params, path, server="rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        self.check_species()
        if self.is_id():
            self.id = params["gene"]
        else:
            self.get_id()
        self.source = f"/sequence/id/{self.id}?content-type=application/json"

    def count(self, seq):
        bases = {"A": 0, "C": 0, "T": 0, "G": 0}
        try:
            for l in seq:
                if l in bases:
                    bases[l] += 1
        except Exception:
            pass
        return bases


class geneList(response):
    def __init__(self, params, path, server="rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        self.check_species()
        self.source = f"/overlap/region/{self.params['species']}/{params['region']}:{params['start']}-{params['end']}?feature=gene;feature=transcript;feature=cds;feature=exon;content-type=application/json"

    def get_names(self):
        names = {}
        if isinstance(self.ens_data, list):
            for e in self.ens_data:
                try:
                    names.update({e[self.params["name_selection"]]: "selected"})
                except KeyError:
                    names.update({e["id"]: "fallback"})
        return names




class GenomeHandler(http.server.BaseHTTPRequestHandler):

    def render(self, template, context={}, status=200):
        """Compiles a template using Jinja2 and responds to the browser"""
        try:
            html = env.get_template(template).render(context)
            self.send_response(status)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html.encode('utf-8'))))
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(f"Jinja2 Structural Rendering Exception: {e}".encode())

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        raw_query = parse_qs(parsed.query)
        params = {key: val[0] for key, val in raw_query.items()}

        template_path = "Final-project/html"

        if path == "/" or path == "/index.html":
            self.render("index.html")

        elif path == "/listSpecies":
            spec_lim = params.get("spec_lim", "")
            name_selection = params.get("name_selection", "common_name")

            service = listSpecies(params, template_path)
            service.load()

            if isinstance(service.ens_data, tuple):
                self.render("error.html", {"message": "Database lookup failed to pull species data array."})
                return

            clean_list = []
            for item in service.ens_data.get("species", []):
                clean_list.append(item.get(name_selection, "N/A"))
                if spec_lim and len(clean_list) == int(spec_lim):
                    break

            self.render("listSpecies.html", {"species_list": clean_list})

        elif path == "/karyotype":
            species = params.get("species", "")
            if not species:
                self.render("error.html", {"message": "The species form name tracking box is required."})
                return

            service = karyotype(params, template_path)
            service.load()

            if isinstance(service.ens_data, tuple):
                self.render("error.html",
                            {"message": f"Target specimen grouping classification '{species}' not found."})
                return

            self.render("karyotype.html", {
                "species": species,
                "chromosomes": service.ens_data.get("karyotype", [])
            })


        elif path == "/chromosomeLength":
            species = params.get("species", "")
            chromosome = params.get("chromosome", "")

            if not species or not chromosome:
                self.render("error.html", {
                    "message": "Both the target species classification and chromosome ID are fully mandatory."})
                return

            service = chromosomeLenght(params, template_path)
            service.load()

            if isinstance(service.ens_data, tuple):
                self.render("error.html", {
                    "message": f"Could not extract assembly profiles tracking mapping records for '{species}'."})
                return

            found_length = None
            for region in service.ens_data.get("top_level_region", []):
                if str(region.get("name")).lower() == str(chromosome).lower():
                    found_length = region.get("length")
                    break

            if found_length is not None:
                self.render("chromosomeLength.html", {
                    "species": species,
                    "chromo": chromosome,
                    "length": found_length
                })
            else:
                self.render("error.html", {
                    "message": f"Chromosome track entry '{chromosome}' not observed inside target mapping layout arrays."})

        elif path == "/geneLookup":
            gene = params.get("gene", "")
            species = params.get("species", "homo_sapiens") or "homo_sapiens"

            service = geneLookup({"gene": gene, "species": species}, template_path)
            service.get_id()

            if getattr(service, "id", "") == "":
                self.render("error.html", {
                    "message": f"Locus reference lookup key symbol '{gene}' couldn't be resolved inside assembly indices."})
            else:
                self.render("geneLookup.html", {
                    "gene": gene,
                    "species": species,
                    "gene_id": service.id
                })

        elif path == "/geneSeq":
            gene = params.get("gene", "")
            species = params.get("species", "homo_sapiens") or "homo_sapiens"

            service = geneSeq({"gene": gene, "species": species}, template_path)
            service.load()

            if isinstance(service.ens_data, tuple) or "seq" not in service.ens_data:
                self.render("error.html", {
                    "message": f"Failed to retrieve structural sequence alignments for target reference token '{gene}'."})
                return

            self.render("geneSeq.html", {
                "gene_id": service.id,
                "sequence": service.ens_data["seq"]
            })

        elif path == "/geneInfo":
            gene = params.get("gene", "")
            species = params.get("species", "homo_sapiens") or "homo_sapiens"

            service = geneInfo({"gene": gene, "species": species}, template_path)
            service.load()

            if isinstance(service.ens_data, tuple) or "desc" not in service.ens_data:
                self.render("error.html", {"message": "Invalid tracking locus data description header array formats."})
                return

            service.create_info_table()
            self.render("geneInfo.html", {"info": service.table})

        elif path == "/geneCalc":
            gene = params.get("gene", "")
            species = params.get("species", "homo_sapiens") or "homo_sapiens"

            service = geneCalc({"gene": gene, "species": species}, template_path)
            service.load()

            if isinstance(service.ens_data, tuple) or "seq" not in service.ens_data:
                self.render("error.html",
                            {"message": "Nucleotide chain reference target is empty or invalid structure profiles."})
                return

            base_counts = service.count(service.ens_data["seq"])
            base_counts.update({"len": len(service.ens_data["seq"])})

            self.render("geneCalc.html", {"metrics": base_counts})

        elif path == "/geneList":
            region = params.get("region", "")
            start = params.get("start", "")
            end = params.get("end", "")
            species = params.get("species", "homo_sapiens") or "homo_sapiens"
            name_selection = params.get("name_selection", "id")

            if not region or not start or not end:
                self.render("error.html", {
                    "message": "Coordinate boundaries, start regions, and frame indices are completely mandatory fields."})
                return

            class_params = {"region": region, "start": start, "end": end, "species": species,
                            "name_selection": name_selection}
            service = geneList(class_params, template_path)
            service.load(ignore_list=False)

            if isinstance(service.ens_data, tuple):
                self.render("error.html", {
                    "message": "Failed parsing overlapping features alignment map entries over this sequence zone."})
                return

            self.render("geneList.html", {"overlap_map": service.get_names()})

        else:
            self.render("error.html", {
                "message": "Endpoint or web resource tracking reference not found inside this system configuration layout."},
                        404)


with socketserver.TCPServer(("", PORT), GenomeHandler) as httpd:
    print(f"Server actively listening for system portal requests at address link: http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nHalting running backend layout structure modules safely...")
        httpd.server_close()