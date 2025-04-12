# Feedback

### **Strengths**
1. **Basic Structure**:
   - The code is modular, with separate functions for `login_page`, `main_menu`, `change_password`, and `register_user`.
   - It uses a `while True` loop for the main menu and the initial task selection, which ensures the user can navigate through the program.

2. **File Handling**:
   - The code uses a CSV file (`source.csv`) to store and retrieve user credentials, which is a good starting point for managing user data.

3. **Password Validation**:
   - The `change_password` function includes basic validation to ensure the new password is at least 4 characters long.

---

### **Issues and Suggestions for Improvement**

#### 1. **Incomplete Login Logic**
   - The `login_page` function reads the `source.csv` file but does not validate the entered username and password against the stored credentials.
   - After reading the file, it directly calls `main_menu()` without checking if the login was successful.

   **Fix**: Add logic to validate the username and password.

   Example:
   ```python
   def login_page():
       username = input("Enter username: ")
       password = input("Enter password: ")
       with open("source.csv") as source:
           for line in source:
               s_username, s_password = line.rstrip().split(",")
               if username == s_username and password == s_password:
                   print("Login successful!")
                   main_menu()
                   return
       print("Invalid username or password.")
   ```

---

#### 2. **Password Change Logic**
   - The `change_password` function does not update the password in the `source.csv` file. It only prints "Password changed" without actually saving the new password.

   **Fix**: Implement logic to update the password in the file.

   Example:
   ```python
   def change_password():
       username = input("Enter your username: ")
       new_password = input("Enter new password: ")
       if len(new_password) < 4:
           print("Password too short.")
           return
       rows = []
       with open("source.csv", "r") as source:
           for line in source:
               s_username, s_password = line.rstrip().split(",")
               if s_username == username:
                   rows.append(f"{s_username},{new_password}")
               else:
                   rows.append(line.rstrip())
       with open("source.csv", "w") as source:
           source.write("\n".join(rows) + "\n")
       print("Password changed successfully!")
   ```

---

#### 3. **Error Handling**
   - The code does not handle potential errors, such as:
     - Missing or empty `source.csv` file.
     - Malformed data in the file.
     - Duplicate usernames during registration.

   **Fix**: Add error handling for file operations and input validation.

   Example:
   ```python
   def register_user():
       new_username = input("Enter new username: ")
       new_password = input("Enter new password: ")
       if len(new_password) < 4:
           print("Password too short.")
           return
       try:
           with open("source.csv", "r") as source:
               for line in source:
                   s_username, _ = line.rstrip().split(",")
                   if s_username == new_username:
                       print("Username already exists.")
                       return
       except FileNotFoundError:
           pass  # File will be created if it doesn't exist
       with open("source.csv", "a") as source:
           source.write(f"{new_username},{new_password}\n")
       print("New login details saved.")
   ```

---

#### 4. **Case Sensitivity**
   - The program is case-sensitive for menu options (e.g., "Login" vs. "login"). This can lead to user frustration.

   **Fix**: Normalize user input by converting it to lowercase.

   Example:
   ```python
   task = input("What would you like to do: \n Login \n Register \n Quit\n").strip().lower()
   if task == "login":
       login_page()
   elif task == "register":
       register_user()
   elif task == "quit":
       break
   else:
       print("Please choose an available option.")
   ```

---

#### 5. **Code Readability**
   - **Inconsistent Naming**: Function names like `login_page` and `register_user` are clear, but `m_task` and `task` are less descriptive.
   - **Lack of Comments**: The code lacks comments to explain the purpose of each function and key logic.

   **Fix**: Use descriptive variable names and add comments.

   Example:
   ```python
   # Main menu function, allows the user to change password or log out
   def main_menu():
       while True:
           user_choice = input("Hello user, what would you like to do: \n Change Password \n Logout\n").strip().lower()
           if user_choice == "change password":
               change_password()
           elif user_choice == "logout":
               break
           else:
               print("Please choose an available option.")
   ```

---

#### 6. **Security Concerns**
   - Storing passwords in plain text in `source.csv` is insecure.

   **Fix**: Use a hashing library like `bcrypt` or `hashlib` to store hashed passwords instead of plain text.

   Example:
   ```python
   import bcrypt

   salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"

   # Hashing a password
   hashed_password = bcrypt.hashpw(password.encode(), salt=salt)

   # Verifying a password
   if bcrypt.checkpw(input_password.encode(), hashed_password):
       print("Login successful!")

   def register_user():
       new_username = input("Enter new username: ")
       new_password = input("Enter new password: ")
       hashed_password = hash_password(input_password.encode())
       with open("source.csv", "a") as source:
           source.write(f"{new_username},{hashed_password}\n")
       print("New login details saved.")
   ```