from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "sequences/U5.fa"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

file_contents = file_contents.split("\n")
body = "\n".join(file_contents[1 : ])
print("body of the U5.txt file:")
print(body)