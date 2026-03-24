import socket
import termcolor
from pathlib import Path

IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    try:
        req_raw = s.recv(2000)
        if not req_raw: return  # Handle empty requests

        req = req_raw.decode()
        lines = req.split('\r\n')  # Use standard CRLF split
        req_line = lines[0]

        # Parse the request line (Method Path Protocol)
        parts = req_line.split(" ")
        if len(parts) < 2: return
        path = parts[1]

        print("Request: ", end="")
        termcolor.cprint(req_line, "green")

        # Logic to find the file
        path_list = ["/info/A", "/info/C"]

        if path in path_list:
            file_path = Path("html" + path + ".html")
            if file_path.exists():
                body = file_path.read_text()
                status_code = "200 OK"
            else:
                body = "<h1>404 Not Found</h1>"
                status_code = "404 Not Found"
        else:
            body = "<h1>403 Forbidden</h1>"
            status_code = "403 Forbidden"

        # Construct HTTP Response
        response = f"HTTP/1.1 {status_code}\r\n"
        response += "Content-Type: text/html\n"
        response += f"Content-Length: {len(body)}\r\n"
        response += "\r\n"  # Blank line separating headers from body
        response += body

        s.send(response.encode())
    except Exception as e:
        print(f"Error processing request: {e}")


# --- SERVER SETUP (Unchanged from your snippet)
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print(f"Server running on http://{IP}:{PORT}")

while True:
    try:
        (cs, addr) = ls.accept()
        process_client(cs)
        cs.close()
    except KeyboardInterrupt:
        print("\nServer stopped!")
        ls.close()
        break