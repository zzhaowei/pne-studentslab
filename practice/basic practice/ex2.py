text = "  Hello, World! Welcome to Python Programming.  "
text1 = text.strip()
text_list = text1.split()

print("\n\n\nStripped:" , text1)
print("Word count:" , len(text_list))
print("Title case:" , text1.title())
print("Start with Hello:", text1.startswith("Hello"))
print("ENd with ing.:" , text1.endswith("ing."))
print("Python position:" , text1.find("Python") + 1)
print("Joined:" ,  " - ".join(text_list))