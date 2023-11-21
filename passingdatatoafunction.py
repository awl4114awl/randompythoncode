def format_name(firstname, lastname):
    full_name = lastname + ", " + firstname
    print("THE FORMAL PRESENTATION OF YOUR NAME IS:",fullname)
    
def main():
    first_name = input("WHAT IS YOUR FIRST NAME? ")
    last_name = input("WHAT IS YOUR LAST NAME? ")
    format_name(first_name, last_name)
    
main()