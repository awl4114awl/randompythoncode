def main():
    dress_today = input("Do you want to know how to dress today? (Yes/No): ")

    if dress_today.lower() == "yes":
        askQuestions()
    else:
        print("We hope you don't get caught in the rain.")
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

    print("Valid locations: London, Chicago, India")

    location_count = 0

    while location_count < num_locations:
        location = input("What location should I check? ")

        if location == "bye":
            print("END OF PROGRAM")            

        if location == "London":
            print("It's Spring. Dress for mild weather.")
            
        if location == "Chicago":
            print("It's Winter. Bundle Up.")
            
        if location == "India":
            print("It's Really Hot! Put on some sunscreen.")
            
        if location not in valid_locations:
            print("Location Not Found")

        location_count += 1

    print("You may not check any other locations!")
    print("END OF PROGRAM")


if __name__ == "__main__":
    main()
