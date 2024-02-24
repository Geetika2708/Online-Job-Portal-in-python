# %%
from tkinter import *
from tkinter import ttk
import mysql.connector
import os
from tkinter import *
from tkinter import ttk
import mysql.connector
from datetime import date
import os
from datetime import datetime

from tkinter import messagebox

class jobs:
    def __init__(self, root):
        self.root = root
        self.root.title("Jobs Registration")
        self.root.geometry("1550x800+0+0")

        title = Label(self.root, text="JOB POSTED BY RECRUITER", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), fg="black")
        title.pack(side=TOP, fill=X)

        # =======All variables=======
        self.Name_var = StringVar()
        self.company_var = StringVar()
        self.salary_var = StringVar()
        self.qualification_var = StringVar()
        self.jobid_var = StringVar()
        self.vacancy_var = StringVar()
        self.posted_var = StringVar()
        self.status_var = StringVar()

        self.Search_by = StringVar()
        self.Search_txt = StringVar()

        # =========manage frame======
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="pale green")
        Manage_Frame.place(x=20, y=140, width=450, height=600)

        m_title = Label(Manage_Frame, text="JOB DESCRIPTION", bg="pale green", fg="black",
                       font=("times new roman", 16, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)

        lbl_Name = Label(Manage_Frame, text="ID :", bg="pale green", fg="black", font=("times new roman", 15, "bold"))
        lbl_Name.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame, textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Name.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_company = Label(Manage_Frame, text="Company:", bg="pale green", fg="black", font=("times new roman", 15, "bold"))
        lbl_company.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_company = Entry(Manage_Frame, textvariable=self.company_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_company.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_salary = Label(Manage_Frame, text="Salary :", bg="pale green", fg="black",
                           font=("times new roman", 15, "bold"))
        lbl_salary.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_salary = Entry(Manage_Frame, textvariable=self.salary_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_salary.grid(row=3, column=1, pady=10, padx=20, sticky="w")
        txt_salary.bind("<FocusOut>", self.validate_salary)

        lbl_qualification = Label(Manage_Frame, text="Qualification :", bg="pale green", fg="black",
                            font=("times new roman", 15, "bold"))
        lbl_qualification.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_qualification = Entry(Manage_Frame, textvariable=self.qualification_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_qualification.grid(row=4, column=1, pady=10, padx=20, sticky="w")
        txt_qualification.bind("<FocusOut>", self.validate_qualification)

        lbl_jobid = Label(Manage_Frame, text="Job ID :", bg="pale green", fg="black", font=("times new roman", 15, "bold"))
        lbl_jobid.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_jobid = Entry(Manage_Frame, textvariable=self.jobid_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_jobid.grid(row=5, column=1, pady=10, padx=20, sticky="w")
        txt_jobid.bind("<FocusOut>", self.validate_jobid)

        lbl_Address = Label(Manage_Frame, text="Job Vacancy :", bg="pale green", fg="black",
                            font=("times new roman", 15, "bold"))
        lbl_Address.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame, width=26, height=3, font=("times new roman", 12))
        self.txt_Address.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        current_date = date.today().strftime("%Y-%m-%d")

        txt_vacancy = Entry(Manage_Frame, textvariable=self.vacancy_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)

        # Set the default value of txt_vacancy to the current date
        lbl_current = Label(Manage_Frame, text="Date :", bg="pale green", fg="black",
                            font=("times new roman", 15, "bold"))
        lbl_current.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_vacancy.insert(0, current_date)
        txt_vacancy.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        lbl_posted = Label(Manage_Frame, text="Last date:", bg="pale green", fg="black",
                           font=("times new roman", 15, "bold"))



        lbl_posted = Label(Manage_Frame, text="Last Date:", bg="pale green", fg="black",
                            font=("times new roman", 15, "bold"))
        lbl_posted.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        txt_posted = Entry(Manage_Frame, textvariable=self.posted_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_posted.grid(row=8, column=1, pady=10, padx=20, sticky="w")
        txt_posted.bind("<FocusOut>", self.validate_date)

        # =========button frame======
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="pale green")
        btn_Frame.place(x=50, y=510, width=300)

        Regbtn = Button(btn_Frame, text="QUIT",font=("times new roman", 10, "bold"), width=10, command=root.destroy).grid(row=0, column=0, padx=10,
                                                                                              pady=5)
        Updatebtn = Button(btn_Frame, text="SUBMIT", font=("times new roman", 10, "bold"),width=10, command=self.update_data).grid(row=0, column=1, padx=10,
                                                                                              pady=5)
        Clearbtn = Button(btn_Frame, text="SAVED", font=("times new roman", 10, "bold"),width=10, command=self.fetch_d).grid(row=0, column=2, padx=10, pady=5)
        backbtn = Button(btn_Frame, text="MAIN PAGE", font=("times new roman", 10, "bold"),width=10, command=self.quit).grid(row=1, column=1, padx=10, pady=5)

        # =========detail frame======
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="pale green")
        Detail_Frame.place(x=550, y=140, width=900, height=600)

        lbl_Search = Label(Detail_Frame, text="Search by :", bg="pale green", fg="black",
                           font=("times new roman", 16, "bold"))
        lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Search = ttk.Combobox(Detail_Frame, width=10, textvariable=self.Search_by,
                                    font=("times new roman", 14, "bold"), state='readonly')
        combo_Search['values'] = ("jobid", "jobtitle","lastdate")
        combo_Search.grid(row=0, column=1, pady=10, padx=20)

        txt_Search = Entry(Detail_Frame, width=15, textvariable=self.Search_txt, font=("times new roman", 15, "bold"),
                           bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbtn = Button(Detail_Frame, text="Search", font=("times new roman", 14, "bold"),command=self.Search_data, width=10).grid(row=0, column=3,
                                                                                                 padx=10, pady=5)
        Showallbtn = Button(Detail_Frame, text="Showall",font=("times new roman", 14, "bold"), command=self.fetch_data, width=10).grid(row=0, column=4,
                                                                                                  padx=10, pady=5)

        # ===============table frame========
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="pale green")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Job_table = ttk.Treeview(Table_Frame, columns=(
        "job", "company", "salary", "qualification", "Job ID", "job vacancy", "Job posted", "Last Date","status"), xscrollcommand=scroll_x.set,
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
        self.Job_table.heading("status", text="status")

        self.Job_table['show'] = 'headings'
        self.Job_table.column("job", width=150)
        self.Job_table.column("company", width=150)
        self.Job_table.column("salary", width=100)
        self.Job_table.column("qualification", width=100)
        self.Job_table.column("Job ID", width=100)
        self.Job_table.column("job vacancy", width=150)
        self.Job_table.column("Job posted", width=100)
        self.Job_table.column("Last Date", width=150)
        self.Job_table.column("status", width=150)
        self.Job_table.pack(fill=BOTH, expand=1)
        self.Job_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def register_job(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute("insert into jobs(job,company,salary,qual,jobid,jobvacancy,job,lastdate) values(%s,%s,%s,%s,%s,%s,%s,%s)", (self.Name_var.get(),
                                                                                   self.company_var.get(),
                                                                                   self.salary_var.get(),
                                                                                   self.qualification_var.get(),
                                                                                   self.jobid_var.get(),
                                                                                   self.txt_Address.get('1.0', END),
                                                                                   self.vacancy_var.get(),
                                                                                   self.posted_var.get()
                                                                                   ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def validate_salary(self, event):
        salary = self.salary_var.get()
        if salary and not salary.isdigit() or int(salary) <= 0:
            messagebox.showerror("Error", "Invalid salary input")
            self.salary_var.set("")  # Clear the invalid input
            self.txt_salary.focus_set()  # Set focus back to the salary entry field
            self.txt_salary.icursor(0)  # Mo

    def validate_qualification(self, event):
        qualification = self.qualification_var.get()
        if qualification and len(qualification) < 3:
            messagebox.showerror("Error", "Qualification should not be less than 3 words")
            self.qualification_var.set("")  # Clear the invalid input
            self.txt_qualification.focus_set()  # Set focus back to the qualification entry field

    def validate_jobid(self, event):
        jobid = self.jobid_var.get()
        if jobid and not jobid.isdigit():
            messagebox.showerror("Error", "Job ID must be a number")
            self.jobid_var.set("")  # Clear the invalid input
            self.txt_jobid.focus_set()  # Set focus back to the job ID entry field

    def validate_date(self, event):
        date_str = self.posted_var.get()
        if date_str:
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                if date < datetime.today().date():
                    messagebox.showerror("Error", "Invalid date. Date cannot be in the past.")
                    self.posted_var.set("")
                    self.txt_posted.focus_set()
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
                self.posted_var.set("")
                self.txt_posted.focus_set()

    def validate_current_date(self, event):
        date_str = self.vacancy_var.get()
        if date_str:
            date_format = "%Y-%m-%d"
            try:
                date_obj = datetime.strptime(date_str, date_format).date()
            except ValueError:
                messagebox.showerror("Error", f"Invalid date format. Please use {date_format}.")
                self.vacancy_var.set("")
                self.txt_vacancy.focus_set()
                return

            if date_obj < date.today():
                messagebox.showerror("Error", "Invalid date. Date cannot be in the past.")
                self.vacancy_var.set("")
                self.txt_vacancy.focus_set()
            else:
                self.vacancy_var.set(date_obj.strftime(date_format))

    def back(self):
        self.root.destroy()
        os.system('python Mainpage.py')

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select jobtitle,company,salary,qual,jobid,jobvacancy,job,lastdate,status from Jobregister2")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Job_table.delete(*self.Job_table.get_children())
            for row in rows:
                self.Job_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Name_var.set(""),
        self.company_var.set(""),
        self.salary_var.set(""),
        self.qualification_var.set(""),
        self.jobid_var.set(""),
        self.txt_Address.delete('1.0', END),
        self.vacancy_var.set(""),
        self.posted_var.set("")

    def get_cursor(self, ev):
        cursor_row = self.Job_table.focus()
        contents = self.Job_table.item(cursor_row)
        row = contents['values']
        self.Name_var.set(row[0]),
        self.company_var.set(row[1]),
        self.salary_var.set(row[2]),
        self.qualification_var.set(row[3]),
        self.jobid_var.set(row[4]),
        self.txt_Address.delete('1.0', END),
        self.txt_Address.insert(END, row[5]),
        self.vacancy_var.set(row[6]),
        self.posted_var.set(row[7])

    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute(
            "update jobregister2 set company=%s,salary=%s,qual=%s,jobid=%s,jobvacancy=%s,Job=%s,lastdate=%s where id=%s",
            (self.company_var.get(),
             self.salary_var.get(),
             self.qualification_var.get(),
             self.jobid_var.get(),
             self.txt_Address.get('1.0', END),
             self.vacancy_var.get(),
             self.posted_var.get(),
             self.Name_var.get()
             ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def quit(self):
        self.root.destroy()
        import Main_page

    def fetch_d(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute("SELECT company FROM jobregister2 WHERE id = %s", (self.Name_var.get(),))
        row = cursor.fetchone()

        if row is not None:
            self.company_var.set(row[0])
    def Search_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select jobtitle,company,salary,qual,jobid,jobvacancy,job,lastdate,status from Jobregister2 where " + str(self.Search_by.get()) + " LIKE '%" + str(
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
