# Scenario 1 - Program 2: Student Grade Analyzer

print("Student Grade Analyzer")

# Ask how many students will be graded (keep asking until a valid number is entered)
while True:
    try:
        num_students = int(input("Enter number of students: "))
        break
    except:
        print("Invalid input! Please enter a whole number.")

# Variables to store the total, highest and lowest grades
total = 0
highest = 0
lowest = 0

# Use a for loop to enter the name and grade of each student
for i in range(num_students):
    student_name = input("Enter student name: ")

    # Use try/except to handle invalid numeric input
    while True:
        try:
            grade = float(input(f"Enter grade for {student_name}: "))
            break
        except:
            print("Invalid input! Please enter a number.")

    # Add the grade to the total
    total = total + grade

    # Find the highest and lowest grades
    if i == 0:
        highest = grade
        lowest = grade
    else:
        if grade > highest:
            highest = grade
        if grade < lowest:
            lowest = grade

# Calculate the average grade
average = total / num_students

# Print the results
print()
print("Average grade:", average)
print("Highest grade:", highest)
print("Lowest grade:", lowest)
