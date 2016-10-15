import tkinter as tk
root=tk.Tk()
equa=""
equation= tk.StringVar()

calculate=tk.Label(root,textvariable=equation)
equation.set('23+54')

calculate.grid(columnspan=4)
def btnpress(num):
    global equa
    if num == '=':
        x=str(eval(equa))
        print (x)
        equation.set(x)
        equa = x
        
    elif num == 'ce':
        equa=""
        equation.set(equa)
    else:    
        
        equa = equa+ str(num)
        equation.set(equa)
    
   
button1=tk.Button(root,text='0',command=lambda:btnpress(0))
button1.grid(row=1,column=0)
button2=tk.Button(root,text='1',command=lambda:btnpress(1))
button2.grid(row=1,column=1)
button3=tk.Button(root,text='2',command=lambda:btnpress(2))
button3.grid(row=1,column=2)
button4=tk.Button(root,text='3',command=lambda:btnpress(3))
button4.grid(row=2,column=0)
button5=tk.Button(root,text='4',command=lambda:btnpress(4))
button5.grid(row=2,column=1)
button6=tk.Button(root,text='5',command=lambda:btnpress(5))
button6.grid(row=2,column=2)
button7=tk.Button(root,text='6',command=lambda:btnpress(6))
button7.grid(row=3,column=0)
button8=tk.Button(root,text='7',command=lambda:btnpress(7))
button8.grid(row=3,column=1)
button9=tk.Button(root,text='8',command=lambda:btnpress(8))
button9.grid(row=3,column=2)
button10=tk.Button(root,text='9',command=lambda:btnpress(9))
button10.grid(row=4,column=1)
plus=tk.Button(root,text='+',command=lambda:btnpress("+"))
plus.grid(row=1,column=3)
subtract=tk.Button(root,text='-',command=lambda:btnpress('-'))
subtract.grid(row=2,column=3)
div=tk.Button(root,text='/',command=lambda:btnpress('/'))
div.grid(row=3,column=3)
multiply=tk.Button(root,text='x',command=lambda:btnpress('*'))
multiply.grid(row=4,column=3)
equal=tk.Button(root,text='=',command=lambda:btnpress('='))
equal.grid(row=4,column=0)
ce=tk.Button(root,text='CE',command=lambda:btnpress('ce'))
ce.grid(row=4,column=2)





root.mainloop
