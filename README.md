# Password Strength Checker

## Description

This is a simple **Password Strength Checker** application built using **PyQt6** in Python. The application evaluates the strength of a given password based on specific criteria and provides feedback to the user.

## Features

- Checks password strength based on:
    - Minimum length (>= 8 characters)
    - Presence of uppercase letters
    - Presence of lowercase letters
    - Presence of digits
    - Presence of special characters
- Provides feedback on password strength:
    - Very Weak
    - Weak
    - Medium
    - Strong
- User-friendly **GUI** built with **PyQt6**

## Requirements

Ensure you have the following installed:

- Python 3.x
- PyQt6

You can install PyQt6 using:

```bash
pip install PyQt6
```

## How to Run

1. Clone the repository or copy the script.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command:
    
    ```bash
    python password_checker.py
    ```
    
5. Enter a password in the input field and click **Check Strength**.

## Password Strength Criteria

|Strength Level|Conditions Met|
|---|---|
|Very Weak|Only 1 criterion|
|Weak|2 criteria|
|Medium|3 criteria|
|Strong|All 4 criteria|

## File Structure

```
PasswordStrengthChecker/
│── password_checker.py  # Main script
│── README.md            # Project documentation
```

## License

This project has MIT License.

## Author

Developed by **Göksel Özdemir**.