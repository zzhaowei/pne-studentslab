import socket
class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    def ping(self):
        print("OK!\n")

    def __str__(self):
        return f"Client connected to server at {self.ip}, port:{self.port}"

    def talk(self,msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((self.ip, self.port))

        s.send(str.encode(msg))

        response = s.recv(2048).decode("utf-8")

        s.close()

        return response

