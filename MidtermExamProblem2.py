from tkinter import *

class Name:
    def __init__(self,Name):
        self.fn = Label(Name, text="My Full Name")
        self.fn.place(x=250, y=50)
        self.fn = Label(Name, text="Enter Given Name:")
        self.fn.place(x=100, y=100)
        self.mn = Label(Name, text="Enter Middle Name:")
        self.mn.place(x=100, y=150)
        self.ln = Label(Name, text="Enter Last Name:")
        self.ln.place(x=100, y=200)
        self.rslt = Label(Name, text="My full name is:")
        self.rslt.place(x=100, y=250)
        self.txt1 = Entry(Name,bd=1)
        self.txt1.place(x=360,y=100)
        self.txt2 = Entry(Name,bd=1)
        self.txt2.place(x=360,y=150)
        self.txt3 = Entry(Name,bd=3)
        self.txt3.place(x=360,y=200)
        self.txt4 = Entry(Name,bd=3)
        self.txt4.place(x=360,y=250)
        self.btnadd = Button(Name,text="Show Full Name")
        self.btnadd.place(x=250,y=280)
        self.btnadd.bind('<Button-1>',self.FullName)

    def FullName(self,Full):
        self.txt4.delete(0, 'end')
        n1 = self.txt1.get()
        n2 = self.txt2.get()
        n3 = self.txt3.get()
        result = f"{n1} {n2} {n3}"
        self.txt4.insert(END, result)

window = Tk()
name = Name(window)
window.geometry("600x400+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()