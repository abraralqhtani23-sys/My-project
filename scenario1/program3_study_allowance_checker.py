# Scenario 1 - Program 3: Study Allowance Eligibility Checker

# Function that returns the total allowance based on the GPA
def calculate_allowance(gpa):
    if gpa > 4.5:
        return 840 + 1000      # base allowance + Excellence Bonus
    elif gpa >= 1.0:
        return 840             # base allowance only
    else:
        return 0               # no allowance


print("Study Allowance Eligibility Checker")

try:
    # Ask for the student's name and GPA
    name = input("Enter student name: ")
    gpa = float(input("Enter GPA: "))

    # Call the function
    amount = calculate_allowance(gpa)

    # Display a clear message
    if amount > 0:
        print(f"{name} is eligible and will receive {amount} SAR.")
    else:
        print(f"{name} is not eligible for the study allowance.")

except:
    print("Error, please enter a number.  Please run the program again.")
