from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title('slider')
root.iconbitmap('icon.ico')


#Verticat Slider
vertical = Scale(root, from_=0, to=200)
vertical.pack()
#Horizontal Slider
horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()
#my_label = Label(root, text=horizontal.get()).pack()
# #Function slide craeated

def slide():
     my_label = Label(root, text=horizontal.get()).pack()
     root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


#Function called
my_btn = Button(root, text="Click Me", command=slide).pack()


root.mainloop()
