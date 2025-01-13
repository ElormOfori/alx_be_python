# weather_advice.py

def get_weather_advice():
    """Prompt the user for the weather and provide clothing recommendations."""
    # Prompt user for weather input
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

    # Provide recommendations based on the weather condition
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

# Run the function if this script is executed
if __name__ == "__main__":
    get_weather_advice()
