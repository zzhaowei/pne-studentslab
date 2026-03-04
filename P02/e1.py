from P02.client0 import Client

client = Client("212.128.255.87", 8080)


PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Test the ping method
client.ping()
