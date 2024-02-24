# %%
from tkinter import *
from tkinter import ttk
import mysql.connector
import os


class jobs:
    def __init__(self, root):
        self.root = root
        self.root.title("Jobs Registration")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Online Job Registration", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), fg="black")
        title.pack(side=TOP, fill=X)

        # =======All variables=======
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.id_var = StringVar()
        self.Job_var = StringVar()
        self.Qualifi_var = StringVar()

        self.Search_by = StringVar()
        self.Search_txt = StringVar()

        # =========manage frame======
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="coral1")
        Manage_Frame.place(x=20, y=100, width=450, height=600)

        m_title = Label(Manage_Frame, text="Jobs manage register", bg="coral1", fg="white",
                        font=("times new roman", 18, "bold"))
        m_title.grid(row=0, columnspan=2, pady=5)

        lbl_Name = Label(Manage_Frame, text="Name :", bg="coral1", fg="white", font=("times new roman", 15, "bold"))
        lbl_Name.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame, textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Name.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="coral1", fg="white", font=("times new roman", 15, "bold"))
        lbl_Email.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.Email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_Email.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender :", bg="coral1", fg="white",
                           font=("times new roman", 15, "bold"))
        lbl_Gender.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        combo_Gender = ttk.Combobox(Manage_Frame, textvariable=self.Gender_var, font=("times new roman", 14, "bold"),
                                    state='readonly')
        combo_Gender['values'] = ("Male", "Female", "Other")
        combo_Gender.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Contact = Label(Manage_Frame, text="Contact :", bg="coral1", fg="white",
                            font=("times new roman", 15, "bold"))
        lbl_Contact.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame, textvariable=self.Contact_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_Contact.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_id = Label(Manage_Frame, text="Job ID :", bg="coral1", fg="white", font=("times new roman", 15, "bold"))
        lbl_id.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_id = Entry(Manage_Frame, textvariable=self.id_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_id.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address :", bg="coral1", fg="white",
                            font=("times new roman", 15, "bold"))
        lbl_Address.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame, width=26, height=3, font=("times new roman", 12))
        self.txt_Address.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Job = Label(Manage_Frame, text="Job :", bg="coral1", fg="white", font=("times new roman", 15, "bold"))
        lbl_Job.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_Job = Entry(Manage_Frame, textvariable=self.Job_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_Job.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        lbl_Qualifi = Label(Manage_Frame, text="Qualification:", bg="coral1", fg="white",
                            font=("times new roman", 15, "bold"))
        lbl_Qualifi.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        txt_Qualifi = Entry(Manage_Frame, textvariable=self.Qualifi_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_Qualifi.grid(row=8, column=1, pady=10, padx=20, sticky="w")

        # =========button frame======
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="coral1")
        btn_Frame.place(x=50, y=510, width=300)

        Regbtn = Button(btn_Frame, text="Register", width=10, command=self.register_job).grid(row=0, column=0, padx=10,
                                                                                              pady=5)
        Updatebtn = Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10,
                                                                                              pady=5)
        Clearbtn = Button(btn_Frame, text="Clear", width=10, command=self.clear).grid(row=0, column=2, padx=10, pady=5)
        backbtn = Button(btn_Frame, text="back", width=10, command=self.back).grid(row=1, column=1, padx=10, pady=5)

        # =========detail frame======
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=600)

        lbl_Search = Label(Detail_Frame, text="Search by :", bg="crimson", fg="white",
                           font=("times new roman", 15, "bold"))
        lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Search = ttk.Combobox(Detail_Frame, width=10, textvariable=self.Search_by,
                                    font=("times new roman", 14, "bold"), state='readonly')
        combo_Search['values'] = ("Name", "Qualification", "job")
        combo_Search.grid(row=0, column=1, pady=10, padx=20)

        txt_Search = Entry(Detail_Frame, width=15, textvariable=self.Search_txt, font=("times new roman", 15, "bold"),
                           bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbtn = Button(Detail_Frame, text="Search", command=self.Search_data, width=10).grid(row=0, column=3,
                                                                                                 padx=10, pady=5)
        Showallbtn = Button(Detail_Frame, text="Showall", command=self.fetch_data, width=10).grid(row=0, column=4,
                                                                                                  padx=10, pady=5)

        # ===============table frame========
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Job_table = ttk.Treeview(Table_Frame, columns=(
        "job", "company", "salary", "qualification", "Job ID", "job vacancy", "Job posted", "Last Date"), xscrollcommand=scroll_x.set,
                                      yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Job_table.xview)
        scroll_y.config(command=self.Job_table.yview)

        self.Job_table.heading("job", text="job")
        self.Job_table.heading("company", text="company")
        self.Job_table.heading("salary", text="salary")
        self.Job_table.heading("qualification", text="qualification")
        self.Job_table.heading("Job ID", text="Job ID")
        self.Job_table.heading("job vacancy", text="job vacancy")
        self.Job_table.heading("Job posted", text="Job posted")
        self.Job_table.heading("Last Date", text="Last Date")

        self.Job_table['show'] = 'headings'
        self.Job_table.column("job", width=150)
        self.Job_table.column("company", width=150)
        self.Job_table.column("salary", width=100)
        self.Job_table.column("qualification", width=100)
        self.Job_table.column("Job ID", width=100)
        self.Job_table.column("job vacancy", width=150)
        self.Job_table.column("Job posted", width=100)
        self.Job_table.column("Last Date", width=150)
        self.Job_table.pack(fill=BOTH, expand=1)
        self.Job_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def register_job(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute("insert into jobreg values(%s,%s,%s,%s,%s,%s,%s,%s)", (self.Name_var.get(),
                                                                                   self.Email_var.get(),
                                                                                   self.Gender_var.get(),
                                                                                   self.Contact_var.get(),
                                                                                   self.id_var.get(),
                                                                                   self.txt_Address.get('1.0', END),
                                                                                   self.Job_var.get(),
                                                                                   self.Qualifi_var.get()
                                                                                   ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def back(self):
        self.root.destroy()
        os.system('python Mainpage.py')

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select * from Jobs where status = 'approved' ")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Job_table.delete(*self.Job_table.get_children())
            for row in rows:
                self.Job_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Name_var.set(""),
        self.Email_var.set(""),
        self.Gender_var.set(""),
        self.Contact_var.set(""),
        self.id_var.set(""),
        self.txt_Address.delete('1.0', END),
        self.Job_var.set(""),
        self.Qualifi_var.set("")

    def get_cursor(self, ev):
        cursor_row = self.Job_table.focus()
        contents = self.Job_table.item(cursor_row)
        row = contents['values']
        self.Name_var.set(row[0]),
        self.Email_var.set(row[1]),
        self.Gender_var.set(row[2]),
        self.Contact_var.set(row[3]),
        self.id_var.set(row[4]),
        self.txt_Address.delete('1.0', END),
        self.txt_Address.insert(END, row[5]),
        self.Job_var.set(row[6]),
        self.Qualifi_var.set(row[7])

    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute(
            "update jobs set Email=%s,Gender=%s,Contact=%s,Date=%s,Address=%s,Job=%s,Qualification=%s where Name=%s",
            (self.Email_var.get(),
             self.Gender_var.get(),
             self.Contact_var.get(),
             self.id_var.get(),
             self.txt_Address.get('1.0', END),
             self.Job_var.get(),
             self.Qualifi_var.get(),
             self.Name_var.get()
             ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def Search_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select * from Jobs where " + str(self.Search_by.get()) + " LIKE '%" + str(
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
