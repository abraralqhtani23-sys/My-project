# Scenario 1 - Program 2: Student Grade Analyzer

print("Student Grade Analyzer")

try:
    # Ask how many students will be graded
    num_students = int(input("Enter number of students: "))

    total = 0        # sum of all grades
    highest = 0      # start with the smallest possible grade
    lowest = 100     # start with the largest possible grade

    # Use a for loop to repeat the steps for each student
    for i in range(num_students):
        name = input("Enter student name: ")
        grade = float(input(f"Enter grade for {name}: "))

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

except:
    print("Error, please enter a number.  Please run the program again.")
