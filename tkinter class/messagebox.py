from tkinter import *
from tkinter import messagebox



root = Tk()

def popup():
    response = messagebox.askyesno("this is my popup","hello world")

    if response == 1:
        Label(root,text="clicked yes").pack()
    else:
        Label(root,text="clicked NO").pack()


Button(root,text="popup",command=popup).pack()


root.mainloop()

