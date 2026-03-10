from client0 import Client

PRACTICE = 2
EXERCISE = 3
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

c = Client("212.128.255.93", 8080)

print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")

