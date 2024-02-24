# %%
from tkinter import *
from tkinter import ttk
import mysql.connector
import os

class jobs:
    def __init__(self, root):
        self.root = root
        self.root.title("Available Jobs")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="JOB POSTED BY RECRUITER", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="dark slate grey", fg="black")
        title.pack(side=TOP, fill=X)

        # =======All variables=======
        self.Job_var = StringVar()
        self.Company_var = StringVar()
        self.Salary_var = StringVar()
        self.Qualifi_var = StringVar()
        self.Department_var = StringVar()

        self.Search_by = StringVar()
        self.Search_txt = StringVar()

        # =========manage frame======
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="pink1")
        Manage_Frame.place(x=20, y=100, width=450, height=600)

        m_title = Label(Manage_Frame, text="JOB DESCRIPTION", bg="IndianRed1", fg="black",
                        font=("Microsoft Yahei UI LIGHT", 24, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)

        lbl_Job = Label(Manage_Frame, text="Job Role :", bg="royal blue", fg="white", font=("Microsoft Yahei UI LIGHT"
                                                                                            , 15, "bold"))
        lbl_Job.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Job = Entry(Manage_Frame, textvariable=self.Job_var, font=("Microsoft Yahei UI LIGHT", 12, "bold"), bd=5,
                        relief=GROOVE)
        txt_Job.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_Company = Label(Manage_Frame, text="Company :", bg="royal blue", fg="white",
                            font=("Microsoft Yahei UI LIGHT", 15, "bold"))
        lbl_Company.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Company = Entry(Manage_Frame, textvariable=self.Company_var, font=("Microsoft Yahei UI LIGHT", 12, "bold"), bd=5,
                            relief=GROOVE)
        txt_Company.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Salary = Label(Manage_Frame, text="Salary :", bg="royal blue", fg="white",
                           font=("Microsoft Yahei UI LIGHT", 18, "bold"))
        lbl_Salary.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Salary = Entry(Manage_Frame, textvariable=self.Salary_var, font=("Microsoft Yahei UI LIGHT", 12, "bold"), bd=5,
                           relief=GROOVE)
        txt_Salary.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Qualifi = Label(Manage_Frame, text="Qualification:", bg="royal blue", fg="white",
                            font=("Microsoft Yahei UI LIGHT", 18, "bold"))
        lbl_Qualifi.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_Qualifi = Entry(Manage_Frame, textvariable=self.Qualifi_var, font=("Microsoft Yahei UI LIGHT", 12, "bold"), bd=5,
                            relief=GROOVE)
        txt_Qualifi.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_Department = Label(Manage_Frame, text="Department :", bg="royal blue", fg="white",
                               font=("Microsoft Yahei UI LIGHT", 18, "bold"))
        lbl_Department.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Department = Entry(Manage_Frame, textvariable=self.Department_var, font=("Microsoft Yahei UI LIGHT", 12, "bold"),
                               bd=5, relief=GROOVE)
        txt_Department.grid(row=5, column=1, pady=10, padx=20, sticky="w")




        # =========button frame======
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="brown4")
        btn_Frame.place(x=50, y=510, width=300)

        Postbtn = Button(btn_Frame, text="Post",fg='black',bg='yellow', width=10, command=self.register_job).grid(row=0, column=0, padx=10,
                                                                                              pady=5)
        Updatebtn = Button(btn_Frame, text="Update",fg='black',bg='yellow', width=10, command=self.update_data).grid(row=0, column=1, padx=10,
                                                                                              pady=5)
        Clearbtn = Button(btn_Frame, text="Clear",fg='black',bg='yellow', width=10, command=self.clear).grid(row=0, column=2, padx=10, pady=5)
        backbtn = Button(btn_Frame, text="back",fg='black',bg='yellow', width=10, command=self.back).grid(row=1, column=1, padx=10, pady=5)
        deletebtn = Button(btn_Frame, text="delete",fg='black',bg='yellow', width=10, command=self.back).grid(row=1, column=2, padx=10, pady=5)


        # =========detail frame======
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="pink1")
        Detail_Frame.place(x=500, y=100, width=800, height=600)

        lbl_Search = Label(Detail_Frame, text="Search by :", bg="IndianRed1", fg="black",
                           font=("times new roman", 18, "bold"))
        lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Search = ttk.Combobox(Detail_Frame, width=10, textvariable=self.Search_by,
                                    font=("times new roman", 14, "bold"), state='readonly')
        combo_Search['values'] = ("Job", "Qualification", "Salary", "Department")
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
        self.Job_table = ttk.Treeview(Table_Frame, columns=("Job", "Company", "Salary", "Qualifi", "Department"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Job_table.xview)
        scroll_y.config(command=self.Job_table.yview)

        self.Job_table.heading("Job", text="Job")
        self.Job_table.heading("Company", text="Company")
        self.Job_table.heading("Salary", text="Salary")
        self.Job_table.heading("Qualifi", text="Qualification")
        self.Job_table.heading("Department", text="Department")


        self.Job_table['show'] = 'headings'
        self.Job_table.column("Job", width=150)
        self.Job_table.column("Company", width=150)
        self.Job_table.column("Salary", width=100)
        self.Job_table.column("Qualifi", width=150)
        self.Job_table.column("Department", width=100)


        self.Job_table.pack(fill=BOTH, expand=1)
        self.Job_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def register_job(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute("insert into Jobregister1 values(%s,%s,%s,%s,%s)", (self.Job_var.get(),
                                                                           self.Company_var.get(),
                                                                           self.Salary_var.get(),
                                                                           self.Qualifi_var.get(),
                                                                           self.Department_var.get()
                                                                           ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select * from Jobregister1")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Job_table.delete(*self.Job_table.get_children())
            for row in rows:
                self.Job_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Job_var.set(""),
        self.Company_var.set(""),
        self.Salary_var.set(""),
        self.Qualifi_var.set(""),
        self.Department_var.set("")


    def back(self):
        self.root.destroy()
        os.system('python Mainpage.py')
    def get_cursor(self, ev):
        cursor_row = self.Job_table.focus()
        contents = self.Job_table.item(cursor_row)
        row = contents['values']
        self.Job_var.set(row[0]),
        self.Company_var.set(row[1]),
        self.Salary_var.set(row[2]),
        self.Qualifi_var.set(row[3]),
        self.Department_var.set(row[4])

    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute("update jobregister1 set Company=%s,Salary=%s,Qualification=%s,Department=%s where Job=%s",
                       (self.Company_var.get(),
                        self.Salary_var.get(),
                        self.Qualifi_var.get(),
                        self.Department_var.get(),
                        self.Job_var.get()
                        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def Search_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select * from Jobregister1 where " + str(self.Search_by.get()) + " LIKE '%" + str(
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
