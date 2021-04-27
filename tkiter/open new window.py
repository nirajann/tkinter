from tkinter import *
from PIL import ImageTk, Image



root = Tk()


#Crentes new window
def open():
    global my_img
    top = Toplevel()
    top.title('Check new window')
    top.iconbitmap("calculator_31111.ico")
    my_img = ImageTk.PhotoImage(Image.open("983794168.jpg"))
    my_label = Label(top, image=my_img).pack() # closing the window using button. destroy
    btn2 = Button(top, text="Close Window", command = top.destroy).pack()

btn = Button(root, text="Open", command=open).pack()

root.mainloop()
