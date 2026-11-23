from tkinter import *

root = Tk()
root.config(bg="#3110B7")
root.title("Multiple Frames Example")
root.geometry("400x400")

frame2 = Frame(root, bg="#234567")
frame2.place(x=125, y=0, width=300, height=400)

label_title = Label(root, text="Click on the buttons on the left side.", font=('Roboto', 10), bg="#FFFFFF", fg="#234567")
label_title.place(x=150, y=0)

frame1 = Frame(root, bg="#16293D")
frame1.place(x=0, y=0, width=125, height=400)

homebutton = Button(frame1, text="Home", fg = "#FFFFFF", bg="#234567")
homebutton.pack(pady=5)

mainbutton = Button(frame1, text="Main", fg="#FFFFFF", bg="#234567")
mainbutton.pack(pady=5)

informationbutton = Button(frame1, text="Information", fg="#FFFFFF", bg="#234567")
informationbutton.pack(pady=5)

root.mainloop()
