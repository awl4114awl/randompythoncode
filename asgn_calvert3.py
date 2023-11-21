valid_locations = ["London", "Chicago", "India"]

def main():
    user_input = input("Do you want to know how to dress today? (Yes/No) ")
    if user_input.lower() == "yes":
        askQuestions()
    else:
        print("Hope you don't get caught in the rain!")
        print("END OF PROGRAM")
        
def askQuestions():
    first_name = input("Enter your first name: ")

    while True:
        num_locations_input = input("How many locations do you want to check? ")
        if num_locations_input.isdigit():
            num_locations = int(num_locations_input)
            break
        else:
            print("You did not enter a valid number.")

    print("Hello, " + first_name + "! You want to check " + str(num_locations) + " locations.")
    checkLocations(num_locations)

def checkLocations(num_locations):
    valid_locations = ["London", "Chicago", "India"]

    print("Note: The only valid locations answers are London, Chicago, or India")

    location_count = 0
    reached_limit = False

    while location_count < num_locations:
        valid_locations = input("What location should I check? ")

        if valid_locations == "bye":
            print("END OF PROGRAM")
            break

        location_count += 1

if valid_locations == "London" or valid_locations == "Chicago" or valid_locations == "India":
    if valid_locations == "London":
        print("It's Spring. Dress for mild weather.")
    if valid_locations == "Chicago":
        print("It's Winter. Bundle Up.")
    if valid_locations == "India":
        print("It's Really Hot! Put on some sunscreen.")
else:
    print("Location Not Found")

if location_count == num_locations:
    print("You may not check any other locations!")
    print("END OF PROGRAM")


def main():
    dress_today = input("Do you want to know how to dress today? (Yes/No): ")

    if dress_today.lower() == "yes":
        askQuestions()
    else:
        print("We hope you don't get caught in the rain.")
        print("END OF PROGRAM")

if __name__ == "__main__":
    main()
