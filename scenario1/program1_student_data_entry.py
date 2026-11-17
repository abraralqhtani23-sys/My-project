# Scenario 1 - Program 1: Student Data Entry

print("Student Information Entry")

# Ask the user to enter the student name and major
name = input("Enter your name: ")
major = input("Enter your major: ")

# Print both values
print()
print("Your name is:", name)
print("Your major is:", major)

# Display the length of the name using len()
length = len(name)
print("Length of your name is:", length)

# Check whether the word "Ali" appears in the name (membership check)
if "Ali" in name:
    print("The word 'Ali' is found in your name.")
else:
    print("The word 'Ali' is not found in your name.")

# Display the first 3 letters of the name using slicing
first_three = name[:3]
print("The first three letters of your name are:", first_three)
