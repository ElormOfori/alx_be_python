# pattern_drawing.py

# Prompt the user to enter the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
    exit()

# Draw the square pattern
row = 0
while row < size:  # Iterate through rows
    for _ in range(size):  # Print asterisks for each column in the row
        print("*", end="")
    print()  # Move to the next row
    row += 1
