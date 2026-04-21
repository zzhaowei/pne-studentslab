import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
from jinja2 import Environment, FileSystemLoader
from Seq1 import Seq

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

seq_list = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"
]

VALID_GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
VALID_OPS = ["info", "comp", "rev"]

env = Environment(loader=FileSystemLoader('html'))


class SeqHandler(http.server.BaseHTTPRequestHandler):

    def render(self, template, context={}, status=200):
        html = env.get_template(template).render(context)
        self.send_response(status)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(html.encode())))
        self.end_headers()
        self.wfile.write(html.encode())

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)

        if path == "/" or path == "/index.html":
            self.render("index.html")

        elif path == "/ping":
            self.render("ping.html")

        # GET
        elif path == "/get":
            if "n" not in params:
                self.render("get_form.html")
            else:
                try:
                    n = int(params["n"][0])
                    if n < 0 or n >= len(seq_list):
                        raise ValueError

                    self.render("get.html", {
                        "n": n,
                        "sequence": seq_list[n]
                    })

                except:
                    self.render("error.html", {"message": "Invalid sequence"}, 400)

        elif path == "/gene":
            if "name" not in params:
                self.render("gene_form.html")
            else:
                name = params["name"][0]

                if name not in VALID_GENES:
                    self.render("error.html", {"message": "Invalid gene"}, 400)
                    return

                try:
                    s = Seq()
                    sequence = s.read_fasta(f"sequences/{name}.fa")

                    self.render("gene.html", {
                        "name": name,
                        "sequence": sequence
                    })

                except:
                    self.render("error.html", {"message": "File not found"}, 404)

        elif path == "/operation":
            if "seq" not in params or "op" not in params:
                self.render("operation_form.html")
            else:
                seq_str = params["seq"][0]
                op = params["op"][0]

                if op not in ["info", "comp", "rev"]:
                    self.render("error.html", {"message": "Invalid operation"}, 400)
                    return

                s = Seq(seq_str)

                if op == "info":
                    result = {
                        "sequence": seq_str,
                        "length": s.len(),
                        "counts": s.count().split("\n")
                    }

                elif op == "comp":
                    result = {"sequence": s.complement()}

                elif op == "rev":
                    result = {"sequence": s.rev()}

                self.render("operation.html", {
                    "op": op,
                    "result": result
                })

        else:
            self.render("error.html", {"message": "Page not found"}, 404)


with socketserver.TCPServer(("", PORT), SeqHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()