class GetPassword(Dialog):

    def body(self, master):
        self.title("Enter New Password")

        tk.Label(master, text='Old Password:').grid(row=0, sticky=W)
        tk.Label(master, text='New Password:').grid(row=1, sticky=W)
        tk.Label(master, text='Enter New Password Again:').grid(row=2, sticky=W)

        self.oldpw = tk.Entry(master, width=16, show='*')
        self.newpw1 = tk.Entry(master, width=16, show='*')
        self.newpw2 = tk.Entry(master, width=16, show='*')

        self.oldpw.grid(row=0, column=1, sticky=W)
        self.newpw1.grid(row=1, column=1, sticky=W)
        self.newpw2.grid(row=2, column=1, sticky=W)
        return self.oldpw

    #確認/取消鍵
    def buttonbox(self):
        box = tk.Frame(self)

        w = tk.Button(box, text="確認", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="取消", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()


root = Tk()
dialog = GetPassword(root)