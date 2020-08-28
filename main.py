from tkinter import *

root =Tk()
root.title('calculator')
MAIN_WIN_XPOS = 50
MAIN_WIN_YPOS = 50
MAIN_WIN_WIDTH = 392
MAIN_WIN_HEIGHT = 325

root.geometry("{}x{}+{}+{}".format(
    MAIN_WIN_WIDTH, MAIN_WIN_HEIGHT, MAIN_WIN_XPOS, MAIN_WIN_YPOS))
root.resizable(height=False,width=False)


# functions

def seven():
    t.configure(state='normal')
    t.insert(END,7)
    t.configure(state="disabled")

def eight():
    t.configure(state='normal')
    t.insert(END,8)
    t.configure(state="disabled")

def nine():
    t.configure(state='normal')
    t.insert(END,9)
    t.configure(state="disabled")

def four():
    t.configure(state='normal')
    t.insert(END,4)
    t.configure(state="disabled")

def five():
    t.configure(state='normal')
    t.insert(END,5)
    t.configure(state="disabled")

def six():
    t.configure(state='normal')
    t.insert(END,6)
    t.configure(state="disabled")

def one():
    t.configure(state='normal')
    t.insert(END,1)
    t.configure(state="disabled")

def two():
    t.configure(state='normal')
    t.insert(END,2)
    t.configure(state="disabled")

def three():
    t.configure(state='normal')
    t.insert(END,3)
    t.configure(state="disabled")

def zero():
    t.configure(state='normal')
    value = t.get("1.0","end-1c")
    if str(value) != '0':
        t.insert(END,0)
        t.configure(state="disabled")
    else:
        pass

def dot():
    t.configure(state='normal')
    value = t.get("1.0","end-1c")
    if str(value[-1]) not in signs :
        t.insert(END,'.')
        t.configure(state="disabled")
    else:
        pass

def sum():
    t.configure(state='normal')
    value = t.get("1.0","end-1c")
    if str(value[-1]) not in signs :
        t.insert(END,'+')
        t.configure(state="disabled")
    else:
        pass

def times():
    t.configure(state='normal')
    value = t.get("1.0","end-1c")
    if str(value[-1]) not in signs :
        t.insert(END,'*')
        t.configure(state="disabled")
    else:
        pass

def divide():
    t.configure(state='normal')
    value = t.get("1.0","end-1c")
    if str(value[-1]) not in signs :
        t.insert(END,'/')
        t.configure(state="disabled")
    else:
        pass

def diff():
    t.configure(state='normal')
    value = t.get("1.0","end-1c")
    if str(value[-1]) not in signs :
        t.insert(END,'-')
        t.configure(state="disabled")
    else:
        pass

def percent():
    t.configure(state='normal')
    value = t.get("1.0","end-1c")
    if str(value[-1]) not in signs :
        t.insert(END,'%')
        t.configure(state="disabled")
    else:
        pass

def open_paren():
    t.configure(state='normal')
    value = t.get("1.0","end-1c")
    if str(value) != '0':
        t.insert(END,'(')
        t.configure(state="disabled")
    else:
        pass


def close_paren():
    t.configure(state='normal')
    value = t.get("1.0","end-1c")
    if str(value) != '0':
        t.insert(END,')')
        t.configure(state="disabled")
    else:
        pass

def back():
    t.configure(state='normal')
    temp = t.get('1.0','end-1c')
    t.delete(1.0,END)
    t.insert(END,temp[:-1])
    t.configure(state="disabled")

def equal():
    t.configure(state='normal')
    try:
        expression = t.get('1.0','end-1c')
        total = str(eval(expression))
        t.delete(1.0,END)
        t.insert(END,total)
        t.configure(state="disabled")
    except:
        t.delete(1.0,END)
        t.insert(END,'ERROR')
        t.configure(state="disabled")

def clear():
    t.configure(state='normal')
    t.delete(1.0, END)
    t.configure(state="disabled")
    
signs = ['%','.','+','-','/','*']

#  left side

Button(root,command=seven,text='7',font=('arial 15'),height=2,width=5).place(x=0,y=65)
Button(root,command=eight,text='8',font=('arial 15'),height=2,width=5).place(x=65,y=65)
Button(root,command=nine,text='9',font=('arial 15'),height=2,width=5).place(x=130,y=65)
Button(root,command=four,text='4',font=('arial 15'),height=2,width=5).place(x=0,y=130)
Button(root,command=five,text='5',font=('arial 15'),height=2,width=5).place(x=65,y=130)
Button(root,command=six,text='6',font=('arial 15'),height=2,width=5).place(x=130,y=130)
Button(root,command=one,text='1',font=('arial 15'),height=2,width=5).place(x=0,y=195)
Button(root,command=two,text='2',font=('arial 15'),height=2,width=5).place(x=65,y=195)
Button(root,command=three,text='3',font=('arial 15'),height=2,width=5).place(x=130,y=195)
Button(root,command=zero,text='0',font=('arial 15'),height=2,width=11).place(x=0,y=260)
Button(root,command=dot,text='.',font=('arial 15'),height=2,width=5).place(x=130,y=260)

# right side
Button(root,command=sum,text='+',font=('arial 15'),height=5,width=5).place(x=195,y=61)
Button(root,command=times,text='x',font=('arial 15'),height=2,width=5).place(x=195,y=195)
Button(root,command=percent,text='%',font=('arial 15'),height=2,width=5).place(x=195,y=260)
Button(root,command=back,text='<==',font=('arial 15'),height=2,width=5).place(x=260,y=65)
Button(root,command=diff,text='-',font=('arial 15'),height=2,width=5).place(x=260,y=130)
Button(root,command=divide,text='/',font=('arial 15'),height=2,width=5).place(x=260,y=195)
Button(root,command=equal,text='=',font=('arial 15'),height=2,width=5).place(x=260,y=260)
Button(root,command=open_paren,text='(',font=('arial 15'),height=2,width=5).place(x=325,y=65)
Button(root,command=close_paren,text=')',font=('arial 15'),height=2,width=5).place(x=325,y=130)
Button(root,command=clear,text='CE',font=('arial 15'),height=5,width=5).place(x=325,y=195)

# display pannel

t=Text(root,height=2,width=100,font=('arial 20'))
t.insert(END,'')
t.configure(state="disabled")
t.place(x=0,y=0)
main_value = t.get('1.0','end-1c')


root.mainloop()

