def is_even(number):
    if number % 2 == 0:
        print("True")
    else:
        print("False")
is_even(4)
is_even(7)
is_even(0)
is_even(-3)
is_even(10)


def classify_triangle(a, b, c):
    if a == b and a == c:
        print("equilateral")
    elif a == b or a == c or b == c:
        print("isosceles")
    else:
        print("scalene")

classify_triangle(5, 5, 5)
classify_triangle(3, 3, 4)
classify_triangle(3, 4, 5)