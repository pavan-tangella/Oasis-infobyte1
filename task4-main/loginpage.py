from tkinter import *
from tkinter import messagebox
win=Tk()

win.geometry('500x400')
win.title('login page')
L1=Label(win,text='User id:')
L2=Label(win,text='Password')
T1=Entry(win,width=30)
T2=Entry(win,show='*',width=30)
L1.grid(row=0,column=0,pady=10,padx=5)
L2.grid(row=1,column=0,pady=10,padx=5)
T1.grid(row=0,column=1)
T2.grid(row=1,column=1)
def show():
    messagebox.showinfo('Login','Welcome to the Page')
    
B1=Button(win,text='Login',command=show)
B1.grid(row=5,column=0)

win.mainloop()
