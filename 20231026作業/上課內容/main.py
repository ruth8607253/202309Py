import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from threading import Timer
import data

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 把我在data.py/download裡Exception的內容傳到這邊，用視窗顯示
        try:
            data.SQL()
            messagebox.showwarning("成功")
        except Exception:
            messagebox.showerror("錯誤") # (視窗標題,視窗內容)
            self.destroy() # 自動關閉視窗們(顯示錯誤的視窗+300x300的視窗)

def on_close(w:Window):
    print("(☞ﾟヮﾟ)☞成功")
    t.cancel()
    w.destroy()

t=None

def update_data()->None:
    print("做事")
    global t
    t=Timer(5,update_data) # 視窗開啟後，每5秒
    t.start()

def main():
    window=Window()
    window.title("youbike2.0")
    window.geometry("300x300")
    window.resizable(width=False,height=False) # 讓視窗不能被user放大縮小
    update_data()
    window.protocol("wM_DELETE_WINDOW",lambda :on_close(window))
    window.mainloop()
    

if __name__=="__main__":
    main()