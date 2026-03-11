from client0 import Client
c = Client("21  2.128.255.93", 8080)


for i in range(5):

    response = c.talk(f"Message{i}")
    print(f"To server: Message{i}")
    print(f"Response: {response}")

