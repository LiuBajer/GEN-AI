while True:
    user_input = input("Enter temperature in fahrenheit: ")
    try:
        fahrenheit = float(user_input)
        break
    except (ValueError, TypeError):
        print("This is not a proper number pls try again.")


celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F is {celsius}°C")