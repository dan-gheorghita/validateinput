```python
# Infinite loop to repeatedly ask for user input until valid age is entered
while True:
    # Prompt user to enter their age
    print('Enter your age:')
    # Get user input for age
    age = input()
    
    # Check if the input is a decimal number
    if age.isdecimal():
        # If valid, break out of the loop
        break
    # If not a decimal number, prompt user to enter a number
    print('Please enter a number for your age.')

    # Another infinite loop to repeatedly ask for password input until valid password is entered
    while True:
        # Prompt user to enter a new password with certain conditions
        print('Select a new password (letters and numbers only):')
        # Get user input for password
        password = input()
        
        # Check if the input contains only alphanumeric characters
        if password.isalnum():
            # If valid, break out of the loop
            break
        # If not alphanumeric, prompt user to enter a password with letters and numbers
        print('Passwords can only have letters and numbers.')
```