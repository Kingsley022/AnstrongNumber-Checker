from tkinter import * 
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width=1000, height= 500)
canvas.grid(columnspan=3, rowspan=5)

#Logo
logo = Image.open('./logo2.png')
logo = logo.resize((500, 55))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


#Instruction
instruction = tk.Label(root, text='Enter a three digit number:', font=("GiddyupStd 12 bold"))
instruction.grid(columnspan=3, column=1, row=2, sticky = "WS", padx=20)

#Input Field
user_input = Entry(root, width=80, font=("Vani", 15), borderwidth=3, relief="ridge", justify="center")
user_input.grid(column=1, row=3)
# user_input.insert(0, "Enter a number less than 999 : ")

#My button function
def check():
    checker = int(user_input.get())
    unit_digit = checker % 10
    tens_digit = (checker//10) % 10
    hundred_digits = checker//100

    if unit_digit ** 3 + tens_digit ** 3 + hundred_digits ** 3 == checker:
        checkInput = Label(root, text = f"{checker} is an Armstrong Number", fg="blue", font=("Poplar Std", 12))
        checkInput.grid(column=1, row=1)

    else:
       checkInput = Label(root, text = f"{checker} is not Armstrong Number",  fg="red", font=("Poplar Std", 12))
       checkInput.grid(column=1, row=1)


#check Button
check_input = tk.StringVar()
check_btn = tk.Button(root, command=check, textvariable=check_input, bg="#00BFFF",fg="white", borderwidth=-1, relief="ridge", height=2,  width=15, font=8)
check_input.set("Check")
check_btn.grid(column=1, row=4)




root.mainloop()