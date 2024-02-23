from tkinter import *

win = Tk()
win.title("Calculator")
win.geometry("360x480")  # Adjusted for better proportionality
win.resizable(0, 0)
win.configure(bg='light gray')  # Background color for the window

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    try:
        result = str(eval(expression))  # Using try-except block to handle errors
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

expression = ""
input_text = StringVar()

# Input Frame
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Button Frame
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()

# Styling for the buttons (Colors, Font)
btn_params = {
    'width': 10,
    'height': 3,
    'bd': 0,
    'fg': 'black',
    'bg': '#fff',
    'cursor': 'hand2',
    'font': ('arial', 12, 'bold')
}

# Update the button creation process with **btn_params to apply the styling
clear  = Button(btns_frame, text="C", **btn_params, command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", **btn_params, command=lambda: btn_click('/')).grid(row=0, column=3, padx=1, pady=1)

# Defining button for each row
buttons = [
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '+']
]

# Row configuration for button layout
for i, row in enumerate(buttons):
    for j, item in enumerate(row):
        if item == '=':  # Special case for equal button
            Button(btns_frame, text=item, **btn_params, command=lambda: bt_equal()).grid(row=i+1, column=j, padx=1, pady=1)
        elif item == '0':  # Special case for zero button to occupy two columns
            Button(btns_frame, text=item, **btn_params, command=lambda item=item: btn_click(item)).grid(row=i+1, column=j, columnspan=2, padx=1, pady=1)
        else:
            Button(btns_frame, text=item, **btn_params, command=lambda item=item: btn_click(item)).grid(row=i+1, column=j, padx=1, pady=1)

win.mainloop()
