# Scenario 1 - Program 2: Student Grade Analyzer

print("Student Grade Analyzer")

try:
    # Ask how many students will be graded
    num_students = int(input("Enter number of students: "))

    total = 0

    # Use a for loop to enter the name and grade of each student
    for i in range(num_students):
        name = input("Enter student name: ")
        grade = float(input(f"Enter grade for {name}: "))

        # Add the grade to the total
        total = total + grade

        # The first grade is the starting value for highest and lowest
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

except:
    print("Error, please enter a number.  Please run the program again.")
