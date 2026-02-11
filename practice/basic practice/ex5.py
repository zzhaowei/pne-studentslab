words = ["Python", "is", "a", "programming", "language"]
def count_len(words):
    for word in words:
        print(word , "->" , len(word) , "characters")

count_len(words)

def double_n():
    n = 1
    while n <= 1000:
        n = n * 2
        print(n)
double_n()