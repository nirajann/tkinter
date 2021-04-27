from tkinter import *
from PIL import ImageTk, Image

win = Tk()

win.title('images insertion')


win.iconbitmap("calculator_31111.ico")



my_images = ImageTk.PhotoImage(Image.open("983794168.jpg"))
my_images1 = ImageTk.PhotoImage(Image.open("ON-THE-LI-RIVER-BY-TOBIAS-HAGG-1500x1000.jpeg"))
my_images2 = ImageTk.PhotoImage(Image.open("Calculator_31111.ico"))

def next():
    global my_images1
    my_label = Label(image=my_images1)



my_label = Label(image=my_images)
my_label.pack()


button_code = Button(win,text="<<", command = next, width = 20)
button_code.pack(side= LEFT)

button_code = Button(win,text=">>", command = win.quit, width = 20)
button_code.pack(side= RIGHT)

button_code = Button(win,text="Exit", command = win.quit, width = 20)
button_code.pack()




win.mainloop()






