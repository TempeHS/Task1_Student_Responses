# menu loads
def main():
    login = get_password()
    register = get_username , get_password
    quit = quit_menu


#Login Script loop 
def get_password():
    while True:
        password = input("password")
        if password == patu:
            break
        return password

def get_username():
    while True:
        username = input("username")
        if username == grogu:
            break
        return username

def register():
    while True:
        new_password = input("new password")
        if new_password < 4:
            break
        return False


def quit():
    while True:
            quit
main()
# quit menu item 


#incorrect combination
# incorrect username
# incorrect password
x = input("What's the user name?")
y = input("What's the password?")


if x != grogu:
    print("Incorrect username")

if y != patu:
    print("Incorrect password")
else:
    print("login success")
#login success
# when the password and the username met the requirement 
# after login success the menu will be updated 
# will ask if you want to change the password or just logout


# if chose to change the password
# the password character requirements (minimum of 4 character)
#if user type less than the requirement, ask him again until met the requiresment of minimum of 4 character
# after the password change user go back to the main menu 

# elif user chose to log out simply quit 

# login with new login details 
# after change the password 
# user can login again from the main menu using the new pw and the username


# if the user pick register at the start of the menu
# ask the user to create a newuser/ password which need to met the requirements

