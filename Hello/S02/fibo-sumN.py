def fibosum(n):
    a = 0
    b = 1
    i = 1
    res = 1
    if n == 1:
        res = a
    if n == 2:
        res = b
    else:

        while i < n:
            c = a + b
            res += c
            a = b
            b = c
            i += 1
    return res

n = int(input("Enter the nth term of the fibonacci sequence to sum:"))
print("Sum of the first", n ,"terms of the fibonacci sequence: " , fibosum(n))