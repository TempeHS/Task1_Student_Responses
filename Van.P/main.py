def logged():
    geek = int(input("1.Change password " "2.Log out "))
    if geek == 1:
        change = input("what you finna change it to? ")
        print("Your password", (change), "has been confirmed")
    if geek == 2:
        print("Logged out")



menu = int(input("1.Login " "2.Register " "3.Quit "))

if menu == 1:
    LogUs = input("Username? ")
    while LogUs == ("sithLord") or LogUs == ("d_Vader") or LogUs == ("GENERALleia") or LogUs == ("grogu") or LogUs == ("there_is_no_try") or LogUs == ("MyRey") or LogUs == ("Luke"):
        LogPa = input("Password? ")
        while LogPa == ("Ancient enimes r us") or LogPa == ("I'm Your Father") or LogPa == ("May the Force be with you") or LogPa == ("patu") or LogPa == ("Yoda") or LogPa == ("I Am All The Jedi") or LogPa == ("May the Force be with you"):
            print("Logged in!")
            logged()
        else:
            print("WRONG")
    else:
        print("WRONG")

elif menu == 2:
    RegUs = input("Username? ")
    if RegUs == ("sithLord") or RegUs == ("d_Vader") or RegUs == ("GENERALleia") or RegUs == ("grogu") or RegUs == ("there_is_no_try") or RegUs == ("MyRey") or RegUs == ("Luke"):
        print("Taken")
    elif input("Password? "):
        print("Okay!")
        logged()




elif menu == 3:
    print("Terminated")

    