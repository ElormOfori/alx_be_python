# future_age_calculator.py

# Step 1: Prompt the user to input their current age
current_age = int(input("How old are you? "))  # Convert user input to an integer

# Step 2: Calculate the age in 2050
years_to_2050 = 2050 - 2023  # Difference between 2050 and the current year
future_age = current_age + years_to_2050

# Step 3: Print the result
print(f"In 2050, you will be [{future_age}] years old.")
