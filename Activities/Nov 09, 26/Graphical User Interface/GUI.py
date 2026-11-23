from tkinter import * 
root = Tk()
root.title('Tkinter_Program')
root.geometry('400x400')
root.config(bg='#234567')

def add():
    v1=int(e1.get())
    v2=int(e2.get())
    result = v1+v2
    l2.configure(text = f"Sum of two numbers is: {result}")


def sub():
    v1=int(e1.get())
    v2=int(e2.get())
    result = v1-v2
    l2.configure(text = f"Subtraction of two numbers is: {result}")

l1 = Label(root, text = "Enter Values",
bg='#234567',fg="white",font=("tahoma",12))
l1.place(x=10, y=20)

e1 = Entry(root,font=("tahoma",12))
e1.place(x=10, y=60)
e2 = Entry(root,font=("tahoma",12))
e2.place(x=200, y=60)

l2 = Label(root, text = "",
bg='#234567',fg="white",font=("tahoma",12))
l2.place(x=10, y=200)

b1 = Button(root, text = "Sum", fg="yellow", bg="#001111"
,font=("tahoma",12), command = add)
b1.place(x=60,y=100)

b2 = Button(root, text = "Sub", fg="yellow", bg="#001111"
,font=("tahoma",12), command = sub)
b2.place(x=200,y=100)

root.mainloop()