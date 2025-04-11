#menu
loginsexit = ["Ancient enimes r us", "I'm Your Father", "May the Force be with you", "patu", "Yoda", "I Am All The Jedi", "May the Force be with you"]
logins = []
menu_options = input("login: 1\nregister: 2\nexit: 3\nChoice: ")
#if for 1
if menu_options == "1":
    login_username = input("username: ")
    #opens file to check if username and password are in
    with open("logins.csv") as file:
        print(login_username)
        for line in file:
            if login_username in line:
                listusername = []
                listpassword = []
                login_password = input("Whats your password: ")
                username, password = line.rstrip().split(",")
                password = password.strip()
                # print(f"{username},{password}")
                #get the index of the username
                index = login_password[1]
                #checks if password is in the value corrosponding the the username, dosent work :( properly
                for line in index:
                    if password in loginsexit:
                        #asks if to change password or sxt
                        login_options = input("change password: 1\nLogout: 2\nChoice: ")
                        #if change password opens files as read
                        if login_options == "1":
                            with open("logins.csv") as file:
                                #creates new line to append file execpt for changeding line
                                for line in file:
                                    templist = []
                                new_password = input("New password: ")
                                
                                #opens files as write and writes templist to file
                            with open("logins", "w") as file:
                                file.write(templist)
                        else:
                            exit
                    else:
                        print("invalid password")
            else:
                print("username not found")
#if for register 2
elif menu_options == "2":
    register_username = input("new username: ")
    register_password = input("New password: ")
    if len(register_password) < 4:
        print("to small")
    else:
        logins.append(f"{register_username},{register_password}")
    #add usernames to file
    with open("logins.csv", "a") as file:
        loginsexit.append(f"{register_username},{register_password}")
        file.write(f"\n{register_username},{register_password}")
#if for exit
elif menu_options == "3":
    exit
else:
    print("pick a valid option")
