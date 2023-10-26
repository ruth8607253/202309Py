import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import data

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 把我在data.py/download裡Exception的內容傳到這邊，用視窗顯示
        try:
            data.SQL()
            messagebox.showwarning("成功",e)
        except Exception as e:
            messagebox.showerror("錯誤",e) # (視窗標題,視窗內容)
            self.destroy() # 自動關閉視窗們(顯示錯誤的視窗+300x300的視窗)
        
            

def main():
    window=Window()
    window.title("youbike2.0")
    window.geometry("300x300")
    window.resizable(width=False,height=False) # 讓視窗不能被user放大縮小
    window.mainloop()

if __name__=="__main__":
    main()