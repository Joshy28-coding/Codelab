# Import Module
from tkinter import *
from PIL import ImageTk, Image

main = Tk()
main.title("Student Management System")
main.geometry("350x600")
main.resizable(0, 0)

img = ImageTk.PhotoImage(Image.open("Codelab\Activities\BathSpa.png"))
imgLabel = Label(main, image=img)

imgLabel.place(x=0, y=0)

main.mainloop()
