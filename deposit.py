# deposit

from tkinter import *

root = Tk()
root.geometry('500x400')
root.title("ATM MACHINE")
root.configure(bg="sky blue")
amount = StringVar()

dep = StringVar()
acca = ""


def deposit():
    global acca
    amo = (amount.get())
    bal = acca + amo
    label3.config(text=(f"Current Balance: {bal}"))


    
def Exit():
    root.destroy()


lab = Label (text = "Deposit Account",font= 'arial 17', bg = "red", bd=10).pack()
lbl = Label(text = "Enter amount to deposit",font ='arial 16 bold', bg ="sky blue", anchor = 'w').place(x=148, y = 70)
text = Entry (font ='arial 16', textvariable =amount, fg = "black", bg = "white", bd=5, insertwidth=4, justify='right').place(x=150, y = 120, width=250,height=50)
label3 = Label(font ='arial 16', fg='black', bg = "sky blue")
label3.place(x = 152, y = 180)

# deposit and exit button
depbutton = Button(text = "DEPOSIT", font = 'arial 10', padx =2,bg ='limegreen' ,command = deposit).place(x=200, y = 260)
exbutton = Button(text = "CANCEL", font = 'arial 10', width = 6, command = Exit, bg = 'red').place(x=200, y = 290)


root.mainloop()