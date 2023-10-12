import tkinter as tk
from tkinter import ttk
import datasource

class Window(tk.Tk):
    def __init__(self, **a):
        super().__init__(**a)
        self.title("c9 c9 ")
        self.config(background="red") # 也可以用confiigure(bg)

        topf=tk.Frame(self,background="green") # 用Frame裝起來後，原本的config就會被蓋過(第8行)
        label=tk.Label(topf,text="aaaa",font=("Helvetica","20"))
        label.pack(padx=10,pady=10)
        # pad -> ppadding，不包含上面的標題欄的padding
        topf.pack()

        bottomf=tk.Frame(self,background="blue")
        label.pack(pady=20)
        # 可點選介面
        choice=datasource.city_names()
        choicecity=tk.StringVar(value=choice)
        self.listbox=tk.Listbox(bottomf,listvariable=choicecity,width=12)
        self.listbox.pack()
        bottomf.pack(expand=True,fill="x")
        self.listbox.bind("<<ListboxSelect>>",self.select)

        result=tk.Frame(self)
        tk.Label(result,text="年度：").grid(column=0,row=0,sticky="E",padx=10)
        tk.Label(result,text="地區：").grid(column=0,row=1,sticky="E",padx=10)
        tk.Label(result,text="人口數：").grid(column=0,row=2,sticky="E",padx=10)
        tk.Label(result,text="土地面積：").grid(column=0,row=3,sticky="E",padx=10)
        tk.Label(result,text="人口密度：").grid(column=0,row=4,sticky="E",padx=10)
        self.year=tk.StringVar()
        tk.Label(result,textvariable=self.year).grid(column=1,row=0,sticky="W",padx=10)
        self.where=tk.StringVar()
        tk.Label(result,textvariable=self.where).grid(column=1,row=1,sticky="W",padx=10)
        self.people=tk.StringVar()
        tk.Label(result,textvariable=self.people).grid(column=1,row=2,sticky="W",padx=10)
        self.ground=tk.StringVar()
        tk.Label(result,textvariable=self.ground).grid(column=1,row=3,sticky="W",padx=10)
        self.peoplep=tk.StringVar()
        tk.Label(result,textvariable=self.peoplep).grid(column=1,row=4,sticky="W",padx=10)
        result.pack()

    def select(self,event):
        select=self.listbox.curselection()[0]
        cityname=self.listbox.get(select)
        datalist=datasource.info(cityname)
        self.year.set(datalist[0])
        self.where.set(datalist[1])
        self.people.set(datalist[2])
        self.ground.set(datalist[3])
        self.peoplep.set(datalist[4])

def main():
    window =Window()
    # window.title("c9 c9 ") 跟self.title("c9 c9 ")一樣效果
    window.mainloop()

if __name__ == "__main__":
    main()