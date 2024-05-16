from tkinter import*
mansLogs=Tk()
mansLogs.title("Kalkulators")

def btnClick(number):
    current=e.get()#nolasa skaitli
    e.delete(0,END)#nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)#ievieto displejā
    return 0

#_____ciparu pogas_____
btn0=Button(mansLogs,text='0',padx='40',pady='20',command=lambda:btnClick(0),bg='white',font=('Arial Black',15), bd = 5)
btn1=Button(mansLogs,text='1',padx='40',pady='20',command=lambda:btnClick(1),bg='white',font=('Arial Black',15), bd = 5)
btn2=Button(mansLogs,text='2',padx='40',pady='20',command=lambda:btnClick(2),bg='white',font=('Arial Black',15), bd = 5)
btn3=Button(mansLogs,text='3',padx='40',pady='20',command=lambda:btnClick(3),bg='white',font=('Arial Black',15), bd = 5)
btn4=Button(mansLogs,text='4',padx='40',pady='20',command=lambda:btnClick(4),bg='white',font=('Arial Black',15), bd = 5)
btn5=Button(mansLogs,text='5',padx='40',pady='20',command=lambda:btnClick(5),bg='white',font=('Arial Black',15), bd = 5)
btn6=Button(mansLogs,text='6',padx='40',pady='20',command=lambda:btnClick(6),bg='white',font=('Arial Black',15), bd = 5)
btn7=Button(mansLogs,text='7',padx='40',pady='20',command=lambda:btnClick(7),bg='white',font=('Arial Black',15), bd = 5)
btn8=Button(mansLogs,text='8',padx='40',pady='20',command=lambda:btnClick(8),bg='white',font=('Arial Black',15), bd = 5)
btn9=Button(mansLogs,text='9',padx='40',pady='20',command=lambda:btnClick(9),bg='white',font=('Arial Black',15), bd = 5)

btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)

btn0.grid(row=4,column=0)

e=Entry(mansLogs,width=25,bd=10,font=("Arial Black",20),justify="right",bg='lightgrey') #displejs
e.grid(row=0,columnspan=4)

def btnCommand(command):
    global number
    global num1 #jāiegaumē skaitlis, darbība
    global mathOp#matemātiskais operators
    mathOp=command
    num1=int(e.get())
    e.delete(0,END)
    return 0

#_____darbības zīmju pogas_____
btnpluss=Button(mansLogs,text='+',padx='40',pady='20',command=lambda:btnCommand('+'),bg='lightblue',font=('Arial Black',15), bd = 5) 
btnmin=Button(mansLogs,text='-',padx='40',pady='20',command=lambda:btnCommand('-'),bg='lightblue',font=('Arial Black',15), bd = 5)
btndal=Button(mansLogs,text='/',padx='40',pady='20',command=lambda:btnCommand('/'),bg='lightblue',font=('Arial Black',15), bd = 5)
btnreiz=Button(mansLogs,text='*',padx='40',pady='20',command=lambda:btnCommand('*'),bg='lightblue',font=('Arial Black',15), bd = 5)

def Vienads():
    num2=int(e.get())
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0
btnvien=Button(mansLogs,text='=',padx='40',pady='20',command=Vienads,bg='lightblue',font=('Arial Black',15), bd = 5)

def notirit():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

btnc=Button(mansLogs,text='C',padx='40',pady='20',command=notirit,bg='lightpink',font=('Arial Black',15), bd = 5)

btnpluss.grid(row=1,column=3)
btnmin.grid(row=2,column=3)
btnreiz.grid(row=3,column=3)
btndal.grid(row=4,column=3)
btnvien.grid(row=4,column=2)
btnreiz.grid(row=3,column=3)
btnc.grid(row=4,column=1)


mansLogs.mainloop()