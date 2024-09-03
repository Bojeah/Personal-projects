from tkinter import *
import string
from random import choice
from tkinter import messagebox as msg


uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
numbers = list(string.digits)
punctuations = list(string.punctuation)
punctuations.remove("\\")





def button_pressed():
    characters = [lowercase,uppercase,numbers,punctuations]
    selected_chars = []
    

    password_box.config(state= NORMAL)
    password_box.delete("1.0", "end")
    pass_len = password_length.get()
    
    lower_select= lower_value.get()
    upper_select= upper_value.get()
    number_select= numbers_value.get()
    punctuation_select= punctuation_value.get()
    
    checked = [lower_select,upper_select,number_select,punctuation_select]

    try:
        for check in range(0,4):
            if checked[check] == 1:
                for i in characters[check]:
                    selected_chars.append(i)

        password = []

        for i in range(pass_len):
            password.append(choice(selected_chars))
            
        password_box.insert(END, password)
        password_box.config(state=DISABLED)

    except:
        msg.showerror("Error", "Select atleast one element to be in your password")
    


root = Tk()
root.minsize(height=500,width= 600)
root.title("Random Password Generator")

head_font = ("times", 32, "bold italic")
body_font = ("helvetica", 16)

Label(root, text= "Random Password Generator", font= head_font).place(x=40,y=0)
Label(root, text= "Create strong and secure passwords to keep your account safe online.", font= body_font).place(x=0,y=50)


lower_value = IntVar()
upper_value = IntVar()
numbers_value = IntVar()
punctuation_value = IntVar()

Label(root, text= "Password:", font= ("calibri", 15, "bold")).place(x=100,y=100)
password_box = Text(root,font= ("calibri", 15, "bold"),width=30, height=1,background="#F0F0F0",borderwidth=0,state=DISABLED)
password_box.place(x=200,y=102)

Label(root, text="Please use slider to signify your desired password length").place(x=150,y=150)
password_length = Scale(root, from_=1, to=15, orient=HORIZONTAL)
password_length.place(x=250,y=175)

Label(root,text="Choose which elements you would like to be in your password").place(x=150,y=225)
lower_cb =Checkbutton(root,text="abc",offvalue=0,onvalue=1, variable=lower_value)
lower_cb.place(x=200,y=250)


upper_cb =Checkbutton(root,text="ABC",offvalue=0,onvalue=1, variable=upper_value)
upper_cb.place(x=250,y=250)

numbers_cb =Checkbutton(root,text="123",offvalue=0,onvalue=1, variable=numbers_value)
numbers_cb.place(x=300,y=250)

punctuations_cb = Checkbutton(root,text="!@#",offvalue=0,onvalue=1, variable=punctuation_value)
punctuations_cb.place(x=350,y=250)

Button(root,bg="#52C26E",width=25,height=3,text= "Generate",command= lambda:button_pressed()).place(x=205,y=300)



root.mainloop()
