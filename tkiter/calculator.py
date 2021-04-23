from tkinter import *


win = Tk() #to create the basic window
win.geometry("310x345")
win.title("simple calculator")



###################Starting with functions ####################
# 'btn_click' function :
# This Function continuously updates the
# input field whenever you enters a number
expression = ""
def btn_click(item):    #lambda:btn_click(item)
    global expression
    expression = expression + str(item)
    input_text.set(expression)


# 'bt_clear' function :This is used to clear
# the input field
def bt_clear():
    global expression
    expression = ""
    input_text.set("")


def bt_equal():
    global expression
    result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""


#it is used for input field
input_text = StringVar()

#creating a frame for input
input_frame = Frame(win, width=600, height=300, highlightbackground="black", highlightcolor="black",highlightthickness=1)
input_frame.pack(side=TOP)

#creating a input field inside the frame
input_field = Entry(input_frame, font=('arial', 18, 'bold'),relief=RIDGE, textvariable=input_text, width=20, bg="powder blue", bd=0,  justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady = 20,ipadx = 20)

#frame height width and colour
btns_frame = Frame(win, width=465, height=420, bg="Powder blue")
btns_frame.pack()


#first row
clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#fff", cursor="hand2",command= bt_clear).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2" ).grid(row=0, column=3, padx=1, pady=1)

#second row buttoms
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, cursor="hand2",command = lambda : btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command = lambda : btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command = lambda : btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command = lambda : btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

#third row
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, cursor="hand2",command = lambda : btn_click(4)).grid(row=4, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command = lambda : btn_click(5)).grid(row=4, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command = lambda : btn_click(6)).grid(row=4, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command = lambda : btn_click("-")).grid(row=4, column=3, padx=1, pady=1)

#fourth row
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, cursor="hand2",command = lambda : btn_click(7)).grid(row=5, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command = lambda : btn_click(8)).grid(row=5, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command = lambda : btn_click(9)).grid(row=5, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="x", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command = lambda : btn_click("x")).grid(row=5, column=3, padx=1, pady=1)

#fifth row
zero = Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command = lambda : btn_click(0)).grid(row=6, column=0, padx=1, pady=1)
dot = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command = lambda : btn_click(".")).grid(row=6, column=1, padx=1, pady=1)
equal = Button(btns_frame, text="=", fg="black", width=22, height=3, bd=0, bg="#eee", cursor="hand2",command = bt_equal).grid(row=6, column=2, columnspan=3, padx=1, pady=1)

win.mainloop()

