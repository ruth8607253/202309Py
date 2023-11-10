import datasource
import psycopg2
import password
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from youbiketreeview impport 

class Window(tk.Tk):
    pass

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
    def update_data(w:window):
        try:
            datasource.updata_render_data()
        except Exception:
            messagebox.showerror("錯誤","網路部正常")
        datasource.updata_render_data()
        las
        w.after(5*60*1000,update_data)


    window=Window()
    window.title("台北市youbike2.0")
    window.resizable(width=False,height=False)
    window.after(1000,update_data,window)
    window.mainloop()

if __name__=="__main__":
    main()