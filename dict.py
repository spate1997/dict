
# Task 1: Create a Dictionary
student_info = {
    "name": "Alice",
    "age": 23,
    "major": "Computer Science",
    "courses": ["Algorithms", "Data Structures", "Operating Systems"]
}

# Task 2: Access Dictionary Values
print(student_info["name"])  # Output: Alice
print(student_info["courses"])  # Output: ['Algorithms', 'Data Structures', 'Operating Systems']

# Task 3: Update Dictionary
student_info["graduation_year"] = 2024
student_info["age"] = 24

# Task 4: Delete Dictionary Entry
del student_info["major"]

# Task 5: Dictionary Methods
print(student_info.get("graduation_year"))  # Output: 2024
print(student_info.keys())  # Output: dict_keys(['name', 'age', 'courses', 'graduation_year'])
print(student_info.values())  # Output: dict_values(['Alice', 24, ['Algorithms', 'Data Structures', 'Operating Systems'], 2024])

# Task 6: Iterate Over Dictionary
for key, value in student_info.items():
    print(f"{key}: {value}")

# Task 7: Nested Dictionaries
university_info = {
    "name": "b",
    "location": "a",
    "departments": {
        "CS": {
            "chair": "Dr. Smith",
            "students": 1200
        },
        "Math": {
            "chair": "Dr. Johnson",
            "students": 800
        }
    }
}

print(university_info["departments"]["CS"]["chair"])  # Output: Dr. Smith
university_info["departments"]["Math"]["students"] = 850

# Bonus Task: Merge Dictionaries
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 3, 'c': 4}
