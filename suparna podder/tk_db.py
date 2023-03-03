from tkinter import *
import sqlite3
conn = sqlite3.connect("dbs.db")
curr = conn.cursor()

cl = Tk()

cl.minsize(700,500)
cl.maxsize(1366,768)


def database():
    roll = e1.get()
    name = e2.get()
    age = e3.get()
    course = e4.get()
    marks = e5.get()
    
    curr.execute("CREATE TABLE IF NOT EXISTS student (Roll INTEGER, Name STRING, Age INTEGER, Course STRING, Marks INTEGER)")


    curr.execute("INSERT INTO STUDENT(Roll, Name, Age, Course, Marks) VALUES(?,?,?,?,?)",(roll, name, age , course, marks))

conn.commit()

l = Label(cl,text="Interect with database in python gui",font=('trebuchet ms',25,'underline'),fg="blue")
l.pack()

l1 = Label(cl, text = "Roll No.", font=('trebuchet ms',12,'bold'), fg = "black")
l1.place(x = 25, y = 80)

e1 = Entry(cl,font=('trebuchet ms',12),highlightthickness=4)
e1.config(highlightbackground='black', highlightcolor="black")
e1.place(x= 100, y = 80, width=100, height="30")

l2 = Label(cl, text = "Name :", font=('trebuchet ms',12,'bold'), fg = "black")
l2.place(x = 25, y = 125)

e2 = Entry(cl,font=('trebuchet ms',12),highlightthickness=4)
e2.config(highlightbackground='black', highlightcolor="black")
e2.place(x= 100, y = 125, width=200, height="30")

l3 = Label(cl, text = "Age", font=('trebuchet ms',12,'bold'), fg = "black")
l3.place(x = 25, y = 165)

e3 = Entry(cl,font=('trebuchet ms',12),highlightthickness=4)
e3.config(highlightbackground='black', highlightcolor="black")
e3.place(x= 100, y = 165, width=80, height="30")

l4 = Label(cl, text = "Class", font=('trebuchet ms',12,'bold'), fg = "black")
l4.place(x = 25, y = 210)

e4 = Entry(cl,font=('trebuchet ms',12),highlightthickness=4)
e4.config(highlightbackground='black', highlightcolor="black")
e4.place(x= 100, y = 210, width=100, height="30")

l5 = Label(cl, text = "Marks", font=('trebuchet ms',12,'bold'), fg = "black")           
l5.place(x = 25, y = 255)

e5 = Entry(cl,font=('trebuchet ms',12),highlightthickness=4)
e5.config(highlightbackground='black', highlightcolor="black")
e5.place(x= 100, y = 255, width=100, height="30")

l6 = Label(cl, text = "Select Roll No. to\n Update/Find/Delete", font=('trebuchet ms',12,'bold'), fg = "black")
l6.place(x = 25, y = 310)

drop = OptionMenu(cl,"1","2","3","4")
drop.place(x = 25, y = 370)

b1 = Button(cl,text="Show Db",font=('trebuchet ms',12,'bold'),command=lambda:show())                       
b1.place(x = 550, y = 60)

b2 = Button(cl,text="Add Data",font=('trebuchet ms',12,'bold'),command=lambda:database())
b2.place(x = 550, y = 120)

b3 = Button(cl,text="Clear",font=('trebuchet ms',12,'bold'),command=lambda:())
b3.place(x = 550, y = 180)

b4 = Button(cl,text="Update",font=('trebuchet ms',12,'bold'),command=lambda:())
b4.place(x = 200, y = 365)

b5 = Button(cl,text="Find",font=('trebuchet ms',12,'bold'),command=lambda:())
b5.place(x = 280, y = 365)

b6 = Button(cl,text="Remove",font=('trebuchet ms',12,'bold'),command=lambda:())
b6.place(x = 360, y = 365)

b7 = Button(cl,text="Exit",font=('trebuchet ms',12,'bold'),command=lambda:())
b7.place(x = 270, y = 420)

cl.mainloop()


