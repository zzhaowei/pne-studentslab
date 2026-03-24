import socket
import termcolor
from pathlib import Path

IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    try:
        req_raw = s.recv(2000)
        if not req_raw: return

        req = req_raw.decode()
        lines = req.split('\n')
        req_line = lines[0].strip()

        # Parse path (e.g., "GET /info/A HTTP/1.1" -> "/info/A")
        parts = req_line.split(" ")
        if len(parts) < 2: return
        path = parts[1]

        print("Request line: ", end="")
        termcolor.cprint(req_line, "green")

        # Logic to find the body
        path_list = ["/info/A", "/info/G", "/info/C", "/info/T"]

        if path in path_list:
            file_path = Path("html" + path + ".html")
            if file_path.exists():
                body = file_path.read_text()
                status = "200 OK"
            else:
                body = "<h1>File Not Found</h1>"
                status = "404 NOT FOUND"
        else:
            body = "<h1>Welcome to the DNA Server</h1><p>Try /info/A</p>"
            status = "200 OK"

        # Build the HTTP response
        response_msg = f"HTTP/1.1 {status}\r\n"
        response_msg += "Content-Type: text/html\r\n"
        response_msg += f"Content-Length: {len(body)}\r\n"
        response_msg += "\r\n"  # The mandatory blank line
        response_msg += body

        s.send(response_msg.encode())

    except Exception as e:
        print(f"Error processing client: {e}")


# --- MAIN PROGRAM (Socket Setup)
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print(f"DNA server configured on http://{IP}:{PORT}")

while True:
    try:
        (cs, client_ip_port) = ls.accept()
        process_client(cs)
        cs.close()
    except KeyboardInterrupt:
        print("\nServer stopped!")
        ls.close()
        break