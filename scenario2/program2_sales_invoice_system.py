# Scenario 2 - Program 2: Sales Invoice System

# Function that returns the total after the discount (if applicable)
def calculate_invoice(quantity, price):
    total = quantity * price
    if total > 500:
        total = total - (total * 0.05)   # apply 5% discount
    return total


print("Sales Invoice System")

total_sales = 0
customer = 1

# Use a while loop to process 3 customers
while customer <= 3:
    name = input(f"Customer {customer} name: ")

    # Input validation for the quantity using try/except
    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except:
            print("Invalid input! Please enter numbers only.")

    # Input validation for the unit price using try/except
    while True:
        try:
            price = float(input("Unit price (SAR): "))
            break
        except:
            print("Invalid input! Please enter numbers only.")

    # Call the function and print the final invoice
    invoice = calculate_invoice(quantity, price)
    print(f"Final invoice for {name}: {invoice} SAR")
    print()

    # Add the invoice to the total sales
    total_sales = total_sales + invoice
    customer = customer + 1

# Print the total sales after all customers have been processed
print("--- Sales Summary ---")
print(f"Total sales: {total_sales} SAR")
