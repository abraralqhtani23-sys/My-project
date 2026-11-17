# Scenario 2 - Program 1: Customer Registration

print("Customer Registration")

# Ask the user for the customer information
name = input("Enter customer name: ")
phone = input("Enter phone number: ")
membership = input("Enter membership type: ")

# Print all entered information
print()
print("--- Customer Information ---")
print("Name        :", name)
print("Phone       :", phone)
print("Membership  :", membership)

# Display the length of the name using len()
print("Name length :", len(name))

# Check whether the word "gold" appears in the membership type using find()
index = membership.find("gold")
if index != -1:          # find() returns -1 when the word is not found
    print('"gold" found in membership type at index:', index)
else:
    print('"gold" not found in membership type.')

# Display the last 4 digits of the phone number using slicing
print("Last 4 digits of phone:", phone[-4:])
