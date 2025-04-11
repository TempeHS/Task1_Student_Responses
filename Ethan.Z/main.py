def Main():
    name = ["sithLord", "d_Vader", "GENERALleia", "grogu", "there_is_no_try", "MyRey", "Luke"]
    Password = ["$2b$12$ieYNkQp8QumgedUo30nuPOQY14I3/FmuJe6Ej91GqWW8RBgf1wfvu", "$2b$12$ieYNkQp8QumgedUo30nuPO.qRDpHPiP0Z/pctrrGccRINm4LQBWlC", "$2b$12$ieYNkQp8QumgedUo30nuPOI22lGwfoSU39wcYoKe4NH2qfVb2b.DK", "$2b$12$ieYNkQp8QumgedUo30nuPO8ROZupPfEGkAYIy3CKPqYVac8AsOOiq", "$2b$12$ieYNkQp8QumgedUo30nuPOJmY35Nd7O1t9Z4NpLlxlXNlU4JaoG.C", "$2b$12$ieYNkQp8QumgedUo30nuPO.KiLuPhQP.JAaPgmmIz3/MFzJGjdjfO", "$2b$12$ieYNkQp8QumgedUo30nuPOI22lGwfoSU39wcYoKe4NH2qfVb2b.DK"]
    Home = input("Would you want to Login, Register or Quit? ").strip().title()
    if Home == "Login":
        Login_account()
    elif Home == "Register":
        Register_account()
    else:
        End_Program()


def Login_account():
    Name = ["sithLord", "d_Vader", "GENERALleia", "grogu", "there_is_no_try", "MyRey", "Luke"]
    Password = ["$2b$12$ieYNkQp8QumgedUo30nuPOQY14I3/FmuJe6Ej91GqWW8RBgf1wfvu", "$2b$12$ieYNkQp8QumgedUo30nuPO.qRDpHPiP0Z/pctrrGccRINm4LQBWlC", "$2b$12$ieYNkQp8QumgedUo30nuPOI22lGwfoSU39wcYoKe4NH2qfVb2b.DK", "$2b$12$ieYNkQp8QumgedUo30nuPO8ROZupPfEGkAYIy3CKPqYVac8AsOOiq", "$2b$12$ieYNkQp8QumgedUo30nuPOJmY35Nd7O1t9Z4NpLlxlXNlU4JaoG.C", "$2b$12$ieYNkQp8QumgedUo30nuPO.KiLuPhQP.JAaPgmmIz3/MFzJGjdjfO", "$2b$12$ieYNkQp8QumgedUo30nuPOI22lGwfoSU39wcYoKe4NH2qfVb2b.DK"]
    Name_Old = input("Username1? ")
    Password_Old = input("Password1? ")
    In_domain()

def In_domain():
    Do = input("Would you like to Change_Password or Quit? ").strip(). title()
    if Do == "Change_Password":
        Change_Password()
    else:
        End_Program()

def End_Program():
    pass

def Register_account():
    Name_New = input("Username? ")
    Password_New = input("Password? ")

    file = open("source.csv", "w")
    file.write(f"{Name_New}, {Password_New}")
    file.close()

def Change_Password():
    Changed = input("New password? ")
    print("Ok, ending program! ")
    End_Program()

Main()