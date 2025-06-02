
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obese (Class I)"
    elif bmi < 40:
        return "Obese (Class II)"
    else:
        return "Obese (Class III – Severe)"
    
while True:
    user_input = input("Enter weight in kilograms: ")
    try:
        weight = float(user_input)
        break
    except (ValueError, TypeError):
        print("This is not a proper number pls try again.")

while True:
    user_input = input("Enter height in meters: ")
    try:
        height = float(user_input)
        break
    except (ValueError, TypeError):
        print("This is not a proper number pls try again.")

BMI = weight / (height ** 2)

print(f"Your body mass inded is {BMI}.")
print(f"You are {categorize_bmi(BMI)}.")