import csv
import sys

def Menu_inputs():
    def Menu_prompt():
        Menu = input(" do you want to register, login or quit?") #name error (name Menu is not defined)
        print (Menu)

#Menu Login Function
if Menu == Login:
    def userandpasswordcheck():
            User = input("Username")
            Pswrd = input("Password")
if User != grogu:    #not done fully needs to work on any of the plain_text.txt list
    print('Incorrect Username')
elif Pswrd != patu:
    print("incorrect Password")
else: 
    print("Welcome in")
    Change = input("do you want to change password?")
    logout = input("do you want to logout?")
    def Logout():
        if logout == Yes:
            print("Logging out")
    def PswrdChange():
        if Change == Yes:  #unfinished passwprd change 
            print("what do you want to change it to?")


#Register Function
if Menu == register:
    def makenewaccount():
        NewUser= input("What do you want your Username to be?")
        NewPswrd= input("What do you want your new passwor to be?")
        print(NewUser)
        if NewUser > [4]:
            print(NewPswrd)
            if NewPswrd <= [4]:
                print ("password has to be longer than 4 characters")
        else:
            print("Username And Password set")
            print(Menu)
            
# Save new Username and Password (not done)

#Menu Quit Function
if Menu == quit:
    print("Stopping Program")