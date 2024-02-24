# %%
from tkinter import *
from tkinter import ttk
import mysql.connector
import os
from tkinter import messagebox



class jobs:
    def __init__(self, root):
        self.root = root
        self.root.title("Jobs Registration")
        self.root.geometry("1550x800+0+0")

        title = Label(self.root, text="ADMIN PANEL", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"),fg="black")
        title.pack(side=TOP, fill=X)

        # =======All variables=======
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.Date_var = StringVar()
        self.Job_var = StringVar()
        self.Qualifi_var = StringVar()

        self.Search_by = StringVar()
        self.Search_txt = StringVar()

        # =========manage frame======
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="cornflower blue")
        Manage_Frame.place(x=20, y=140, width=450, height=600)

        m_title = Label(Manage_Frame, text="Registered Users->", bg="cornflower blue", fg="white",
                        font=("Microsoft Yahei UI LIGHT", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)

        backbtn = Button(root, text="BACK",  font=("times new roman", 20, "bold"),width=10, command=self.back)
        backbtn.place(relx=0.07, rely=0.45, relwidth=0.18, relheight=0.08)

        # =========detail frame======
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="cornflower blue")
        Detail_Frame.place(x=550, y=140, width=950, height=600)

        lbl_Search = Label(Detail_Frame, text="Search by :", bg="cornflower blue", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Search = ttk.Combobox(Detail_Frame, width=10, textvariable=self.Search_by,
                                    font=("times new roman", 14, "bold"), state='readonly')
        combo_Search['values'] = ( "Qualification")
        combo_Search.grid(row=0, column=1, pady=10, padx=20)


        self.txt_Address = Text(Detail_Frame, width=30, height=4, font=("times new roman", 15, "bold"),
                                bd=5, relief=GROOVE)
        self.txt_Address.grid(row=6, column=1, pady=10, padx=8, sticky="w")

        txt_Search = Entry(Detail_Frame, width=15, textvariable=self.Search_txt, font=("times new roman", 15, "bold"),
                           bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbtn = Button(Detail_Frame, text="Search",font=("times new roman", 12, "bold"),
                           command=self.Search_data, width=10).grid(row=0, column=3,padx=10, pady=5)
        Showallbtn = Button(Detail_Frame, text="Showall",font=("times new roman", 12, "bold"),
                            command=self.fetch_data, width=10).grid(row=0, column=4,padx=10, pady=5)

        # ===============table frame========
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="cornflower blue")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Job_table = ttk.Treeview(Table_Frame, columns=(
        "job", "company", "salary", "qualification", "department", "job vacancy", "Job posted", "Last Date","status","address"), xscrollcommand=scroll_x.set,
                                      yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Job_table.xview)
        scroll_y.config(command=self.Job_table.yview)

        self.Job_table.heading("job", text="name")
        self.Job_table.heading("company", text="email")
        self.Job_table.heading("salary", text="gender")
        self.Job_table.heading("qualification", text="password")
        self.Job_table.heading("department", text="contact")
        self.Job_table.heading("job vacancy", text="qualification")
        self.Job_table.heading("Job posted", text="job id")
        self.Job_table.heading("Last Date", text="gender")
        self.Job_table.heading("status", text="address")
        self.Job_table.heading("address", text="job name")


        self.Job_table['show'] = 'headings'
        self.Job_table.column("job", width=150)
        self.Job_table.column("company", width=150)
        self.Job_table.column("salary", width=100)
        self.Job_table.column("qualification", width=100)
        self.Job_table.column("department", width=100)
        self.Job_table.column("job vacancy", width=150)
        self.Job_table.column("Job posted", width=100)
        self.Job_table.column("Last Date", width=150)
        self.Job_table.column("status", width=150)
        self.Job_table.column("address", width=150)
        self.Job_table.pack(fill=BOTH, expand=1)
        self.Job_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()



    def back(self):
        self.root.destroy()
        os.system('python Mainpage.py')

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select * from login2")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Job_table.delete(*self.Job_table.get_children())
            for row in rows:
                self.Job_table.insert('', END, values=row)
            con.commit()
        con.close()



    def get_cursor(self, ev):
        cursor_row = self.Job_table.focus()
        contents = self.Job_table.item(cursor_row)
        row = contents['values']
        self.Name_var.set(row[0]),
        self.Email_var.set(row[1]),
        self.Gender_var.set(row[2]),
        self.Contact_var.set(row[3]),
        self.Date_var.set(row[4]),
        self.txt_Address.delete('1.0', END),
        self.txt_Address.insert(END, row[5]),
        self.Job_var.set(row[6]),
        self.Qualifi_var.set(row[7])

    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute("UPDATE jobs SET status = 'Approved' WHERE name = %s", (self.Name_var.get(),))

        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("Applicant accepted", "The applicant has been accepted.")


    def reject_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute("delete from  login  WHERE name = %s", (self.Name_var.get(),))

        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("Applicant Rejected", "The applicant has been rejected.")

    def Search_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select * from login where " + str(self.Search_by.get()) + " LIKE '%" + str(
            self.Search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Job_table.delete(*self.Job_table.get_children())
            for row in rows:
                self.Job_table.insert('', END, values=row)
            con.commit()
        con.close()


root = Tk()
obj = jobs(root)
root.mainloop()

# %%
