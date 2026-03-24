from client0 import Client


c = Client("127.0.0.1", 8080)

flag = True
while flag:

    number = input("Guess the number between 1 - 100:")

    response = c.talk(number)
    print(response)

    if response == "correct!":
        flag = False
        print(f"You are correct! Congratulations!!")




