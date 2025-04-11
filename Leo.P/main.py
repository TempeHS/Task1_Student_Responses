# user logs in
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    ## check login for correct username and password
    ## IF password or username incorrect
    ## reprompt user with login screen
    ## IF password and username correct
    ## prompt user with new menu 

# register user
def register():
    chosen_username = input("Choose a username: ")
    chosen_password = input("Choose a password: ")
    if chosen_password < 4:
        i = chosen_password
        while i < 4:
            print("Your password must be a minimum of 4 characters.")
    else:
        with open("plain_text.txt", "a") as file:
	        file.write(f"{chosen_username}, {Chosen_password}\n")

# quit option
def quit():
    exit()

def new_menu():
    print("1. Change password")
    print("2. Logout")
    log_or_change = input("What would you like to do? ")
    if log_or_change == 1:
        print()
    ## offer user new menu depending on input

# User is offered a menu
def menu():
    print("1. Login")
    print("2. Register")
    print("3. Quit")
    selection = input("Select an option: ")
    if selection == 1:
        login()
    elif selection == 2:
        register()
    elif selection == 3:
        quit()
    else:
        print("Not a valid input.")

menu()