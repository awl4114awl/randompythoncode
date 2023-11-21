def main():

    answer = input("Do you want to know how to dress today? (Yes/No) ")

    if answer.lower() == "yes":
        askQuestions()
    else:
        print("Hope you don't get caught in the rain!")
        print("END OF PROGRAM")     
        
        
def askQuestions():
    first_name = input("Enter your first name: ")
    
    num_locations_input = input("How many locations do you want to check? ")
        
    if num_locations_input.isdigit():
        num_locations = int(num_locations_input)
        print("Hello, " + first_name + "! You want to check " + str(num_locations) + " locations.")
        checkLocations()
    else:
        print("You did not enter a valid number.")
        print("END OF PROGRAM")
        
        
def checkLocations():
    valid_locations = "London" 
    valid_locations = "Chicago"
    valid_locations = "India"
    num_locations = 5
    print("Note: The only valid locations answers are London, Chicago, or India")
    location_count = 0

    while location_count < num_locations:
        valid_locations = input("What location should I check? ")

        if valid_locations.lower() == "bye":
            print("END OF PROGRAM")
            break
            
        if valid_locations == "London":
            print("It's Spring. Dress for mild weather.")           
        if valid_locations == "Chicago":
            print("It's Winter.  Bundle Up.")            
        if valid_locations == "India":
            print("It's Really Hot!  Put on some sunscreen.")
            
        if valid_locations != valid_locations:
            print("Location Not Found")    
        location_count += 1    
        
        if location_count < 0:
            print("You may not check any other locations!")
            print("END OF PROGRAM")        
            
if __name__ == "__main__":
    main()