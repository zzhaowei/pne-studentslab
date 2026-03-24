import socket
import termcolor
from pathlib import Path

def process_client(s):
    try:
        req_raw = s.recv(2000)
        if not req_raw: return

        req = req_raw.decode()
        lines = req.split('\n')
        req_line = lines[0].strip()

        parts = req_line.split(" ")
        if len(parts) < 2: return
        path = parts[1]

        path_list = ["/info/A"]

        if path in path_list:
            file_path = Path("html" + path + ".html")
            if file_path.exists():
                body = file_path.read_text()
                status_line = "HTTP/1.1 200 OK\r\n"
            else:
                body = "<h1>File missing on disk</h1>"
                status_line = "HTTP/1.1 404 NOT FOUND\r\n"
        else:
            body = "<h1>404 Not Found</h1><p>Try /info/A</p>"
            status_line = "HTTP/1.1 404 NOT FOUND\r\n"

        header = "Content-Type: text/html\r\n"
        header += f"Content-Length: {len(body.encode())}\r\n"

        response_msg = status_line + header + "\r\n" + body

        s.send(response_msg.encode())

        print("Request line: ", end="")
        termcolor.cprint(req_line, "green")

    except Exception as e:
        print(f"Error: {e}")