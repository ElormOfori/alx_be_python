# daily_reminder.py

# Prompt for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Validate priority and time-bound inputs
valid_priorities = {"high", "medium", "low"}
if priority not in valid_priorities:
    print("Invalid priority level. Please enter high, medium, or low.")
    exit()

if time_bound not in {"yes", "no"}:
    print("Invalid response for time-bound. Please enter yes or no.")
    exit()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high-priority task."
    case "medium":
        reminder = f"'{task}' is a medium-priority task."
    case "low":
        reminder = f"'{task}' is a low-priority task."

# Add time-sensitive details if applicable
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Display the customized reminder
print("\nReminder:", reminder)
