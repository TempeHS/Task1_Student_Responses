import csv
import sys

login = []

# the register
user = input("1. Login, 2. Register, 3. Quit ")

## logn and checks if the username and password is in the storage
if user == "Login":
    input("Username? ")
    input("Password? ")

if user in "storage.csv":
    print("Valid Confirmation!")

## checks the register if it is more than 4 
## enter username and password
## inputs username and password into a storage
if user == "Register":
    username = input("Enter Username: ")
    password = input("Enter Password: ")

with open("storage.csv", "a") as file:
	writer = csv.DictWriter(file, fieldnames=["username", "password"])
	writer.writerow({"username": username, "password": password})

if password < 4:
    x = password
    while x < 4:
        print("Must be a 4+ letter password")

#incorrect password

#incorrect username 

# quit

# logout
