from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = ("sequences/ADA.fa")

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

file_contents = file_contents.split("\n")
body = "".join(file_contents[1 : ])
print(body)
print("Total number of bases:", len(body))