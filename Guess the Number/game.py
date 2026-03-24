import socket
import random
PORT = 8080
IP = "127.0.0.1"

class NumberGuesser:
    def __init__(self, secret_number, attempts):
        self.secret_number = secret_number
        self.attempts = []

    def guess(self,number):
        if number == secret_number:
            return "correct!"

        elif number < secret_number:
            return "higher"

        else:
            return "lower"



secret_number = random.randint(1, 100)
attempts = []
game = NumberGuesser(secret_number,attempts)


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()


print("The Seq server is configured!")

while True:
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()




    except KeyboardInterrupt:
        print("Server stopped by the user")

        ls.close()

        exit()

    else:

        print("A client has connected to the server!")

        msg_raw = cs.recv(2048)

        number = int(msg_raw.decode())

        response = game.guess(number)

        cs.send(response.encode())
        attempts.append(number)

        cs.close()

