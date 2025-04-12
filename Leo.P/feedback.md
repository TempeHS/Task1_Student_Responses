# Feedback

### **Strengths**
1. **Basic Structure**:
   - The code has a clear structure with functions for `login`, `register`, `quit`, and `menu`.
   - It attempts to handle user input and provide a menu-driven interface.

2. **File Handling**:
   - The `register` function writes user credentials to a file (`plain_text.txt`), which is a good step toward persistent storage.

---

### **Issues and Suggestions for Improvement**

#### 1. **Code Does Not Run**
   - The code contains several syntax and logical errors:
     - `if chosen_password < 4` is invalid because `chosen_password` is a string, and strings cannot be compared to integers.
     - `Chosen_password` in `file.write` is undefined (case-sensitive typo).
     - `if log_or_change == 1` and `if selection == 1` compare strings to integers, which will always evaluate to `False`.

   **Fix**: Correct these issues by ensuring proper type handling and fixing typos.

---

#### 2. **Password Validation**
   - The password validation logic in `register` is incorrect:
     - The `while` loop (`while i < 4`) is invalid because `i` is a string, and the loop does not prompt the user to re-enter the password.
   - **Fix**: Use `len(chosen_password)` to check the password length and prompt the user to re-enter it if it is too short.

   Example:
   ```python
   def register():
       while True:
           chosen_username = input("Choose a username: ")
           chosen_password = input("Choose a password (minimum 4 characters): ")
           if len(chosen_password) < 4:
               print("Your password must be a minimum of 4 characters.")
           else:
               with open("plain_text.txt", "a") as file:
                   file.write(f"{chosen_username}, {chosen_password}\n")
               print("Registration successful!")
               break
   ```

---

#### 3. **Login Functionality**
   - The `login` function does not validate the username and password against stored credentials.
   - **Fix**: Read the file containing user credentials and validate the input.

   Example:
   ```python
   def login():
       username = input("Enter your username: ")
       password = input("Enter your password: ")
       with open("plain_text.txt", "r") as file:
           users = [line.strip().split(", ") for line in file.readlines()]
           for user, passw in users:
               if user == username and passw == password:
                   print("Login successful!")
                   new_menu()
                   return
       print("Incorrect username or password. Try again.")
   ```

---

#### 4. **New Menu Functionality**
   - The `new_menu` function is incomplete and does not handle the "Change password" option.
   - **Fix**: Implement the "Change password" functionality and ensure proper input handling.

   Example:
   ```python
   def new_menu():
       print("1. Change password")
       print("2. Logout")
       log_or_change = input("What would you like to do? ")
       if log_or_change == "1":
           change_password()
       elif log_or_change == "2":
           print("Logged out.")
       else:
           print("Invalid input.")
   ```

   Add a `change_password` function:
   ```python
   def change_password():
       username = input("Enter your username: ")
       with open("plain_text.txt", "r") as file:
           users = [line.strip().split(", ") for line in file.readlines()]
       for i, (user, passw) in enumerate(users):
           if user == username:
               new_password = input("Enter a new password (minimum 4 characters): ")
               if len(new_password) < 4:
                   print("Password too short.")
                   return
               users[i][1] = new_password
               with open("plain_text.txt", "w") as file:
                   for user, passw in users:
                       file.write(f"{user}, {passw}\n")
               print("Password changed successfully!")
               return
       print("Username not found.")
   ```

---

#### 5. **Menu Input Handling**
   - The `menu` function compares `selection` (a string) to integers, which will always evaluate to `False`.
   - **Fix**: Convert `selection` to an integer or compare it to strings.

   Example:
   ```python
   def menu():
       while True:
           print("1. Login")
           print("2. Register")
           print("3. Quit")
           selection = input("Select an option: ")
           if selection == "1":
               login()
           elif selection == "2":
               register()
           elif selection == "3":
               quit()
           else:
               print("Not a valid input.")
   ```

---

#### 6. **File Handling**
   - The code appends new credentials to the file but does not handle duplicate usernames.
   - **Fix**: Check for duplicate usernames before writing to the file.

   Example:
   ```python
   def register():
       while True:
           chosen_username = input("Choose a username: ")
           with open("plain_text.txt", "r") as file:
               users = [line.strip().split(", ")[0] for line in file.readlines()]
           if chosen_username in users:
               print("Username already taken. Try again.")
               continue

           chosen_password = input("Choose a password (minimum 4 characters): ")
           if len(chosen_password) < 4:
               print("Your password must be a minimum of 4 characters.")
               continue

           with open("plain_text.txt", "a") as file:
               file.write(f"{chosen_username}, {chosen_password}\n")
           print("Registration successful!")
           break
   ```