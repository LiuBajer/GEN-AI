def bool_to_yes_no(value: bool) -> str:
    return "Yes" if value else "No"
voting_age = 18
salutation = "Hey Heyyyyyyyyyyiiiii!!!"
ageText = input("Write Your age pls: ")
age = int(ageText)
height = 186
is_old_enough_to_vote = age >= voting_age
is_married = True

# sekancioje ejluteje programa turetu isspausdinti pasisveikinima.
print(f"{salutation} My age is {age} years and height {height} centimeters")
print(f"am i old enough to vote? {bool_to_yes_no(is_old_enough_to_vote)}")
print(f"Bin ich verheiratet? {bool_to_yes_no(is_married)}")

if not is_old_enough_to_vote:
    print("Limonado")
else:
    print("Kefyro")


