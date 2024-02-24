from tkinter import *
from PIL import ImageTk
class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Acess")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="#fafafa")

        self.bg = ImageTk.PhotoImage(file="img_11.png")
        self.lbl_bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=560, y=250, width=380, height=300)

        btn_login=Button(login_frame,text="Job Posted",command=self.panel,font=("times new roman",18,"bold"),
                         bg="dark orchid3",fg="white",
                         activeforeground="black",cursor="hand2").place(x=45,y=40,width=280,height=45)

        btn_login = Button(login_frame, text="Registered User", command=self.job_registration, font=("times new roman", 18,"bold"),
                           bg="dark orchid3", fg="white", activeforeground="white",
                           cursor="hand2").place(x=45, y=135, width=280, height=45)

        btn_login = Button(login_frame, text="Back", command=self.back,
                           font=("times new roman", 18,"bold"),
                           bg="dark orchid3", fg="white", activeforeground="black",
                           cursor="hand2").place(x=45, y=220, width=280, height=45)

    def job_registration(self):
        self.root.destroy()
        import admin_window

    def panel(self):
        self.root.destroy()
        import admin_panel

    def back(self):
        self.root.destroy()
        import Main_page

root = Tk()
obj = Main(root)
root.mainloop()

