from tkinter import *

window = Tk()
window.title("Calculator")
window.minsize(width=405,height=435)
window.maxsize(width=405,height=435)


def delete(val):

    if val == "backspace":
        my_text.config(state=NORMAL)
        my_text.delete("end-2c")
        my_text.config(state=DISABLED)

    else:
        my_text.config(state=NORMAL)
        my_text.delete("1.0","end")
        my_text.config(state=DISABLED)

def calculator(value):

    my_text.config(state=NORMAL)
    my_text.insert(END, value)
    my_text.config(state=DISABLED)

def calculate():

    my_text.config(state=NORMAL)
    input = my_text.get("1.0",END)
    my_text.insert(END, "\n=")
    ans = eval(input)
    my_text.insert(END,f"\n\n\n{ans}")
    my_text.config(state= DISABLED)
    



my_text = Text(window, width=49, height= 5, font=(30))
my_text.place(x= 5, y= 5)
my_text.config(state=DISABLED)

Button(window,text= "1", width=12,height=3, background="#FFFFFF", command=lambda:calculator(1)).place(x=5, y=410- 100)
Button(window,text= "2", width=12,height=3, background="#FFFFFF", command=lambda:calculator(2)).place(x=105, y=410- 100)
Button(window,text= "3", width=12,height=3, background="#FFFFFF", command=lambda:calculator(3)).place(x=205, y=410- 100)
Button(window,text= "4", width=12,height=3, background="#FFFFFF", command=lambda:calculator(4)).place(x=5, y=350- 100)
Button(window,text= "5", width=12,height=3, background="#FFFFFF", command=lambda:calculator(5)).place(x=105, y=350- 100)
Button(window,text= "6", width=12,height=3, background="#FFFFFF", command=lambda:calculator(6)).place(x=205, y=350- 100)
Button(window,text= "7", width=12,height=3, background="#FFFFFF", command=lambda:calculator(7)).place(x=5, y=290- 100)
Button(window,text= "8", width=12,height=3, background="#FFFFFF", command=lambda:calculator(8)).place(x=105, y=290- 100)
Button(window,text= "9", width=12,height=3, background="#FFFFFF", command=lambda:calculator(9)).place(x=205, y=290- 100)
Button(window,text= "0", width=26,height=3, background="#FFFFFF", command=lambda:calculator(0)).place(x=5, y=470- 100)
Button(window,text= "x", width=12,height=3, command=lambda:calculator("*")).place(x=305, y=290- 100)
Button(window,text= "-", width=12,height=3, command=lambda:calculator("-")).place(x=305, y=350- 100)
Button(window,text= "+", width=12,height=3, command=lambda:calculator("+")).place(x=305, y=410- 100)
Button(window,text= "=", width=12,height=3, background="#455AB3", command= lambda: calculate()).place(x=305, y=470- 100)
Button(window,text= "÷", width=12,height=3, command=lambda:calculator("/")).place(x=305, y=230- 100)
Button(window,text= ".", width=12,height=3, background="#FFFFFF", command=lambda:calculator(".")).place(x=205, y=470- 100)
Button(window,text= "C", width=26,height=3, command=lambda:delete("clear")).place(x=5, y=230- 100)
Button(window,text= "←", width=12,height=3, command=lambda:delete("backspace")).place(x=205, y=230- 100)

window.mainloop()