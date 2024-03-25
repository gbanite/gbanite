# details.py



# pseudocode:
# Define a main function:
#   - Perompt the user to input their name, age, house number, and street name.
#   - Store the input values in variables.
#   - Print a single sentence containing all the details of the user.
# If the script is run as the main program:
#   - Call the main function.



def main():
    #Prompt the user to inoput their name, age, house number, and street name.
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    house_number = input("Enter your house number: ")
    street_name = input("Enter your street name: ")

    # Print a single sentence containing all the details of the user.
    print("\nThis is {}. He is {} years old and lives at house number {} on {}".format(name, age, house, street_namew))

    if __name__ =="__main__":
        main()
