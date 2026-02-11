student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print("\n\n\nName: " , student["name"])
print("Number of subjects:" , len(student["subjects"]))
print("Enrolled in PNE:", "PNE" in student["subjects"])
print("Database grade:", student["grades"]["Databases"])

grades = student["grades"].values()
average = sum(grades) / len(grades)
print("Average grade:", round(average, 2))

print("Subject-grade pairs:")
for subject, grade in student["grades"].items():
    print(f"{subject}: {grade}")