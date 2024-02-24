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
                      font=("times new roman", 40, "bold"), bg="dark slate grey", fg="black")
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
        self.StartDate_var = StringVar()  # New variable
        self.EndDate_var = StringVar()  # New variable

        # =========manage frame======
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="pink1")
        Manage_Frame.place(x=20, y=100, width=450, height=600)

        m_title = Label(Manage_Frame, text="JOBS", bg="IndianRed1", fg="black",
                        font=("Microsoft Yahei UI LIGHT", 24, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)




        Regbtn = Button(root, text="REJECT", width=10, command=self.reject_data)
        Regbtn.place(relx=0.1, rely=0.4, relwidth=0.18, relheight=0.08)
        Updatebtn = Button(root, text="APPROVE", width=10, command=self.update_data)
        Updatebtn.place(relx=0.1, rely=0.6, relwidth=0.18, relheight=0.08)
        backbtn = Button(root, text="back", width=10, command=self.back)
        backbtn.place(relx=0.1, rely=0.8, relwidth=0.18, relheight=0.08)




        # =========detail frame======
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="pink1")
        Detail_Frame.place(x=500, y=100, width=800, height=600)

        lbl_Search = Label(Detail_Frame, text="Search by :", bg="royal blue", fg="white",
                           font=("times new roman", 15, "bold"))
        lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Search = ttk.Combobox(Detail_Frame, width=10, textvariable=self.Search_by,
                                    font=("times new roman", 14, "bold"), state='readonly')
        combo_Search['values'] = ("status", "Qualification", "jobtitle","Date Range")
        combo_Search.grid(row=0, column=1, pady=10, padx=20)

        lbl_start_date = Label(Detail_Frame, text="Start Date:", bg="royal blue", fg="white",
                               font=("times new roman", 15, "bold"))
        lbl_start_date.grid(row=0, column=3, pady=10, padx=20, sticky="w")

        txt_start_date = Entry(root, width=15, textvariable=self.StartDate_var,
                               font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_start_date.place(relx=0.1, rely=0.18, relwidth=0.1, relheight=0.08)

        lbl_end_date = Label(Detail_Frame, text="End Date:", bg="royal blue", fg="white",
                             font=("times new roman", 15, "bold"))
        lbl_end_date.grid(row=1, column=3, pady=10, padx=20, sticky="w")

        txt_end_date = Entry(root, width=15, textvariable=self.EndDate_var,
                             font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_end_date.place(relx=0.1, rely=0.28, relwidth=0.1, relheight=0.08)


        self.txt_Address = Text(Detail_Frame, width=30, height=4, font=("times new roman", 15, "bold"),
                                bd=5, relief=GROOVE)
        self.txt_Address.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        txt_Search = Entry(Detail_Frame, width=15, textvariable=self.Search_txt, font=("times new roman", 15, "bold"),
                           bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")


        Showallbtn = Button(Detail_Frame, text="Showall", command=self.Search_data, width=10).grid(row=0, column=4,
                                                                                                  padx=10, pady=5)
        Showallbtn = Button(root, text="Showall", command=self.Search_data, width=10).place(relx=0.1, rely=0.08, relwidth=0.1, relheight=0.08)
        # ===============table frame========
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Job_table = ttk.Treeview(Table_Frame, columns=(
        "job", "company", "salary", "qualification", "department", "job vacancy", "Job posted", "Last Date","status"), xscrollcommand=scroll_x.set,
                                      yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Job_table.xview)
        scroll_y.config(command=self.Job_table.yview)

        self.Job_table.heading("job", text="job")
        self.Job_table.heading("company", text="company")
        self.Job_table.heading("salary", text="salary")
        self.Job_table.heading("qualification", text="qualification")
        self.Job_table.heading("department", text="Job ID")
        self.Job_table.heading("job vacancy", text="job vacancy")
        self.Job_table.heading("Job posted", text="Job posted")
        self.Job_table.heading("Last Date", text="Last Date")
        self.Job_table.heading("status", text="status")

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
        self.Job_table.pack(fill=BOTH, expand=1)
        self.Job_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()



    def back(self):
        self.root.destroy()
        os.system('python Mainpage.py')

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select jobtitle,email,gender,qual,jobid,address,job,qualification,status from Jobregister2")
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

    def Search_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select jobtitle,email,gender,qual,jobid,address,job,qualification,status from Jobregister2 where " + str(self.Search_by.get()) + " LIKE '%" + str(
            self.Search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Job_table.delete(*self.Job_table.get_children())
            for row in rows:
                self.Job_table.insert('', END, values=row)
            con.commit()
        con.close()

    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute("UPDATE jobregister2 SET status = 'Approved' WHERE jobid = %s", (self.Date_var.get(),))

        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("Applicant accepted", "The applicant has been accepted.")

    def Search_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        search_by = str(self.Search_by.get())

        if search_by == "status" or search_by == "Qualification" or search_by == "jobtitle":
            cur.execute(
                "SELECT jobtitle, email, gender, qual, jobid, address, job, qualification, status FROM Jobregister2 WHERE "
                + search_by + " LIKE '%" + str(self.Search_txt.get()) + "%'")
        elif search_by == "Date Range":
            start_date = str(self.StartDate_var.get())
            end_date = str(self.EndDate_var.get())
            cur.execute(
                "SELECT jobtitle, email, gender, qual, jobid, address, job, qualification, status FROM Jobregister2 WHERE "
                + "qualification >= STR_TO_DATE(%s, '%%Y-%%m-%%d') AND qualification <= STR_TO_DATE(%s, '%%Y-%%m-%%d')",
                (start_date, end_date))
        else:
            cur.execute(
                "SELECT jobtitle, email, gender, qual, jobid, address, job, qualification, status FROM Jobregister2")

        rows = cur.fetchall()
        if len(rows) != 0:
            self.Job_table.delete(*self.Job_table.get_children())
            for row in rows:
                self.Job_table.insert('', END, values=row)
            con.commit()
        con.close()


    def reject_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute("delete from  jobregister2  WHERE jobid = %s", (self.Date_var.get(),))

        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("Applicant Rejected", "The applicant has been rejected.")




root = Tk()
obj = jobs(root)
root.mainloop()

# %%
