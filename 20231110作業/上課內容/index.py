import datasource
import psycopg2
import password
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from youbiketreeview import YoubikeTreeView
from threading import Timer

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #---------建立介面------------------------
        #print(datasource.lastest_datetime_data())
        topFrame = tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame,text="台北市youbike及時資料",font=("arial", 20), bg="#333333", fg='#ffffff',padx=10,pady=10).pack(padx=20,pady=20)
        topFrame.pack(pady=30)
        #---------------------------------------

        #----------建立搜尋------------------------
        middleFrame = ttk.LabelFrame(self,text='')
        tk.Label(middleFrame,text='站點名稱搜尋:').pack(side='left')
        search_entry = tk.Entry(middleFrame)
        search_entry.bind("<KeyRelease>", self.OnEntryClick)
        search_entry.pack(side='left')        
        middleFrame.pack(fill='x',padx=20)
        #----------------------------------------

        #---------------建立treeView---------------
        bottomFrame = tk.Frame(self)
        
        self.youbikeTreeView = YoubikeTreeView(bottomFrame,show="headings",
                                               columns=('sna','mday','sarea','ar','tot','sbi','bemp'),
                                               height=20)
        self.youbikeTreeView.pack(side='left')
        vsb = ttk.Scrollbar(bottomFrame, orient="vertical", command=self.youbikeTreeView.yview)
        vsb.pack(side='left',fill='y')
        self.youbikeTreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=(0,30),padx=20)

def main():
    '''jsonData=datasource.download_youbike_data()
    try:
        conn = psycopg2.connect(
                                database=password.database,
                                user=password.user,
                                password=password.password,
                                host=password.host,
                                port=password.port)
    except psycopg2.Error as e:
        print("error")
        print(e)
    else:
        print("連線成功")
        datasource.create_table(conn)
        for item in jsonData:
            datasource.insert_data(conn,[item['sna'],item['sarea'],item['mday'],item['ar'],item['tot'],item['sbi'],item['bemp']])
        conn.close()'''
    def update_data(w:Window):
        try:
            datasource.updata_render_data()
        except Exception:
            messagebox.showerror("錯誤","網路部正常")
        lastest_data=datasource.updata_render_data()
        w.youbikeTreeView.update_content(lastest_data)
        #w.after(5*60*1000,update_data)

        t=Timer(5*60,update_data,args=(window,))
        t.start()

    global t,window
    window=Window()
    window.title("台北市youbike2.0")
    window.resizable(width=False,height=False)
    window.protocol("WM_DELETE_WINDOW",on_closing)
    lastest_data=datasource.lastest_datetime_data()
    window.youbikeTreeView.update_content(lastest_data)
    # window.after(1000,update_data,window)
    t=Timer(1,update_data,args=(window,))
    t.start()
    window.mainloop()

def on_closing():
    t.cancel()
    window.destroy()

if __name__=="__main__":
    t=None
    window=None
    main()