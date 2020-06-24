from tkinter import *
import math
hi
root = Tk()
root.title("Scientific Calculator")

# Place where you enter number
number_entry = Entry(root, width=24, borderwidth=10, font=("Times New Roman", 40))
number_entry.grid(row=0, column=0, columnspan=7)


def add():
 first_number = number_entry.get()
 global fnum
 fnum = float(first_number)
 global math1
 math1 = "Addition"
 number_entry.delete(0, END)


def subtract():
 first_number = number_entry.get()
 global fnum
 fnum = float(first_number)
 global math1
 math1 = "Subtraction"
 number_entry.delete(0, END)


def multiply():
 first_number = number_entry.get()
 global fnum
 fnum = float(first_number)
 global math1
 math1 = "Multiply"
 number_entry.delete(0, END)


def divide():
 first_number = number_entry.get()
 global fnum
 fnum = float(first_number)
 global math1
 math1 = "Division"
 number_entry.delete(0, END)


# If clicked
def click(n):
 before = number_entry.get()
 number_entry.delete(0, END)
 number_entry.insert(0, str(before) + str(n))


def special(n):
 global math1

 if n == 1:
     before = number_entry.get()
     number_entry.delete(0, END)
     number_entry.insert(0, str(before) + "(")

 elif n == 2:
     before = number_entry.get()
     number_entry.delete(0, END)
     number_entry.insert(0, str(before) + ")")

 elif n == 3:
     before = number_entry.get()
     number_entry.delete(0, END)
     number_entry.insert(0, str(before) + "%")

 elif n == 4:
     before = number_entry.get()
     number_entry.delete(0, END)
     number_entry.insert(0, str(before) + ".")
     equal()

 elif n == 5:
     before = number_entry.get()
     number_entry.delete(0, END)
     number_entry.insert(0, str(before) + "3.1415926589793")

 elif n == 6:
     before = number_entry.get()
     number_entry.delete(0, END)
     number_entry.insert(0, str(before) + "2.718281828459045")


def fact():
 global math1
 global before
 before = number_entry.get()
 number_entry.delete(0, END)
 number_entry.insert(0, str(before) + "!")
 math1 = "factorial"
 equal()


def sqrt():
 global math1
 before = number_entry.get()
 number_entry.delete(0, END)
 number_entry.insert(0, str(before) + "√")
 math1 = "sqrt"
 equal()


def equal():
 global math1
 global fnum
 global before
 global method

 if math1 == "Addition":
     second_number = number_entry.get()
     snum = float(second_number)
     sum = fnum + snum
     number_entry.delete(0, END)
     number_entry.insert(0, str(sum))

 elif math1 == "Subtraction":
     second_number = number_entry.get()
     snum = float(second_number)
     difference = fnum - snum
     number_entry.delete(0, END)
     number_entry.insert(0, str(difference))

 elif math1 == "Multiply":
     second_number = number_entry.get()
     snum = float(second_number)
     product = fnum * snum
     number_entry.delete(0, END)
     number_entry.insert(0, str(product))

 elif math1 == "Division":
     second_number = number_entry.get()
     snum = float(second_number)
     quotient = fnum / snum
     number_entry.delete(0, END)
     number_entry.insert(0, str(quotient))

 elif math1 == "factorial":
     before1 = int(before)
     print(before1)

     def the_real_factorial(n):
         if n == 1:
             return 1
         elif n == 0:
             return 0
         else:
             return n * the_real_factorial(n - 1)

     number_entry.delete(0, END)
     number_entry.insert(0, str(the_real_factorial(before1)))

 elif math1 == "sqrt":
     after = number_entry.get()
     number = after.split("√")
     number_we_actually_want = number[1]
     result = math.sqrt(float(number_we_actually_want))
     print(number_we_actually_want)
     number_entry.delete(0, END)
     number_entry.insert(0, str(result))

 elif math1 == "square":
     after = number_entry.get()
     number = after.split("^2")
     number_we_actually_want = number[0]
     result = float(number_we_actually_want) ** 2
     print(number_we_actually_want)
     number_entry.delete(0, END)
     number_entry.insert(0, str(result))


 elif math1 == "sine":
     if method == "deg":
         before = number_entry.get()
         number1 = before.split("sin(")
         sine1 = number1[1]
         result1 = math.sin(float(sine1) * math.pi / 180)
         print(result1)
         number_entry.delete(0, END)
         number_entry.insert(0, str(result1))

     elif method == "rad":
         before = number_entry.get()
         number1 = before.split("sin(")
         sine1 = number1[1]
         result1 = math.sin(float(sine1))
         print(result1)
         number_entry.delete(0, END)
         number_entry.insert(0, str(result1))

 elif math1 == "cosine":
     if method == "deg":
         before = number_entry.get()
         number1 = before.split("cos(")
         cosine1 = number1[1]
         result1 = math.cos(float(cosine1) * math.pi / 180)
         print(result1)
         number_entry.delete(0, END)
         number_entry.insert(0, str(result1))

     elif method == "rad":
         before = number_entry.get()
         number1 = before.split("cos(")
         cosine1 = number1[1]
         result1 = math.cos(float(cosine1))
         print(result1)
         number_entry.delete(0, END)
         number_entry.insert(0, str(result1))


 elif math1 == "tangent":
     if method == "deg":
         before = number_entry.get()
         number1 = before.split("tan(")
         tangent1 = number1[1]
         result1 = math.tan(float(tangent1) * math.pi / 180)
         print(result1)
         number_entry.delete(0, END)
         number_entry.insert(0, str(result1))

     elif method == "rad":
         before = number_entry.get()
         number1 = before.split("tan(")
         tangent1 = number1[1]
         result1 = math.tan(float(tangent1))
         print(result1)
         number_entry.delete(0, END)
         number_entry.insert(0, str(result1))

 elif math1 == "ln":
     before = number_entry.get()
     number1 = before.split("ln(")
     ln1 = number1[1]
     result1 = math.log(float(ln1))
     print(result1)
     number_entry.delete(0, END)
     number_entry.insert(0, str(result1))

 elif math1 == "logarithm":
     before = number_entry.get()
     number1 = before.split("log(")
     log1 = number1[1]
     result1 = math.log10(float(log1))
     print(result1)
     number_entry.delete(0, END)
     number_entry.insert(0, str(result1))

 elif math1 == "power":
     before = number_entry.get()
     number1 = before.split("^")
     pow1 = number1[1]
     result1 = float(number1[0]) ** float(pow1)
     print(result1)
     number_entry.delete(0, END)
     number_entry.insert(0, str(result1))


def clear():
 number_entry.delete(0, END)


def rad():
 global method
 button_rad["bg"] = "yellow"
 button_deg["bg"] ="#dbdbdb"
 method = "rad"
 equal()


def deg():
 global method
 button_deg["bg"] = "yellow"
 button_rad["bg"] ="#dbdbdb"
 method = "deg"
 equal()


def inv():
 return


def sine():
 global math1
 before = number_entry.get()
 number_entry.delete(0, END)
 number_entry.insert(0, str(before) + "sin(")
 math1 = "sine"
 equal()


def cosine():
 global math1
 before = number_entry.get()
 number_entry.delete(0, END)
 number_entry.insert(0, str(before) + "cos(")
 math1 = "cosine"
 equal()


def tangent():
 global math1
 before = number_entry.get()
 number_entry.delete(0, END)
 number_entry.insert(0, str(before) + "tan(")
 math1 = "tangent"
 equal()


def ln():
 global math1
 before = number_entry.get()
 number_entry.delete(0, END)
 number_entry.insert(0, str(before) + "ln(")
 math1 = "ln"
 equal()


def logarithm():
 global math1
 before = number_entry.get()
 number_entry.delete(0, END)
 number_entry.insert(0, str(before) + "log(")
 math1 = "logarithm"
 equal()


def answer():
 return


def square():
 global math1
 before = number_entry.get()
 number_entry.delete(0, END)
 number_entry.insert(0, str(before) + "^2")
 math1 = "square"
 equal()


def power():
 global math1
 before = number_entry.get()
 number_entry.delete(0, END)
 number_entry.insert(0, str(before) + "^")
 math1 = "power"
 equal()


# Defining all the buttons
button_pths1 = Button(root, text="(", width=12, command=lambda: special(1), bg="#dbdbdb", fg="black")
button_pths2 = Button(root, text=")", width=12, command=lambda: special(2), bg="#dbdbdb", fg="black")
button_percent = Button(root, text="%", width=12, command=lambda: special(3), bg="#dbdbdb", fg="black")

button_1 = Button(root, text="1", width=12, command=lambda: click(1), fg="black", bg="white")
button_2 = Button(root, text="2", width=12, command=lambda: click(2), fg="black", bg="white")
button_3 = Button(root, text="3", width=12, command=lambda: click(3), fg="black", bg="white")
button_4 = Button(root, text="4", width=12, command=lambda: click(4), fg="black", bg="white")
button_5 = Button(root, text="5", width=12, command=lambda: click(5), fg="black", bg="white")
button_6 = Button(root, text="6", width=12, command=lambda: click(6), fg="black", bg="white")
button_7 = Button(root, text="7", width=12, command=lambda: click(7), fg="black", bg="white")
button_8 = Button(root, text="8", width=12, command=lambda: click(8), fg="black", bg="white")
button_9 = Button(root, text="9", width=12, command=lambda: click(9), fg="black", bg="white")

button_0 = Button(root, text="0", width=12, command=lambda: click(0), fg="black", bg="white")
button_subtract = Button(root, text="-", width=12, command=subtract, bg="#dbdbdb", fg="black")
button_add = Button(root, text="+", width=12, command=add, bg="#dbdbdb", fg="black")

button_AC = Button(root, text="AC", width=12, command=clear, bg="#dbdbdb", fg="black")
button_divide = Button(root, text="÷", width=12, command=divide, bg="#dbdbdb", fg="black")
button_multiply = Button(root, text="⨉", width=12, command=multiply, bg="#dbdbdb", fg="black")

button_equal = Button(root, text="=", width=12, command=equal, fg="white", bg="blue")
button_point = Button(root, text=".", width=12, command=lambda: special(4), fg="black", bg="white")

# Defining of scientific stuff
button_rad = Button(root, text="Rad", width=12, command=rad, bg="#dbdbdb", fg="black")
button_deg = Button(root, text="Deg", width=12, command=deg, bg="#dbdbdb", fg="black")
button_fact = Button(root, text="x!", width=12, command=fact, bg="#dbdbdb", fg="black")

button_inv = Button(root, text="Inv", width=12, command=inv, bg="#dbdbdb", fg="black")
button_sin = Button(root, text="sin", width=12, command=sine, bg="#dbdbdb", fg="black")
button_ln = Button(root, text="ln", width=12, command=ln, bg="#dbdbdb", fg="black")

button_pi = Button(root, text="π", width=12, command=lambda: special(5), bg="#dbdbdb", fg="black")
button_cos = Button(root, text="cos", width=12, command=cosine, bg="#dbdbdb", fg="black")
button_log = Button(root, text="log", width=12, command=logarithm, bg="#dbdbdb", fg="black")

button_e = Button(root, text="e", width=12, command=lambda: special(6), bg="#dbdbdb", fg="black")
button_tan = Button(root, text="tan", width=12, command=tangent, bg="#dbdbdb", fg="black")
button_sqrt = Button(root, text="√", width=12, command=sqrt, bg="#dbdbdb", fg="black")

button_ans = Button(root, text="Ans", width=12, command=answer, bg="#dbdbdb", fg="black")
button_square = Button(root, text="x^2 ", width=12, command=square, bg="#dbdbdb", fg="black")
button_power = Button(root, text="x^y ", width=12, command=power, bg="#dbdbdb", fg="black")

# Where the buttons are placed
button_pths1.grid(row=1, column=3)
button_pths2.grid(row=1, column=4)
button_percent.grid(row=1, column=5)

button_7.grid(row=2, column=3)
button_8.grid(row=2, column=4)
button_9.grid(row=2, column=5)

button_4.grid(row=3, column=3)
button_5.grid(row=3, column=4)
button_6.grid(row=3, column=5)

button_1.grid(row=4, column=3)
button_2.grid(row=4, column=4)
button_3.grid(row=4, column=5)

button_0.grid(row=5, column=3)
button_point.grid(row=5, column=4)
button_equal.grid(row=5, column=5)

button_AC.grid(row=1, column=6)
button_divide.grid(row=2, column=6)
button_multiply.grid(row=3, column=6)
button_subtract.grid(row=4, column=6)
button_add.grid(row=5, column=6)

# Grid of Scientific stuff
button_rad.grid(row=1, column=0)
button_deg.grid(row=1, column=1)
button_fact.grid(row=1, column=2)

button_inv.grid(row=2, column=0)
button_sin.grid(row=2, column=1)
button_ln.grid(row=2, column=2)

button_pi.grid(row=3, column=0)
button_cos.grid(row=3, column=1)
button_log.grid(row=3, column=2)

button_e.grid(row=4, column=0)
button_tan.grid(row=4, column=1)
button_sqrt.grid(row=4, column=2)

button_ans.grid(row=5, column=0)
button_square.grid(row=5, column=1)
button_power.grid(row=5, column=2)

root.mainloop()


