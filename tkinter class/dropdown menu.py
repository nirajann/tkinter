from tkinter import *

root = Tk()
root.title('Drop down menu')
root.iconbitmap('icon.ico')


def show():
    mylabel = Label(root,text=clicked.get()).pack()

clicked = StringVar()
clicked.set("monday")

drop = OptionMenu(root, clicked,"monday","tuesday","wednesday","thursday","friday")
drop.pack()

mybutton = Button(root, text= "show selection", command=show).pack()





root.mainloop()
