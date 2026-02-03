# Set operations
fruits_set = {"apple", "banana", "cherry"}
fruits_set.add("orange")
fruits_set.remove("banana")
another_set = {"grape", "apple", "melon"}
print("Union:", fruits_set | another_set)
print("Intersection:", fruits_set & another_set)
print("Difference:", fruits_set - another_set)
# Dictionary operations
student_dict = {"name": "John Doe", "age": 21, "major": "CS"}
student_dict["GPA"] = 3.8
del student_dict["age"]
student_dict["name"] = "Jane Doe"
for key, value in student_dict.items():
 print(f"{key}: {value}")