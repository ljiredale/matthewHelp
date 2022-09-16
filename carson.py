import sqlite3
from tkinter import *
import tkinter as tk
from tabulate import tabulate

class mainWin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x800")
        self.con = sqlite3.connect("tutorial.db")
        self.cur=self.con.cursor()
        self.title = Label(self, text = "Movie Inventory Management")
        self.title.place(relx=.5, rely=.1)
        self.first()
    def first(self):
        self.regButt = Button(self, text = "Register", width = 10, command = lambda: self.register())
        self.regButt.place(relx=.5, rely=.4)
        self.signButt = Button(self, text = "Sign In", width = 10, command = lambda: self.signIn())
        self.signButt.place(relx=.5, rely=.6)
    def register(self):
        self.regButt.destroy()
        self.signButt.destroy()
        self.username = StringVar()
        self.password = StringVar()
        self.userLab = Label(self, text = "Username")
        self.userLab.place(relx=.2, rely=.4)
        self.passLab = Label(self, text = "Password")
        self.passLab.place(relx=.2, rely=.5)
        self.userEntry = Entry(self, width = 50, textvariable=self.username)
        self.userEntry.place(relx=.3, rely=.4)
        self.passEntry = Entry(self, width = 50, textvariable=self.password)
        self.passEntry.place(relx=.3, rely=.5)
        self.butt = Button(self, text = "Register", width = 10, command = lambda: self.goNextReg())
        self.butt.place(relx=.5, rely=.6)
    def signIn(self):
        self.regButt.destroy()
        self.signButt.destroy()
        self.username = StringVar()
        self.password = StringVar()
        self.userLab = Label(self, text = "Username")
        self.userLab.place(relx=.2, rely=.4)
        self.passLab = Label(self, text = "Password")
        self.passLab.place(relx=.2, rely=.5)
        self.userEntry = Entry(self, width = 50, textvariable=self.username)
        self.userEntry.place(relx=.3, rely=.4)
        self.passEntry = Entry(self, width = 50, textvariable=self.password)
        self.passEntry.place(relx=.3, rely=.5)
        self.butt = Button(self, text = "Sign In", width = 10, command = lambda: self.goNextPass())
        self.butt.place(relx=.5, rely=.6)
    def goNextReg(self):
        self.cur.execute("""
        INSERT INTO data VALUES
            (?,?)
            """, (self.username.get(), self.password.get()))
        self.con.commit()
        self.userLab.destroy()
        self.passLab.destroy()
        self.userEntry.destroy()
        self.passEntry.destroy()
        self.butt.destroy()
        self.username = StringVar()
        self.password = StringVar()
        self.first()

    def goNextPass(self):
        test = False
        for row in self.cur.execute("SELECT username, password FROM data"):
            if row[0] == self.username.get() and row[1] == self.password.get():
                self.success()
                test = True
        if test == False:
            self.configure(bg = "red")
            self.l = Label(text = "Wrong Password")
            self.l.place(relx=.5, rely=.3)
            self.userLab.configure(bg = "red")
            self.passLab.configure(bg = "red")
            self.after(2000, lambda: self.goBack())
    def goBack(self):
        self.l.destroy()
        self.configure(bg="blue")
        self.userLab.configure(bg = "blue")
        self.passLab.configure(bg = "blue")

    def success(self):
        self.destroy()
        runICM()
class ICM(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x800")
        self.title = Label(self, text = "Movie Inventory Management")
        self.title.place(relx=.5, rely=.1)
        self.addNew = Button(self, text = "Add New Entry", command = lambda: self.addNewEntry())
        self.addNew.place(relx=.5, rely=.3)
        self.showNew = Button(self, text = "Show Entries", command = lambda: self.showNewEntry(1))
        self.showNew.place(relx=.5, rely=.5)
        self.popcornList = []
        self.watBotList = []
        self.snacksList = []
        self.dayList = []
        self.day = StringVar()
        self.popcorn = StringVar()
        self.watBot = StringVar()
        self.snacks = StringVar()

    def addNewEntry(self):
        self.addNew.destroy()
        self.showNew.destroy()
        self.dayLab = Label(self, text = "Day: ")
        self.dayLab.place(relx=.2, rely=.3)
        self.popLab = Label(self, text = "Popcorn: ")
        self.popLab.place(relx=.2, rely=.4)
        self.watLab = Label(self, text = "Water Bottles: ")
        self.watLab.place(relx=.2, rely=.5)
        self.snacksLab = Label(self, text = "Snack Amount: ")
        self.snacksLab.place(relx=.2, rely=.6)
        self.dayEntry = Entry(self, width = 50, textvariable=self.day)
        self.dayEntry.place(relx=.3, rely=.6)
        self.snacksEntry = Entry(self, width = 50, textvariable=self.snacks)
        self.snacksEntry.place(relx=.3, rely=.6)
        self.popEntry = Entry(self, width = 50, textvariable=self.popcorn)
        self.popEntry.place(relx=.3, rely=.4)
        self.watBotEntry = Entry(self, width = 50, textvariable=self.watBot)
        self.watBotEntry.place(relx=.3, rely=.5)
        self.continueOn = Button(self, text = "Continue", command = lambda: self.showNewEntry(0))
        self.continueOn.place(relx=.5, rely=.8)

    def showNewEntry(self, num):
        if num == 1:
            self.addNew.destroy()
            self.showNew.destroy()
            self.continueOn.destroy()
            self.dayLab = Label(self, text = "Day: ")
            self.dayLab.place(relx=.2, rely=.3)
            self.popLab = Label(self, text = "Popcorn: ")
            self.popLab.place(relx=.2, rely=.4)
            self.watLab = Label(self, text = "Water Bottles: ")
            self.watLab.place(relx=.2, rely=.5)
            self.snacksLab = Label(self, text = "Snack Amount: ")
            self.snacksLab.place(relx=.2, rely=.6)
            for i in range(len(self.snacksList)):
                self.wdN = Label(self, text = self.dayList[i])
                self.wdN.place(relx=.25 + i*.1, rely=.3)
                self.pN = Label(self, text = self.popcornList[i])
                self.pN.place(relx=.25 + i*.1, rely=.4)
                self.wN = Label(self, text = self.watBotList[i])
                self.wN.place(relx=.25 + i*.1, rely=.5)
                self.sN = Label(self, text = self.snacksList[i])
                self.sN.place(relx=.25 + i*.1, rely=.6)
            self.done = Button(self, text = "Done", command = lambda: self.beDone())
            self.done.place(relx=.5, rely=.8)

                
                            
        if num == 0:
            self.popcornList.append(self.popcorn.get())
            self.watBotList.append(self.watBot.get())
            self.snacksList.append(self.snacks.get())
            self.dayList.append(self.day.get())
            self.popcorn = StringVar()
            self.watBot = StringVar()
            self.snacks = StringVar()
            self.day = StringVar()
            self.dayLab.destroy()
            self.popLab.destroy()
            self.watLab.destroy()
            self.snacksLab.destroy()
            self.dayEntry.destroy()
            self.snacksEntry.destroy()
            self.popEntry.destroy()
            self.watBotEntry.destroy()
            self.continueOn.destroy()
            self.dayLab = Label(self, text = "Day: ")
            self.dayLab.place(relx=.2, rely=.3)
            self.popLab = Label(self, text = "Popcorn: ")
            self.popLab.place(relx=.2, rely=.4)
            self.watLab = Label(self, text = "Water Bottles: ")
            self.watLab.place(relx=.2, rely=.5)
            self.snacksLab = Label(self, text = "Snack Amount: ")
            self.snacksLab.place(relx=.2, rely=.6)
            for i in range(len(self.snacksList)):
                self.wdN = Label(self, text = self.dayList[i])
                self.wdN.place(relx=.5 + i*.1, rely=.3)
                self.pN = Label(self, text = self.popcornList[i])
                self.pN.place(relx=.5 + i*.1, rely=.4)
                self.wN = Label(self, text = self.watBotList[i])
                self.wN.place(relx=.5 + i*.1, rely=.5)
                self.sN = Label(self, text = self.snacksList[i])
                self.sN.place(relx=.5 + i*.1, rely=.6)
            self.done = Button(self, text = "Done", command = lambda: self.beDone())
            self.done.place(relx=.5, rely=.8)
        if num == -1:
            pass
        num = -1
    def beDone(self):
        self.dayLab.destroy()
        self.popLab.destroy()
        self.watLab.destroy()
        self.snacksLab.destroy()
        self.wdN.destroy()
        self.pN.destroy()
        self.wN.destroy()
        self.sN.destroy()
        self.done.destroy()
        self.addNew = Button(self, text = "Add New Entry", command = lambda: self.addNewEntry())
        self.addNew.place(relx=.5, rely=.3)
        self.showNew = Button(self, text = "Show Entries", command = lambda: self.showNewEntry(1))
        self.showNew.place(relx=.5, rely=.5)
        
def runICM():
    rI = ICM()
    rI.mainloop()
    



def runWin():
    mW = mainWin()
    mW.mainloop()
runWin()