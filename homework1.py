

class DateInputError(Exception): pass

def is_valid_date(y, m, d):
    from datetime import date
    try: date(y, m, d); return True
    except: return False

def calc_age(y, m, d):
    from datetime import date
    today = date.today()
    if today.month > m or (today.month == m and today.day >= d):
        birthday_passed = True
    else:
        birthday_passed = False
    age = today.year - y
    if not birthday_passed:
        age -= 1
    return age

def check_not_future(y, m, d):
    from datetime import date
    entered = date(y, m, d)
    today = date.today()
    if entered > today:
        return False
    return True  # valid date, not in future

while True:
    user_input = input("Enter the year of Your birth: ")
    try:
        year = int(user_input)
        if (year <= 0):
            raise DateInputError("Please enter positive year")
        if (not check_not_future(year, 1, 1)):
            raise DateInputError("Provided year is in future")
        break
    except (ValueError, TypeError):
        print("This is not a proper year pls try again.")
    except DateInputError as e:
        print(e)


while True:
    user_input = input("Enter month (number) of Your birth: ")
    try:
        month = int(user_input)
        if month <=0 or month >=13:
            raise ValueError("Pls try again, months has to be some value between 1 and 12")
        if (not check_not_future(year, month, 1)):
            raise DateInputError("Provided month is in future")
        break
    except (ValueError, TypeError):
        print("This is not a valid date pls try again.")

while True:
    user_input = input("Enter the day of Your birth: ")
    try:
        day = int(user_input)
        if is_valid_date(year, month, day):
            raise ValueError("Pls try again, months has to be some value between 1 and 12")
        if (not check_not_future(year, month, 1)):
            raise DateInputError("Provided day is in future")
        break
    except (ValueError, TypeError):
        print("This is not a valid date pls try again.")

age_categories = [
    (0, 17, "I"),
    (18, 36, "II"),
    (37, 60, "III")
]

age = calc_age(year, month, day)
def get_category():
    for min_age, max_age, cat in age_categories:
        if min_age <= age <= max_age:
            return cat
    return "Unknown"

print("These are the age categories:")
print(f"{'Age Range':<10}\t{'Category'}")
for min_age, max_age, cat in age_categories:
    print(f"{min_age}–{max_age:<7}\t{cat}")

print(f"Your age is: {age} years")
print(f"\nAge {age} belongs to {get_category(age)} category")
