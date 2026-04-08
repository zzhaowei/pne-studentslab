import http.server
import socketserver
import termcolor

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):


        print("GET received! Request line:")

        termcolor.cprint("  " + self.requestline, 'green')

        print("  Command: " + self.command)

        print("  Path: " + self.path)

        if self.path == "/" or self.path == "/index.html":
            file_path = "html/index.html"
        else:

            file_path = "html" + self.path + ".html"

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            status_code = 200
            termcolor.cprint(f"  Success: {file_path}", "green")

        except FileNotFoundError:
            status_code = 404
            termcolor.cprint(f"  Error: {file_path} not found.", "red")
            with open("html/Error.html", "r", encoding="utf-8") as f:
                content = f.read()

        self.send_response(status_code)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content.encode('utf-8'))))
        self.end_headers()

        self.wfile.write(content.encode('utf-8'))

        return



Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
