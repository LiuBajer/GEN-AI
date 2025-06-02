while True:
    user_input = input("Enter temperature in celcius: ")
    try:
        celsius = float(user_input)
        break
    except (ValueError, TypeError):
        print("This is not a proper number pls try again.")


fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C is {fahrenheit}°F")