from tkinter import *
main = Tk()

main.title('Registration Form')
main.geometry('450x600')
main.resizable(0, 0)

greeting = Label(main, text="Welcome to the Registration Form", font=("Arial", 10))
greeting.pack(pady=20)

myname = Label(main, text="Sign-up to access our services", font=("Arial", 15), fg="#730000")
myname.pack(pady=20)

intro1 = Label(main, text="Please fill out your username", font=("Arial", 10))
intro1.pack(pady=20)

username = Label(main, text="Username", font=("Arial", 20))
username.pack(pady=20)

usernameEntry =Entry(main)
usernameEntry.pack(pady=20)

intro2 = Label(main, text="Please fill out your password", font=("Arial", 10))
intro2.pack(pady=20)

password = Label(main, text="Password", font=("Arial", 20))
password.pack(pady=20)
passwordEntry = Entry(main, show="*")
passwordEntry.pack(pady=20)

mybutton = Button(main, text="Log-in", font=("Arial", 10), fg="#730000", command=lambda: print("I am a Button"))
mybutton.pack(pady=20)

R1 = Radiobutton(main, text="option 1", value=1)
R1.pack(pady=20)

R2 = Radiobutton(main, text="option 2", value=2)
R2.pack(pady=20)

R3 = Radiobutton(main, text="option 3", value=3)
R3.pack(pady=20)

main.mainloop()