import random  # For generating random numbers
from asgn7_module import Car, Model_1, Model_2  # Import classes from module

# Main function
def main():
    # Create object myCar of class Model_1
    myCar = Model_1()
    # Display the color of myCar using the getColor method
    print("Your car is Model_1 and the color is {}".format(myCar.getColor()))
    # Sound the horn of myCar
    myCar.soundHorn()
    
    # Create object computerCar of class Model_2
    computerCar = Model_2()
    # Display the color of computerCar using the getColor method
    print("The computer's car is Model_2 and the color is {}".format(computerCar.getColor()))
    # Sound the horn of computerCar
    computerCar.soundHorn()
    
    # Infinite loop for game
    while True:
        # Ask user for input to drive more or not
        drive_more = input("Drive some more? (y/n): ").strip()
        
        # Check if user wants to exit the game
        if drive_more.lower() == "n":
            break
        # Check if user wants to continue the game
        elif drive_more.lower() == "y" or drive_more == "":
            # Generate random numbers for distances
            distance_mine = random.randint(1, 5)
            distance_computer = random.randint(1, 5)
            
            # Update the lines for both cars
            myLine = myCar.showLine(distance_mine)
            computerLine = computerCar.showLine(distance_computer)
            
            # Display the updated lines
            print("(" + myCar.getColor() + ") " + myLine + " (" + str(len(myLine)) + ")")
            print("(" + computerCar.getColor() + ") " + computerLine + " (" + str(len(computerLine)) + ")")

            
            # Check for game-over conditions
            if len(myLine) >= 50 and len(computerLine) >= 50:
                print("It's a tie!")
                break
            elif len(myLine) >= 50:
                print("You win!")
                break
            elif len(computerLine) >= 50:
                print("Computer wins!")
                break

# Run the main function when script is executed
if __name__ == "__main__":
    main()
