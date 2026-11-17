# Scenario 2 - Program 3: Product Inventory Report

# Function that prints the results neatly
def inventory_summary(average, highest, lowest, low_stock):
    print()
    print("--- Inventory Summary ---")
    print("Average quantity :", average)
    print("Highest quantity :", highest)
    print("Lowest quantity  :", lowest)
    print("Low-stock products (< 10 units):", low_stock)


print("Product Inventory Report")

total = 0
highest = 0
lowest = 0
low_stock = 0      # counter for products with fewer than 10 units
product = 1        # loop counter

# Use a while loop to input data for 3 products
while product <= 3:
    name = input(f"Product {product} name: ")
    quantity = int(input(f"Product {product} quantity in stock: "))

    total = total + quantity

    # Count the low-stock products
    if quantity < 10:
        low_stock = low_stock + 1

    # Track the highest and lowest quantities
    if product == 1:
        highest = quantity
        lowest = quantity
    else:
        if quantity > highest:
            highest = quantity
        if quantity < lowest:
            lowest = quantity

    product = product + 1

# Calculate the average quantity
average = total / 3

# Display the results using the function
inventory_summary(average, highest, lowest, low_stock)
