

def fibn(n):
    a = 0
    b = 1
    i = 1
    if n == 1:
        c = a
    if n == 2:
        c = b
    else:

        while i < n:
            c = a + b
            a = b
            b = c
            i += 1
    return c

n = int(input("Enter the nth term of the fibonnacci sequence:"))
print(n, "th fibonnacci term: " , fibn(n))