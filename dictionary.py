student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Science"]
}

print(student["name"])       # Alice
print(student.get("age"))    # 20
print(student["courses"]) # Math

# Update
student["age"] = 21
print(student)

# Add new key
student["grade"] = "A"
print(student)

# Loop through dictionary
for key, value in student.items():
    print(f"{key}: {value}")
