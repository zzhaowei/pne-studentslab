import json
import termcolor
from pathlib import Path

# -- Read the json file
json_string = Path("people-e1.json").read_text()
people = json.loads(json_string)

print()
termcolor.cprint(f"Total people in database: {len(people)}", 'yellow', attrs=['bold'])

for person in people:
    print("-" * 20)
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])

    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    phone_numbers = person['phoneNumber']
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phone_numbers))

    for i, dictnum in enumerate(phone_numbers):
        termcolor.cprint(f"  Phone {i + 1}: ", 'blue')
        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dictnum['number'])