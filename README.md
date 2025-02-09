# Tkinter Calculator ![Python](https://img.shields.io/badge/Python-3.x-blue)  ![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)  ![License](https://img.shields.io/badge/License-MIT-red)

A simple yet powerful calculator application built using Python's Tkinter library. This project showcases my journey of creating a functional GUI-based calculator, including the challenges I faced and how I overcame them. It supports basic arithmetic operations, decimal calculations, and error handling.

---

## Table of Contents

1. [Features](#features)
2. [How I Built It](#how-i-built-it)
   - [Key Insights](#key-insights)
   - [Challenges and Solutions](#challenges-and-solutions)
3. [Requirements](#requirements)
4. [Screenshot](#screenshot)


---

## Features

- **Basic Arithmetic Operations**: Addition (`+`), subtraction (`-`), multiplication (`×`), and division (`÷`).
- **Clear Functionality**: A `C` button to reset the display.
- **Decimal Support**: Allows decimal point (`.`) for floating-point calculations.
- **Error Handling**: Displays an "Error" message for invalid expressions.
- **User-Friendly Interface**: Clean and intuitive layout.

---

## How I Built It

### Key Insights

1. **Tkinter Basics**:
   I used Python's built-in `tkinter` library to create the GUI. The `Entry` widget was used for the display, and `Button` widgets were used for the calculator keys.
   - **Grid Layout**: I used the `grid()` method to arrange buttons in a structured manner, making the interface clean and user-friendly.

2. **Event Handling**:
   Each button is linked to a function using the `command` parameter. For example:

   ```python
   btn_1 = Button(mw, text='1', command=lambda: btn_click("1"), **btn_config)
The btn_click() function updates the display with the clicked number or operator.

3.**Dynamic Evaluation**:
The calculate() function uses Python's eval() to evaluate the expression entered in the display. This was a simple yet powerful way to handle arithmetic operations.  The expression string is taken directly from the display widget.

4.**Error Handling**:
To handle invalid expressions (e.g., division by zero or syntax errors), I wrapped the eval() function in a try-except block:

Python

try:
    result = eval(db.get())  # db is the Entry widget
    db.delete(0, END)
    db.insert(END, result)
except (SyntaxError, ZeroDivisionError):
    db.delete(0, END)
    db.insert(END, "Error")
    
###Challenges and Solutions

Challenge:  Ensuring correct order of operations with eval() and handling user input required careful design.

Solution: eval() handles operator precedence correctly. User input is treated as a standard mathematical expression, and eval() respects operator precedence.  The btn_click() function appends characters to the display string, allowing the user to construct complex expressions.

Challenge: Robust error handling was crucial.

Solution: The try-except block around eval() catches SyntaxError and ZeroDivisionError, displaying "Error" to the user. This prevents the application from crashing and provides feedback to the user.

---

##Requirements
Python 3.x
Tkinter (usually included with Python)
Installation
No special installation is required as Tkinter is a built-in Python library.  Just clone the repository:

---

##Screenshots
python calculator.py 
![calculator](https://github.com/user-attachments/assets/d341bbfe-0337-476f-92c6-4e403f762aa1)
