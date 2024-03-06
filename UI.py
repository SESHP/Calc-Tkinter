from tkinter import *

num = []
all_operant = []
def labeles(label, num):
    label.config(text = ''.join(num))
    
def number1():
    num.append('1')
    labeles(label, num)

def number2():
    num.append('2')
    labeles(label, num)
    print(num)

def number3():
    num.append('3')
    labeles(label, num)
    print(num)

def number4():
    num.append('4')
    labeles(label, num)
    print(num)

def number5():
    num.append('5')
    labeles(label, num)
    print(num)

def number6():
    num.append('6')
    labeles(label, num)
    print(num)

def number7():
    num.append('7')
    labeles(label, num)
    print(num)

def number8():
    num.append('8')
    labeles(label, num)
    print(num)

def number9():
    num.append('9')
    labeles(label, num)
    print(num)

def number0():
    num.append('0')
    labeles(label, num)
    print(num)

def sqrt():
    num.insert(0, '√')
    labeles(label, num)
    print(num)

def summa():
    num.append('+')
    labeles(label, num)
    print(num)

def minus():
    num.append('-')
    labeles(label, num)
    print(num)

def proizv():
    num.append('*')
    labeles(label, num)
    print(num)

def delen():
    num.append('/')
    labeles(label, num)
    print(num)

def V():
    num.append('^')
    labeles(label, num)
    print(num)

def Tochka():
    num.append('.')
    labeles(label, num)
    print(num)

def Sbros():
    num.clear()
    label1.config(text = '')
    labeles(label, num)
    
    print(num)

def Factorial():
    num.insert(0, '!')
    labeles(label, num)
    print(num)

def Last():
    num.clear()
    try:
        label.config(text = all_operant[-1])
        num.append(str(all_operant[-1]))
    except IndexError:
        label.config(text = 'Last not found')

def Ravno():

    if '+' in num:
        x = ''.join(num)
        x = x.split('+')
        summa = float(x[0]) + float(x[1])
        label1.config(text = summa)

        all_operant.append(summa)

    if '-' in num:
        x = ''.join(num)
        x = x.split('-')
        minus = float(x[0]) - float(x[1])
        label1.config(text = minus)

        all_operant.append(minus)

    if '*' in num:
        x = ''.join(num)
        x = x.split('*')
        proiz = float(x[0]) * float(x[1])
        label1.config(text = proiz)

        all_operant.append(proiz)

    if '/' in num:
        x = ''.join(num)
        x = x.split('/')
        delen = float(x[0]) / float(x[1])
        label1.config(text = delen)
    
        all_operant.append(delen)

    if '^' in num:
        x = ''.join(num)
        x = x.split('^')
        V = float(x[0]) ** float(x[1])
        label1.config(text = V)

        all_operant.append(V)

    if '√' in num:
        x = ''.join(num)
        x = x.split('√')
        sqrt = float(x[1]) ** (1/2)
        label1.config(text = sqrt)
        
        all_operant.append(sqrt)

    if '!' in num:
        x = ''.join(num)
        x = x.split('!')
        Factorial = 1
        for i in range(1, int(x[1]) + 1):
            Factorial *= i
        label1.config(text = Factorial)

        all_operant.append(Factorial)


root = Tk()

root.title("Калькулятор")
root.resizable(True, False)
root.geometry("380x290")

label = Label(root, font = 'Trebuchet 18', height='6', anchor='center')
label.grid(row=0, column=0, columnspan=7)

label1 = Label(root, font = 'Trebuchet 15', height='2', anchor='center')
label1.grid(row=5, column=0, columnspan=7)

button0 = Button(root, text='0', width = 5, command=number0)
button0.grid(row=4, column = 0)

button1 = Button(root, text='1', width = 5, command=number1)
button1.grid(row=1, column=0)

button2 = Button(root, text='2', width = 5, command=number2)
button2.grid(row=1, column = 1)

button3 = Button(root, text='3', width = 5, command=number3)
button3.grid(row=1, column = 2)

button4 = Button(root, text='4', width = 5, command=number4)
button4.grid(row=2, column = 0)

button5 = Button(root, text='5', width = 5, command=number5)
button5.grid(row=2, column = 1)

button6 = Button(root, text='6', width = 5, command=number6)
button6.grid(row=2, column = 2)

button7 = Button(root, text='7', width = 5, command=number7)
button7.grid(row=3, column = 0)

button8 = Button(root, text='8', width = 5, command=number8)
button8.grid(row=3, column = 1)

button9 = Button(root, text='9', width = 5, command=number9)
button9.grid(row=3, column = 2)

buttonPlus = Button(root, text='+', width =1, command=summa)
buttonPlus.grid(row=2, column = 5)

buttonMinus = Button(root, text='-', width =1, command= minus)
buttonMinus.grid(row=2, column = 6)

buttonProiz = Button(root, text='*', width =1, command= proizv)
buttonProiz.grid(row=3, column = 6)

buttonDelen = Button(root, text='/', width =1, command=delen)
buttonDelen.grid(row=3, column = 5)

buttonSqrt = Button(root, text='√', width =1, command= sqrt)
buttonSqrt.grid(row=2, column = 4)

buttonV= Button(root, text='^', width =1, command=V)
buttonV.grid(row=3, column = 4)

buttonSbros = Button(root, text='C', width =1, command=Sbros)
buttonSbros.grid(row=1, column = 4)

buttonTochka = Button(root, text='.', width = 5, command=Tochka)
buttonTochka.grid(row=4, column = 1)

buttonFactorial = Button(root, text='Factorial', width = 5, command=Factorial)
buttonFactorial.grid(row=4, column = 2)

buttonLast = Button(root, text='      Last      ', width = 5, command=Last)
buttonLast.grid(row=4, column = 3, columnspan=4)

buttonRavno = Button(root, text='=', width = 6, command=Ravno)
buttonRavno.grid(row=1, column = 5, columnspan=2)


root.mainloop()