from tkinter import*  
from tkinter import messagebox
self = Tk()  
self.geometry('500x500')  
self.title("Registration Form") 

        
myLabel = Label(self, text = "Registration Form", width=20, font=("bold", 20))
myLabel.place(x=97,y=20)
        
#fullname        
LblFullname = Label(self, text="FullName",width=20,font=("bold", 10))  
LblFullname.place(x=80,y=100) 
        
Fullname_entry = Entry(self)  
Fullname_entry.place(x=250,y=100,width=150)  
        
#password        
LblPassword = Label(self, text="Password",width=20,font=("bold", 10))  
LblPassword.place(x=80,y=150) 
        
Password_entry = Entry(self)  
Password_entry.place(x=250,y=150,width=150)  

#contact number
LblNum = Label(self, text="Contact number",width=20,font=("bold", 10))  
LblNum.place(x=95,y=200) 
        
Num_entry = Entry(self)  
Num_entry.place(x=250,y=200,width=150) 

        
#email        
LblEmail = Label(self, text="Email",width=20,font=("bold", 10))  
LblEmail.place(x=69,y=250) 
        
email_entry = Entry(self)  
email_entry.place(x=250,y=250,width=150) 

        
#gender        
LblGender = Label(self, text="Gender",width=20,font=("bold", 10))  
LblGender.place(x=72,y=300)
        
Gender = IntVar()
Radiobutton(self, text="Male",padx = 10, variable=Gender, value=1).place(x=243,y=300)
Radiobutton(self, text="Female",padx = 20, variable=Gender, value=2).place(x=300,y=300)  


#terms and condition
terms_con = Checkbutton(self, text='I agree to the ATM Machine Terms & Conditions.',font=("Bold",10))
terms_con.grid(row=8,column=1,padx=120,pady=350)

    
def Register():
    messagebox.showinfo("Registration","Successfully Registered")
    
    
#for register button
Button(self, text='Register',width=20,bg='black',fg='white', command=Register).place(x=180,y=400) 


self.mainloop()  
