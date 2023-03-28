from tkinter import *

window = Tk()

window.geometry("500x400+10+10")
window.title("My First Graphical User Interface")

txt = Entry(window, border=10)
txt.place(x=170, y=150)
btn = Button(text="Click me", fg="red", bg="yellow")
btn.place(x=210, y=200)

lbl = Label(window,text="My first Demo", font ="Verdana")
lbl.place(x=170, y=50)

window.mainloop()
