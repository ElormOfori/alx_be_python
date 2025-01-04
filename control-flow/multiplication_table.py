# multiplication_table.py

# Prompt the user to enter a number
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Generate and print the multiplication table using a for loop
print(f"Multiplication Table for [number]:")
for i in range(1, 11):
    product = number * i
    print(f"[number] * [i] = [product]")
