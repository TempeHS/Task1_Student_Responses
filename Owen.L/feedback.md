# Feedback

### **Strengths**
1. **Basic Structure**:
   - The code attempts to implement a menu system with options for registering, logging in, and quitting.
   - It includes placeholders for key functionalities like password change and logout.

2. **Use of Functions**:
   - Functions like `Menu_inputs`, `Logout`, and `PswrdChange` are defined, which is a good practice for modularity.

---

### **Issues and Suggestions for Improvement**

#### 1. **Code Does Not Run**
   - The code has several syntax and logical errors that prevent it from running:
     - `Menu` is referenced before being defined in multiple places.
     - The `if` conditions (`if Menu == Login`, `if Menu == register`, etc.) are invalid because `Menu` is not defined, and `Login`/`register` are not strings or variables.
     - The `Menu_inputs` function is incomplete and does not return or set the `Menu` variable.

   **Fix**: Ensure `Menu` is properly defined and passed to the relevant functions. Use strings for menu options.

   Example:
   ```python
   def menu_inputs():
       menu = input("Do you want to register, login, or quit? ").strip().lower()
       return menu
   ```

---

#### 2. **Unfinished and Incorrect Logic**
   - **Login Functionality**:
     - The `userandpasswordcheck` function is incomplete and hardcoded to check against `grogu` and `patu`, which makes it non-functional for other users.
     - It does not read from the `plain_text.txt` file to validate usernames and passwords.

   **Fix**: Implement file reading to validate credentials.

   Example:
   ```python
   def user_and_password_check():
       username = input("Username: ").strip()
       password = input("Password: ").strip()
       try:
           with open("plain_text.txt", "r") as file:
               for line in file:
                   stored_user, stored_password = line.strip().split(",")
                   if username == stored_user and password == stored_password:
                       print("Welcome in!")
                       return True
           print("Incorrect Username or Password.")
           return False
       except FileNotFoundError:
           print("Error: 'plain_text.txt' not found.")
           return False
   ```

   - **Password Change**:
     - The `PswrdChange` function is incomplete and does not implement the logic to update the password in the file.

   **Fix**: Implement password change functionality.

   Example:
   ```python
   def password_change(username):
       new_password = input("Enter a new password: ").strip()
       rows = []
       with open("plain_text.txt", "r") as file:
           for line in file:
               stored_user, stored_password = line.strip().split(",")
               if stored_user == username:
                   rows.append(f"{stored_user},{new_password}")
               else:
                   rows.append(line.strip())
       with open("plain_text.txt", "w") as file:
           file.write("\n".join(rows) + "\n")
       print("Password changed successfully!")
   ```

   - **Registration**:
     - The `makenewaccount` function has incorrect logic for validating username and password lengths. The conditions (`if NewUser > [4]` and `if NewPswrd <= [4]`) are invalid.

   **Fix**: Use `len()` to check the length of strings.

   Example:
   ```python
   def make_new_account():
       new_user = input("What do you want your username to be? ").strip()
       new_password = input("What do you want your password to be? ").strip()
       if len(new_user) < 4:
           print("Username must be at least 4 characters long.")
           return
       if len(new_password) < 4:
           print("Password must be at least 4 characters long.")
           return
       with open("plain_text.txt", "a") as file:
           file.write(f"{new_user},{new_password}\n")
       print("Username and password set successfully!")
   ```

---

#### 3. **Hardcoding and Lack of Flexibility**
   - Hardcoding values like `grogu` and `patu` for username and password makes the code inflexible and unusable for other users.

   **Fix**: Use a file-based or database-based approach to store and validate credentials.

---

#### 4. **Menu Logic**
   - The menu logic is scattered and incomplete. The `Menu_inputs` function does not return the user's choice, and the menu options (`Login`, `register`, `quit`) are not handled properly.

   **Fix**: Centralize the menu logic and ensure proper handling of user input.

   Example:
   ```python
   def main_menu():
       while True:
           menu = input("Do you want to register, login, or quit? ").strip().lower()
           if menu == "login":
               if user_and_password_check():
                   print("Login successful!")
           elif menu == "register":
               make_new_account()
           elif menu == "quit":
               print("Stopping program.")
               sys.exit(0)
           else:
               print("Invalid option. Please choose 'register', 'login', or 'quit'.")
   ```

---

#### 5. **Code Readability**
   - **Inconsistent Naming**: Function names like `Menu_inputs`, `userandpasswordcheck`, and `makenewaccount` use inconsistent naming conventions. Stick to `snake_case` for Python.
   - **Lack of Comments**: The code lacks comments to explain the logic.
   - **Unused Functions**: Functions like `Logout` and `PswrdChange` are defined but not used.

   **Fix**: Use consistent naming, add comments, and remove unused code.

---

#### 6. **Input Validation**
   - The code does not validate user input properly. For example:
     - It does not handle invalid menu options.
     - It does not check for empty usernames or passwords.

   **Fix**: Add input validation to handle invalid or empty inputs.