from tkinter import *



root = Tk()
#creatplg modes for radio button

MODES = [ ("Pepperoni","Pepperoni"),
          ("Cheese","Cheese"),
          ("Mushroom","Mushroom"),
          ("Onion","Onion") ]


pizza = StringVar()
pizza.set("Pepperoni")
for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


# function clicked 4
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

#myLabel = Label(root, text=pizza.get()) #myLabel.pack()

myButton = Button(root,text="Click",command=lambda :clicked(pizza.get())).pack()


root.mainloop()