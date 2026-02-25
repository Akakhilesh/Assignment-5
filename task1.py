student_details={
    "Alice":85,
    "Bary":90,
    "Cathy":76.9,"David":65.2,
    "Roshan":25.6,
    "Henry":56.7,
    "Kabita":68.2}

search_name=input("Enter student name: ")           # Ask the user for input
search_name=search_name.strip()                     # Removes any extra spaces of the input String
found=False                                         # A simple boolean to track if we successfully matched a name
for name,mark in student_details.items():
    if name.lower() == search_name.lower():
        print(f"{name} mark: {mark}")
        found=True
        break
if not found:
    print("Student Not found")
