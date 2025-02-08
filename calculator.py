from tkinter import *

# Create main window
mw = Tk()
mw.title('Calculator')
mw.configure(bg="lightgray")  # Background color

# Function to handle button clicks
def btn_click(num):
    current_num = db.get()
    db.delete(0, END)
    db.insert(END, current_num + num)

# Function to clear the display
def clear_display():
    db.delete(0, END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(db.get())  # Evaluate the expression
        db.delete(0, END)
        db.insert(END, str(result))
    except Exception:
        db.delete(0, END)
        db.insert(END, "Error")

# Creating display box
db = Entry(mw, width=20, font=("Arial", 30), justify=RIGHT, bd=5)
db.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button configuration (Styling)
btn_config = {"padx": 36, "pady": 14, "font": ("Arial", 13), "bg": "white"}

# Creating number buttons
btn_0 = Button(mw, text='0', command=lambda: btn_click("0"), **btn_config)
btn_1 = Button(mw, text='1', command=lambda: btn_click("1"), **btn_config)
btn_2 = Button(mw, text='2', command=lambda: btn_click("2"), **btn_config)
btn_3 = Button(mw, text='3', command=lambda: btn_click("3"), **btn_config)
btn_4 = Button(mw, text='4', command=lambda: btn_click("4"), **btn_config)
btn_5 = Button(mw, text='5', command=lambda: btn_click("5"), **btn_config)
btn_6 = Button(mw, text='6', command=lambda: btn_click("6"), **btn_config)
btn_7 = Button(mw, text='7', command=lambda: btn_click("7"), **btn_config)
btn_8 = Button(mw, text='8', command=lambda: btn_click("8"), **btn_config)
btn_9 = Button(mw, text='9', command=lambda: btn_click("9"), **btn_config)

# Creating operator buttons
btn_add = Button(mw, text='+', command=lambda: btn_click("+"), **btn_config)
btn_sub = Button(mw, text='-', command=lambda: btn_click("-"), **btn_config)
btn_mul = Button(mw, text='×', command=lambda: btn_click("*"), **btn_config)
btn_div = Button(mw, text='÷', command=lambda: btn_click("/"), **btn_config)
btn_clear = Button(mw, text='C', command=clear_display, **btn_config)
btn_equal = Button(mw, text='=', command=calculate, **btn_config)
btn_decimal = Button(mw, text='.', command=lambda: btn_click("."), **btn_config)

# Showing widgets in grid
btn_7.grid(row=1, column=0, padx=2, pady=2)
btn_8.grid(row=1, column=1, padx=2, pady=2)
btn_9.grid(row=1, column=2, padx=2, pady=2)
btn_div.grid(row=1, column=3, padx=2, pady=2)

btn_4.grid(row=2, column=0, padx=2, pady=2)
btn_5.grid(row=2, column=1, padx=2, pady=2)
btn_6.grid(row=2, column=2, padx=2, pady=2)
btn_mul.grid(row=2, column=3, padx=2, pady=2)

btn_1.grid(row=3, column=0, padx=2, pady=2)
btn_2.grid(row=3, column=1, padx=2, pady=2)
btn_3.grid(row=3, column=2, padx=2, pady=2)
btn_sub.grid(row=3, column=3, padx=2, pady=2)

btn_0.grid(row=4, column=1, padx=2, pady=2)  # Centered 0
btn_decimal.grid(row=4, column=0, padx=2, pady=2)  # Decimal point
btn_equal.grid(row=4, column=2, padx=2, pady=2)
btn_add.grid(row=4, column=3, padx=2, pady=2)

btn_clear.grid(row=5, column=0, columnspan=4, padx=2, pady=2, sticky="we")  # Clear spans all columns

# Run main event loop
mw.mainloop()
