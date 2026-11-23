from tkinter import *
root = Tk()

root.title('Student Information')

root.geometry('450x600')

root.resizable(0, 0)

greeting = Label(root, text="Hello! My name is", font=("Arial", 10))
greeting.pack(pady=20)


myname = Label(root, text="Josh Louis R. Contreras", font=("Arial", 20), fg="#730000")
myname.pack(pady=20)

intro1 = Label(root, text="I am studying in BathSpa University Academic center in RAK", font=("Arial", 10))
intro1.pack(pady=20)
intro2 = Label(root, text="I am enrolled in BSc CY Year 2, Group -1 and my student ID is 697714", font=("Arial", 10))
intro2.pack(pady=20)

mybutton = Button(root, text="I am a Button", font=("Arial", 10), fg="#730000", command=lambda: print("I am a Button"))
mybutton.pack(pady=20)

C1 = Checkbutton(root, text="Gaming")
C1.pack(pady=20)

intro2 = Label(root, text="I am enrolled in BSc CY Year 2, Group -1 and my student ID is 697714", font=("Arial", 10))
intro2.pack(pady=20)

root.mainloop()