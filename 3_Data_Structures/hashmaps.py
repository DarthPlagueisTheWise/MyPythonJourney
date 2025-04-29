# Introduction to dictionaries (hashmaps)

student = {
    "name": "Ved",
    "age": 18,
    "course": "Python Programming",
    "is_enrolled": True
}

# Access dictionary values
print("Student Name:", student["name"])
print("Student Age:", student.get("age"))
print("Enrolled Status:", student["is_enrolled"])

# Add a new key-value pair
student["grade"] = "A"
print("Updated Student Record:", student)
