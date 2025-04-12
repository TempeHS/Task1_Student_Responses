# Feedback

### **Strengths**
1. **Basic Structure**:
   - The code attempts to implement a modular structure with functions for `main`, `register`, `login`, and `menu2`.
   - It uses Python's `match-case` syntax for handling user input, which is a modern and clean approach.

2. **Data Storage**:
   - The `accounts` list and the use of a CSV file (`plain_text.txt`) for storing user credentials show an effort to persist data.

3. **Effort Toward Functionality**:
   - The code includes basic functionality for user registration, login, and password change.

---

### **Issues and Suggestions for Improvement**

#### 1. **Broken Logic in `main`**
   - The `main` function has a `while True` loop, but the `menu` variable is not updated inside the loop. This causes the loop to execute indefinitely with the same input.

   **Fix**: Update the `menu` variable inside the loop.

   Example:
   ```python
   def main():
       while True:
           menu = input('What would you like to do (Login, Register, Quit): ').lower().strip()
           match menu:
               case 'login':
                   login()
               case 'register':
                   register()
               case 'quit':
                   print('End Program')
                   break
               default:
                   print('Invalid option. Please try again.')
   ```

---

#### 2. **Incomplete `login` Function**
   - The `login` function references a `username` variable that is not defined within its scope. It also does not validate the password against the `accounts` list or the CSV file.

   **Fix**: Use the `accounts` list or read from the CSV file to validate the username and password.

   Example:
   ```python
   def login():
       login_username = input('What is your username: ')
       login_password = input('What is your password: ')
       for account in accounts:
           if account['username'] == login_username and account['password'] == login_password:
               print('Login successful!')
               menu2()
               return
       print('Invalid username or password.')
   ```

---

#### 3. **Redundant and Confusing Code**
   - The `password` function is redundant and unnecessarily complex. Password validation should be part of the `login` function.
   - The `menu2` function calls `passchange()`, but `passchange` is not defined.

   **Fix**: Simplify the logic and ensure all functions are properly defined.

---

#### 4. **Inconsistent and Unclear Variable Names**
   - Variables like `menu2`, `register`, and `login` are used as both function names and local variables, which is confusing and can lead to errors.

   **Fix**: Use descriptive and consistent variable names.

   Example:
   ```python
   def menu_after_login():
       choice = input('Login Successful. Change password or Logout: ').lower().strip()
       match choice:
           case 'logout':
               print('Logged out.')
           case 'change password':
               change_password()
           default:
               print('Invalid option.')
   ```

---

#### 5. **Password Change Functionality Missing**
   - The code does not implement a proper password change feature. The `passchange` variable is used but not defined as a function.

   **Fix**: Implement a `change_password` function that updates the password in the `accounts` list or the CSV file.

   Example:
   ```python
   def change_password():
       username = input('Enter your username: ')
       new_password = input('Enter your new password: ')
       for account in accounts:
           if account['username'] == username:
               account['password'] = new_password
               print('Password changed successfully!')
               return
       print('Username not found.')
   ```

---

#### 6. **CSV File Handling**
   - The `register` function writes to the CSV file but does not handle cases where the file does not exist or is malformed.
   - The `login` function does not read from the CSV file.

   **Fix**: Add error handling for file operations and ensure consistency between the `accounts` list and the CSV file.

   Example:
   ```python
   import csv

   def load_accounts():
       try:
           with open('plain_text.txt', 'r') as file:
               reader = csv.DictReader(file)
               return [row for row in reader]
       except FileNotFoundError:
           return []

   def save_account(username, password):
       with open('plain_text.txt', 'a') as file:
           writer = csv.DictWriter(file, fieldnames=['username', 'password'])
           writer.writerow({'username': username, 'password': password})
   ```

---

#### 7. **Hardcoded Passwords**
   - The `password` function uses hardcoded passwords, which is insecure and impractical.

   **Fix**: Remove hardcoded passwords and validate against the `accounts` list or the CSV file.

---

#### 8. **Code Readability**
   - The code lacks comments and proper formatting, making it difficult to understand.

   **Fix**: Add comments and improve formatting.

   Example:
   ```python
   # Main function to handle user input
   def main():
       while True:
           menu = input('What would you like to do (Login, Register, Quit): ').lower().strip()
           match menu:
               case 'login':
                   login()
               case 'register':
                   register()
               case 'quit':
                   print('End Program')
                   break
               default:
                   print('Invalid option. Please try again.')
   ```