from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
import sys

# Minimum password length
MIN_LENGTH = 8

"""
Checks password strength based on:
1-) Length >= 8
2-) Contains Uppercase
3-) Contains Lowercase
4-) Contains Digit
5-) Contains Special Characters

Return a score how many criteria were satisfied (0-4)  
"""

def checkPassword(password):
    hasUpper = False
    hasLower = False
    hasDigit = False
    hasSpecialCharacter = False

    # Check password length

    passwd_len = len(password)

    if passwd_len < MIN_LENGTH:
        return ""

    else:
        for char in password:
            if char.isupper():
                hasUpper = True
            elif char.islower():
                hasLower = True
            elif char.isdigit():
                hasDigit = True
            else:
                hasSpecialCharacter = True

        score = 0

        if hasUpper:
            score += 1
        if hasLower:
            score += 1
        if hasDigit:
            score += 1
        if hasSpecialCharacter:
            score += 1

        if score == 1:
            return "Very Weak"
        elif score == 2:
            return "Weak"
        elif score == 3:
            return "Medium"
        elif score == 4:
            return "Strong"

def initUI():
    # It initiates the UI with PyQt6
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Password Strength Checker")
    window.setGeometry(100, 100, 300, 150)

    layout = QVBoxLayout()

    label = QLabel("Enter your password:")
    layout.addWidget(label)

    passwordInput = QLineEdit()
    layout.addWidget(passwordInput)

    resultLabel = QLabel("")
    layout.addWidget(resultLabel)

    def evaluatePassword():
        password = passwordInput.text()
        passwd_len = len(password)
        result = checkPassword(password)
        if passwd_len < MIN_LENGTH:
            resultLabel.setText(f"Your password must be at least {MIN_LENGTH} characters long!!!")
        else:
            resultLabel.setText(f"Strength: {result}")

    checkButton = QPushButton("Check Strength")
    checkButton.clicked.connect(evaluatePassword)
    layout.addWidget(checkButton)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    initUI()
