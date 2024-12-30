from tkinter import *
from PIL import Image, ImageTk

#Create a window with a title bar and set its geometry as well
root = Tk()
root.title('Image')
root.geometry('400x400')

#Now to Image.open() to open the pic
upload = Image.open('Water symbol.png')

#To convert the image into a Tkinter-compatible image
image = ImageTk.PhotoImage(upload)

#To add to Tk label
label = Label(root, image=image, height = 350, width = 300)
label.place(x=50, y=0)
label2 = Label(root, text="This is how run Tkinter for images")
label2.place(x=40,y=350)

#Run the app
root.mainloop()