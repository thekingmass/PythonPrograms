from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("240x380+800+70")

val = ""


def btnClick(number):
    global val
    val = val + str(number)
    data.set(val)


def btnClear():
    global val
    val = ""
    data.set("")


def btnEquals():
    global val
    result = eval(val)
    data.set(result)


data = StringVar()
display = Entry(root, textvariable=data, bd=20, font=("Comic Sans Ms", 12), justify="right", bg="powder blue")
display.grid(row=0, columnspan=4)

# first row of buttons
btn7 = Button(root, text="7", font=("ariel", 27, "bold"), command=lambda: btnClick(7))
btn7.grid(row=1, column=0)
btn8 = Button(root, text="8", font=("ariel", 27, "bold"), command=lambda: btnClick(8))
btn8.grid(row=1, column=1)
btn9 = Button(root, text="9", font=("ariel", 27, "bold"), command=lambda: btnClick(9))
btn9.grid(row=1, column=2)
btnadd = Button(root, text="+", font=("ariel", 27, "bold"), command=lambda: btnClick('+'))
btnadd.grid(row=1, column=3)

# second row of buttons
btn4 = Button(root, text="4", font=("ariel", 27, "bold"), command=lambda: btnClick(4))
btn4.grid(row=2, column=0)
btn5 = Button(root, text="5", font=("ariel", 27, "bold"), command=lambda: btnClick(5))
btn5.grid(row=2, column=1)
btn6 = Button(root, text="6", font=("ariel", 27, "bold"), command=lambda: btnClick(6))
btn6.grid(row=2, column=2)
btnsub = Button(root, text="-", font=("ariel", 30, "bold"), command=lambda: btnClick('-'))
btnsub.grid(row=2, column=3)

# third row of buttons
btn1 = Button(root, text="1", font=("ariel", 27, "bold"), command=lambda: btnClick(1))
btn1.grid(row=3, column=0)
btn2 = Button(root, text="2", font=("ariel", 27, "bold"), command=lambda: btnClick(2))
btn2.grid(row=3, column=1)
btn3 = Button(root, text="3", font=("ariel", 27, "bold"), command=lambda: btnClick(3))
btn3.grid(row=3, column=2)
btnmul = Button(root, text="*", font=("ariel", 30, "bold"), command=lambda: btnClick('*'))
btnmul.grid(row=3, column=3)

# fourth row of buttons
btnc = Button(root, text="C", font=("ariel", 27, "bold"), command=btnClear)
btnc.grid(row=4, column=0)
btn0 = Button(root, text="0", font=("ariel", 27, "bold"), command=lambda: btnClick(0))
btn0.grid(row=4, column=1)
btn_equal = Button(root, text="=", font=("ariel", 27, "bold"), command=btnEquals)
btn_equal.grid(row=4, column=2)
# btn_equal.bind("<Enter>", btnEquals)
btn_div = Button(root, text="/", font=("ariel", 30, "bold"), command=lambda: btnClick('/'))

btn_div.grid(row=4, column=3)

root.mainloop()
