students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]

def avarage(students):
    list_grades = []
    i = 0
    while i < len(students):
        avarage = round(sum(students[i]["grades"]) / len(students[i]["grades"]) , 2)
        list_grades.append(avarage)
        i += 1
    return list_grades

print(avarage(students))