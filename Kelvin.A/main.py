import sys
import csv

## Input user for 1,2,3 options
user = input('Enter a num: 1. Login, 2. Register, 3. Quit: ')

##List of logins
logins = []
## Turns detail. csv into a list
with open('details.csv') as details:
    reader = csv.DictReader(details, fieldnames=['user', 'password'])
    for row in reader:
        logins.append({'user': row['user'], 'password': row['password']})

## Login
if user == '1':
    try:
        detail = input('what is up (u,p), press 1 to quit: ')
        a = detail.split(',')
        user,password = a[0], a[1]
        simple = user,password
        if simple in logins:
            print('logged in')
        else:
            try:
                x = input('1. retry, 2. quit')
                if x == '1':
                    print('placeholder')
                elif x == '2':
                    sys.exit(1)
            except ValueError:
                sys.exit(1)
    except IndexError:
        print('in format of "username,password"')
## User register 
elif user == '2':
    new = input("new username and password? (A,B): ").split(',')
    user_2,password_2 = new[0], new[1]
    userS = new[0], new[1]
    logins.append({'user': new[0], 'password': new[1]})
    print(logins)
elif user == '3':
    print('quitting')
    sys.exit(1)
else:
    print('invalid')
    sys.exit(1)















