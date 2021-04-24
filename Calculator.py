from tkinter import *
def buttonclick(numbers):
    global operator
    operator=operator+ str(numbers)
    input_txt.set(operator)

def buttoncleardisplay():
    global operator
    operator=""
    input_txt.set("")

def buttonequalsinput():
    global operator
    sumup=str(eval(operator))
    input_txt.set(sumup)

root= Tk()

operator=""

input_txt= StringVar()

txtdisplay= Entry(root, font=("arial", 30, "italic"), textvariable=input_txt, bd=20,
                  insertwidth= 6, fg="dark blue", justify="right").grid(columnspan=6)
#=====================================================================================================
button_seven= Button(root, font=("arial",30, "bold"), text="7", fg="black", bg="white", bd=7, padx=18,
                     command= lambda:buttonclick(7)).grid(row=1,column=0)

button_eight= Button(root, font=("arial",30, "bold"), text="8", fg="black", bg="white", bd=7, padx=18,
command = lambda:buttonclick(8)).grid(row=1,column=1)

button_nine= Button(root, font=("arial",30, "bold"), text="9", fg="black", bg="white", bd=7, padx=18,
command = lambda:buttonclick(9)).grid(row=1,column=2)
#=======================================================================================================

button_four= Button(root, font=("arial",30, "bold"), text="4", fg="black", bg="white", bd=7, padx=18,
command = lambda: buttonclick(4)).grid(row=2,column=0)


button_five= Button(root, font=("arial",30, "bold"), text="5", fg="black", bg="white", bd=7, padx=18,
command = lambda: buttonclick(5)).grid(row=2,column=1)

button_six= Button(root, font=("arial",30, "bold"), text="6", fg="black", bg="white", bd=7, padx=18,
command = lambda: buttonclick(6)).grid(row=2,column=2)
#==================================================================================================

button_one= Button(root, font=("arial",30, "bold"), text="1", fg="black", bg="white", bd=7, padx=18,
command = lambda: buttonclick(1)).grid(row=3,column=0)

button_two= Button(root, font=("arial",30, "bold"), text="2", fg="black", bg="white", bd=7, padx=18,
command = lambda: buttonclick(2)).grid(row=3,column=1)

button_three= Button(root, font=("arial",30, "bold"), text="3", fg="black", bg="white", bd=7, padx=18,
command = lambda: buttonclick(3)).grid(row=3,column=2)
#=====================================================================================================

button_add= Button(root, font=("arial",30, "bold"), text="+", fg="black", bg="white", bd=7, padx=18,
command = lambda: buttonclick("+")).grid(row=1,column=3)

button_minus= Button(root, font=("arial",30, "bold"), text="-", fg="black", bg="white", bd=7, padx=18,
command = lambda: buttonclick("-")).grid(row=2,column=3)

button_multiply= Button(root, font=("arial",30, "bold"), text="*", fg="black", bg="white", bd=7, padx=18,
command = lambda: buttonclick("*")).grid(row=3,column=3)

button_divide= Button(root, font=("arial",30, "bold"), text="/", fg="black", bg="white", bd=7, padx=18,
command = lambda: buttonclick("/")).grid(row=4,column=3)

button_clear= Button(root, font=("arial",25, "bold"), text="Clear", fg="black", bg="white", bd=6, padx=13,
                   command=lambda : buttoncleardisplay()).grid(row=4,column=0)

button_Zero= Button(root, font=("arial",30, "bold"), text="0", fg="black", bg="white", bd=7, padx=18,
                    ).grid(row=4,column=1)
#========================================================================================================

button_Equale= Button(root, font=("arial",30, "bold"), text="=", fg="black", bg="white", bd=7, padx=18,
                  command=lambda : buttonequalsinput()).grid(row=4,column=2)

root.mainloop()