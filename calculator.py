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
input_field.grid(row=0
