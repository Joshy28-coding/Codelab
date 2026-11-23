from tkinter import *
from pathlib import Path
from PIL import ImageTk, Image 
root = Tk()

root.title("Graphic User Interface (GUI)")
root.geometry("400x400")
root['bg'] = 'grey'

label1 = Label(root, bg='red')
label2 = Label(root, bg='green')
label3 = Label(root, bg='blue')

# Absolute positioning

label1.place(x = 10, y = 20)
label2.place(x = 20, y = 40)
label3.place(x = 40, y = 60)

image = Image.open(Path(__file__).with_name("Godzilla 2014 transparent.png"))
image.thumbnail((360, 320))
img = ImageTk.PhotoImage(image, master=root)
image_label = Label(root, image=img)
image_label.place(x=80, y=70)

root.mainloop()