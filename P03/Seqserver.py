from Seq1 import Seq
import socket

seq0 = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
seq1 = "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA"
seq2 = "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT"
seq3 = "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA"
seq4 = "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"
seq_list = [seq0, seq1, seq2, seq3, seq4]
# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1" # this IP address is local, so only requests from the same machine are possible


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

        msg = msg_raw.decode()

        print(f"Command received: {msg}")

        response = ""

        if msg == "PING":
            response = "OK!\n"
            print(f"\n\nResponse massage: {response}")
            cs.send(response.encode())

        elif msg.startswith("GET"):
            number = int(msg.split(" ")[1])
            response = seq_list[number] + "\n"
            print(f"\n\nGEN {number}: {response}")


        elif msg.startswith("INFO"):
            sc = Seq(msg.split(" ")[1])
            response = (f"sequence: {sc}"
                        f"\nlength: {sc.len()}"
                        f"\n{sc.count()}\n")
            print("\n\n" + response)


        elif msg.startswith("COMP"):
            sc = Seq(msg.split(" ")[1])
            response = sc.complement()
            print(f"\n\ncomplement sequence: {response}")

        elif msg.startswith("REV"):
            sc = Seq(msg.split(" ")[1])
            response = sc.rev()
            print(f"\n\nReversed sequence: {response}")

        elif msg.startswith("GENE"):
            filename = msg.split(" ")[1]
            sc = Seq()
            response= sc.read_fasta("sequences/" + filename + ".fa")
            print(f"\n\nGene {filename}: {response}")

        cs.send(response.encode())

        cs.close()



