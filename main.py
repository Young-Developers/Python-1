from tkinter import *
import time
import datetime
import requests
import json
import re

def strftime(datetimeobject, formatstring):
    now = datetime.datetime.now()
    formatstring = formatstring.replace("%%", "guest_u_never_use_20130416")
    ps = list(set(re.findall("(%.)", formatstring)))
    format2 = "|".join(ps)
    vs = datetimeobject.strftime(format2).split("|")
    for p, v in zip(ps, vs):
        formatstring = formatstring.replace(p, v)
    return formatstring.replace("guest_u_never_use_20130416", "%") 

class won():
    
    def __init__(self):

        #время
        now = datetime.datetime.now()
        self.timeVar=StringVar()
        self.timeVar.set(strftime(now, "%Y:%m:%Sс."))
        self.lbl1 = Label(tk, textvariable = self.timeVar , width = 16, anchor = "se", font = "arial 14 bold", bg = "#d9c0e3", fg = "#0c0755")
        self.lbl1.place(x = 200, y = 342)
        #время

        #дата
        self.dateVar = StringVar()
        self.dateVar.set(time.strftime("%d.%m.%Y", time.localtime()))
        self.lbl2 = Label(tk, textvariable = self.dateVar , width = 16, anchor = "se", font = "arial 14 bold", bg = "#d9c0e3", fg = "#0c0755")
        self.lbl2.place(x = 185, y = 368)
        #дата


        #поисковик
        self.ent = Entry(tk, width = 40, font = "arial 10 bold", bg = "#e2dfdf")
        self.ent.place(x = 60, y = 10)

        self.btn1 = Button(tk, text = "Найти", width = 5, bg = "grey", fg = "black", command = self.chit)
        self.btn1.place(x = 350, y = 8)
        #поисковик

        #курс долларов и евро
        self.money = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json() 
        self.text = json.dumps(str(self.money), sort_keys=True, indent=4) 
        self.parsed_string = json.loads(self.text) 
        self.mass = self.parsed_string.split() 
        self.USD = self.mass[184][:-3] 
        self.EUR = self.mass[199][:-3]
        self.usdVar = StringVar()
        self.usdVar.set(self.USD)
        self.lbl3 = Label(tk, textvariable = self.usdVar, width = 5, anchor = "sw", font = "arial 14 bold", bg = "#d9c0e3", fg = "#0c0755")
        self.lbl3.place(x = 153, y = 342)
        self.eurVar = StringVar()
        self.eurVar.set(self.EUR)
        self.lbl3 = Label(tk, textvariable = self.eurVar, width = 5, anchor = "sw", font = "arial 14 bold", bg = "#d9c0e3", fg = "#0c0755")
        self.lbl3.place(x = 153, y = 365)
        self.lbl4 = Label(tk, text = "Курс доллара:", width = 12, anchor = "sw", font = "arial 14 bold", bg = "#d9c0e3", fg = "#0c0755")
        self.lbl4.place(x = 5, y = 342)
        self.lbl5 = Label(tk, text = "Курс евро:", width = 9, anchor = "sw", font = "arial 14 bold", bg = "#d9c0e3", fg = "#0c0755")
        self.lbl5.place(x = 40, y = 365)        
        #курс долларов и евро

        
    #функция обновления даты и времени
        self.upd()
    def upd(self):
        now = datetime.datetime.now()
        self.timeVar.set((strftime(now, "%Y:%m:%Sс.")))
        self.dateVar.set(time.strftime("%d.%m.%Y", time.localtime()))
        self.usdVar.set(self.USD)
        self.eurVar.set(self.EUR)
        self.lbl1.after(1000,self.upd)
    #функция обновления даты и времени

    def chit(self):
        a = self.ent.get()
        self.ent.delete(0, END)
        print(a)
        a = ""       


        
        
        

    
tk = Tk()
tk.geometry("400x400+500+180")
tk.resizable(False,False)
tk.title("Панель помощи")
tk["bg"] = "#d9c0e3"
wn = won()
tk.mainloop()


