from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format "YYYY-MM-DD HH:MM:SS".
    """
    current_date = datetime.now()  # Save the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date():
    """
    Calculates and prints a future date based on the number of days entered by the user.
    """
    try:
        days = int(input("Enter the number of days to add to the current date: "))  # Get user input
        future_date = datetime.now() + timedelta(days=days)  # Calculate future date
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer.")


def main():
    """
    Main function to execute the program.
    """
    display_current_datetime()  # Part 1: Display the current date and time
    calculate_future_date()     # Part 2: Calculate and display the future date


if __name__ == "__main__":
    main()

