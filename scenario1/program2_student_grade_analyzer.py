# Scenario 1 - Program 2: Student Grade Analyzer

print("Student Grade Analyzer")

# Ask how many students will be graded (ask again if the input is wrong)
while True:
    try:
        num_students = int(input("Enter number of students: "))
        if num_students > 0:
            break
        else:
            print("Number of students must be more than 0.")
    except:
        print("Invalid input! Please enter a whole number.")

total = 0        # sum of all grades
highest = 0      # start with the smallest possible grade
lowest = 100     # start with the largest possible grade

# Use a for loop to repeat the steps for each student
for i in range(num_students):
    name = input("Enter student name: ")

    # Use try/except to handle invalid numeric input (ask again if wrong)
    while True:
        try:
            grade = float(input(f"Enter grade for {name}: "))
            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100.")
            else:
                break
        except:
            print("Invalid input! Please enter a number.")

    # Add the grade to the total
    total = total + grade

    # Check if this grade is the highest
    if grade > highest:
        highest = grade

    # Check if this grade is the lowest
    if grade < lowest:
        lowest = grade

# Calculate the average grade
average = total / num_students

# Print the results
print()
print("Average grade:", average)
print("Highest grade:", highest)
print("Lowest grade:", lowest)
