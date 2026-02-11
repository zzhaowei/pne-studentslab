def grading(score):
    if 9 <= score <= 10:
        return "A"
    elif 7 <= score < 9:
        return "B"
    elif 5 <= score < 7:
        return "C"
    elif 3 <= score < 5:
        return "D"
    else:
        return "E"

#score = float(input("Enter a score: "))
#print("\n\n\nScore" , score , "->" , grading(score))