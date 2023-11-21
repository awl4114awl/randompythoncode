print("Check Education Level")

first_name = input("Enter your first name: ")

while True:
	education_level = input("Enter your education level (HS, BS, MS, PhD): ")

	if education_level in ["HS", "BS", "MS", "PhD"]:
		print("Hello, " + first_name + "! You have a " + education_level + " degree.")
		break
	else:
		print("Valid education level not entered, please try again.")