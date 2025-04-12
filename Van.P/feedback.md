# Feedback

### **Strengths**
1. **Basic Functionality**:
   - The code implements a simple menu system for login, registration, and quitting.
   - It includes a basic password change feature in the `logged` function.

2. **Interactive Design**:
   - The code provides user prompts for input, making it interactive.

---

### **Issues and Suggestions for Improvement**

#### 1. **Hardcoded Usernames and Passwords**
   - The usernames and passwords are hardcoded into the program, which is insecure and not scalable.

   **Fix**: Store usernames and passwords in a file or database. Use password hashing (e.g., `bcrypt`) to securely store passwords.

---

#### 2. **No Password Hashing**
   - Passwords are stored and compared in plain text, which is a major security flaw.

   **Fix**: Use a library like `bcrypt` to hash passwords before storing them and verify hashed passwords during login.

   Example:
   ```python
   import bcrypt

   salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"

   # Hashing a password
   hashed_password = bcrypt.hashpw(password.encode(), salt=salt)

   # Verifying a password
   if bcrypt.checkpw(input_password.encode(), hashed_password):
       print("Login successful!")
   ```

---

#### 3. **Repetitive and Inefficient Code**
   - The code repeatedly checks usernames and passwords using multiple `or` conditions, which is inefficient and hard to maintain.

   **Fix**: Use a dictionary or list to store usernames and passwords for easier lookup.

   Example:
   ```python
   users = {
       "sithLord": "Ancient enimes r us",
       "d_Vader": "I'm Your Father",
       # Add other users here
   }

   if username in users and password == users[username]:
       print("Logged in!")
   ```

---

#### 4. **No Input Validation**
   - The code does not validate user input, which could lead to unexpected behavior or errors.

   **Fix**: Add input validation to ensure usernames and passwords meet certain criteria (e.g., minimum length, no special characters).

---

#### 5. **No Error Handling**
   - The code does not handle errors, such as invalid input or unexpected exceptions.

   **Fix**: Add error handling using `try` and `except` blocks.

   Example:
   ```python
   try:
       menu = int(input("1.Login 2.Register 3.Quit "))
   except ValueError:
       print("Invalid input. Please enter a number.")
   ```

---

#### 6. **Poor User Experience**
   - The prompts and messages are not user-friendly (e.g., "what you finna change it to?").
   - The program does not provide clear feedback when an action is successful or fails.

   **Fix**: Use clear and professional messages for better user experience.

---

#### 7. **No Separation of Concerns**
   - The code mixes logic for login, registration, and menu handling in a single block, making it hard to read and maintain.

   **Fix**: Refactor the code into separate functions for each feature (e.g., `login`, `register`, `change_password`).

---

#### 8. **No Exit Condition for Loops**
   - The `while` loops for username and password validation do not have a clear exit condition, which could lead to infinite loops.

   **Fix**: Add proper exit conditions or break statements.

---

#### 9. **No Data Persistence**
   - The code does not save new users or password changes, so all changes are lost when the program exits.

   **Fix**: Save user data to a file or database.

   Example:
   ```python
   import json

   def save_users(users):
       with open("users.json", "w") as file:
           json.dump(users, file)

   def load_users():
       try:
           with open("users.json", "r") as file:
               return json.load(file)
       except FileNotFoundError:
           return {}
   ```