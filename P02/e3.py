from client0 import Client
c = Client("212.128.255.87", 8080)

print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")

