import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.93" # this IP address is local, so only requests from the same machine are possible
number_con = 0

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()
clients_data = []

print("The server is configured!")

while len(clients_data) < 5:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()
        number_con += 1
        clients_data.append(client_ip_port)


    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")
        print("CONNECTION{}:  From the IP: {}".format(number_con, client_ip_port))



        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"Message received: {msg}")

        # -- Send a response message to the client
        response = f"ECHO: {msg}\n"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()

    print("MAXIMUM CLIENTS REACHED")
    print("the following clients have connected to the server")


    for i, info in enumerate(clients_data, 1):
        print(f"Client {i}: {info}")


