# validateInput.py

**Code Analysis: User Input Validation for Age and Password**

This Python code is designed to validate user input for age and password. The code consists of two main loops: one for validating the age input and another for validating the password input.

**Age Input Validation:**

1. The code enters an infinite loop (`while True`) that continues to prompt the user to enter their age until a valid input is received.
2. The user is prompted to enter their age, and the input is stored in the `age` variable.
3. The code checks if the input is a decimal number using the `isdecimal()` method. This method returns `True` if all characters in the string are decimal characters and there is at least one character, otherwise, it returns `False`.
4. If the input is a decimal number, the loop breaks, and the program proceeds to the next section.
5. If the input is not a decimal number, the user is prompted to enter a number for their