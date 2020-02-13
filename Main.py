from os import name
from persona import Person


from Dao import Dao
import persona
import tkinter as tk

if __name__ == '__main__':
    myDao = Dao()
    per = Person()


    def btnInsertClicked():
        per.set_id(e1.get())
        per.set_name(e2.get())
        per.set_address(e3.get())
        per.set_phone(e4.get())
        print(e1.get() + e2.get() + e3.get() + e4.get())
        myDao.insert(per)
        cleanScreen()
    def btnUpdateClicked():
        per.setId(e1.get())
        per.setname(e2.get())
        per.setaddress(e3.get())
        per.setphone(e4.get())
        print(e1.get() + e2.get() + e3.get() + e4.get())
        myDao.update(per)
        cleanScreen()
    def btnDeleteClicked():
        per.setId(e1.get())
        myDao.delete(per)
        cleanScreen()
    def btnReadOneClicked():
        per.setId(e1.get())
        print(myDao.readOne(per))
        cleanScreen()
    def btnReadAllClicked():
        myDao.readAll()
        cleanScreen()
    def cleanScreen():
        e1.configure(text=None)
        e2.configure(text=None)
        e3.configure(text=None)
        e4.configure(text=None)

#"""GUI intento"""#
    m = tk.Tk()
    m.geometry('300x300')
    m.title('CRUD PERSONA')

    tk.Label(m, text='Id').grid(row=0)
    tk.Label(m, text='Name').grid(row=1)
    tk.Label(m, text='address').grid(row=2)
    tk.Label(m, text='phone').grid(row=3)
    e1 = tk.Entry(m)
    e2 = tk.Entry(m)
    e3 = tk.Entry(m)
    e4 = tk.Entry(m)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)

    ######BOTONES####
    btnInsert  = tk.Button(m, text = 'Insert', width=20, command=btnInsertClicked,  bg='blue').grid(row=5, column=1)
    btnUpdate  = tk.Button(m, text='Update', width=20, command=btnUpdateClicked, bg='red').grid(row=6, column=1)
    btnDelete  = tk.Button(m, text='Delete', width=20, command=btnDeleteClicked, bg='yellow').grid(row=7, column=1)
    btnReadOne = tk.Button(m, text='Find', width=20, command=btnReadOneClicked, bg='orange').grid(row=8, column=1)
    btnReadAll = tk.Button(m, text='RindAll', width=20, command=btnReadAllClicked, bg='green').grid(row=9, column=1)
    m.mainloop()
