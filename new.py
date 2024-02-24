# %%
from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import ImageTk
from tkinter import messagebox
import os
from datetime import date



class jobs:
    def __init__(self, root):
        self.root = root
        self.root.title("Jobs Registration")
        self.root.geometry("1545x800+0+0")

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
        self.Qualif_var = StringVar()
        self.date_var = StringVar()

        self.Search_by = StringVar()
        self.Search_txt = StringVar()

        # =========manage frame======
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="light salmon")
        Manage_Frame.place(x=20, y=80, width=450, height=800)

        m_title = Label(Manage_Frame, text="Registration Form", bg="light salmon", fg="black",
                        font=("times new roman", 18, "bold"))
        m_title.grid(row=0, columnspan=2, pady=5)

        lbl_Name = Label(Manage_Frame, text="ID :", bg="light salmon", fg="black", font=("times new roman", 15, "bold"))
        lbl_Name.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame, textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Name.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="light salmon", fg="black", font=("times new roman", 15, "bold"))
        lbl_Email.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.Email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_Email.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender :", bg="light salmon", fg="black",
                           font=("times new roman", 15, "bold"))
        lbl_Gender.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        combo_Gender = ttk.Combobox(Manage_Frame, textvariable=self.Gender_var, font=("times new roman", 14, "bold"),
                                    state='readonly')
        combo_Gender['values'] = ("Male", "Female")
        combo_Gender.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Contact = Label(Manage_Frame, text="Contact :", bg="light salmon", fg="black",
                            font=("times new roman", 15, "bold"))
        lbl_Contact.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame, textvariable=self.Contact_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_Contact.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_id = Label(Manage_Frame, text="Job ID :", bg="light salmon", fg="black", font=("times new roman", 15, "bold"))
        lbl_id.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_id = Entry(Manage_Frame, textvariable=self.id_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_id.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address :", bg="light salmon", fg="black",
                            font=("times new roman", 15, "bold"))
        lbl_Address.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame, width=26, height=3, font=("times new roman", 12))
        self.txt_Address.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Job = Label(Manage_Frame, text="Job :", bg="light salmon", fg="black", font=("times new roman", 15, "bold"))
        lbl_Job.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_Job = Entry(Manage_Frame, textvariable=self.Job_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_Job.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        lbl_Qualif = Label(Manage_Frame, text="Qualification:", bg="light salmon", fg="black",
                            font=("times new roman", 15, "bold"))
        lbl_Qualif.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        txt_Qualif = Entry(Manage_Frame, textvariable=self.Qualif_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_Qualif.grid(row=8, column=1, pady=10, padx=20, sticky="w")

        current_date = date.today().strftime("%Y-%m-%d")

        lbl_date = Label(Manage_Frame, text="Date:", bg="light salmon", fg="black",
                         font=("times new roman", 15, "bold"))
        lbl_date.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        txt_date = Entry(Manage_Frame, textvariable=self.date_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)

        # Set the default value of txt_date to the current date
        txt_date.insert(0, current_date)

        txt_date.grid(row=9, column=1, pady=10, padx=20, sticky="w")

        # =========button frame======
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="light salmon")
        btn_Frame.place(x=50, y=610, width=300)

        Regbtn = Button(btn_Frame, text="Submit", width=10, command=self.insert_data).grid(row=0, column=0, padx=10,
                                                                                              pady=5)
        Updatebtn = Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10,
                                                                                              pady=5)
        Clearbtn = Button(btn_Frame, text="Saved", width=10, command=self.fetch_d).grid(row=0, column=2, padx=10, pady=5)
        quitbtn = Button(btn_Frame, text="Main Page", width=10, command=self.back).grid(row=1, column=1, padx=10, pady=5)



        # =========detail frame======
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="light salmon")
        Detail_Frame.place(x=550, y=140, width=800, height=600)

        lbl_Search = Label(Detail_Frame, text="Search by :", bg="light salmon", fg="black",
                           font=("times new roman", 15, "bold"))
        lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Search = ttk.Combobox(Detail_Frame, width=10, textvariable=self.Search_by,
                                    font=("times new roman", 14, "bold"), state='readonly')
        combo_Search['values'] = ("jobtitle","jobid","qual","lastdate")
        combo_Search.grid(row=0, column=1, pady=10, padx=20)

        txt_Search = Entry(Detail_Frame, width=15, textvariable=self.Search_txt, font=("times new roman", 15, "bold"),
                           bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbtn = Button(Detail_Frame, text="Search", command=self.Search_data, width=10).grid(row=0, column=3,
                                                                                                 padx=10, pady=5)
        Showallbtn = Button(Detail_Frame, text="Showall", command=self.fetch_data, width=10).grid(row=0, column=4,
                                                                                                  padx=10, pady=5)

        # ===============table frame========
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="light salmon")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Job_table = ttk.Treeview(Table_Frame, columns=(
        "job", "company", "salary", "qualification", "Job ID", "job vacancy", "Job posted", "Last Date"),
                                      xscrollcommand=scroll_x.set,
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
        self.fetch_data()

    def back(self):
        self.root.destroy()
        os.system('python Main_page.py')

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select jobtitle,company,salary,qual,jobid,jobvacancy,job,lastdate from Jobregister2 where status = 'approved' ")
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
        self.Qualif_var.set("")
        self.date_var.set("")

    def quit(self):
        self.root.destroy()
        import Main_page



    def insert_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute(
                    "INSERT INTO job (id, jobid, Jobtitle, date) VALUES (%s, %s, %s, %s)",

            (
             self.Name_var.get(),
             self.id_var.get(),
             self.Job_var.get(),
             self.date_var.get(),

             ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def get_fields(self, username):
        con = mysql.connector.connect(host='localhost', user='root', password='', database='userdata')
        mycursor = con.cursor()
        query = 'SELECT fields FROM login WHERE email=%s'
        mycursor.execute(query, (username,))
        row = mycursor.fetchone()
        con.close()
        if row is not None:
            return row[0]
        else:
            return None

    def fetch_d(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute("SELECT email, contact, qualification,gender,address FROM login2 WHERE id = %s", (self.Name_var.get(),))
        row = cursor.fetchone()

        if row is not None:
            self.Email_var.set(row[0])
            self.Contact_var.set(row[1])
            self.Qualif_var.set(row[2])
            self.Gender_var.set(row[3])
            self.txt_Address.delete('1.0', END)
            self.txt_Address.insert(END, row[4])
        else:
            # Handle case when no matching record is found
            # For example, you can clear the fields
            self.Email_var.set("")
            self.Contact_var.set("")
            self.txt_Address.delete('1.0', END)
            self.Qualif_var.set("")

        con.close()

    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute(
            "update job set jobid=%s,Jobtitle=%s,date=%s where id=%s",
            (

                self.id_var.get(),
                self.Job_var.get(),
                self.date_var.get(),
                self.Name_var.get()
            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def fetch_de(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute("SELECT jobtitle FROM jobregister2 WHERE jobid = %s", (self.id_var.get(),))
        row = cursor.fetchone()

        if row is not None:
            self.Job_var.set(row[0])


        else:
            # Handle case when no matching record is found
            # For example, you can clear the fields
            self.Email_var.set("")
            self.Contact_var.set("")
            self.txt_Address.delete('1.0', END)
            self.Qualif_var.set("")

        con.close()

    def Search_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select jobtitle,company,salary,qual,jobid,jobvacancy,job,lastdate from Jobregister2 where " + str(self.Search_by.get()) + " LIKE '%" + str(
            self.Search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Job_table.delete(*self.Job_table.get_children())
            for row in rows:
                self.Job_table.insert('', END, values=row)
            con.commit()
        con.close()




def login_user():
    if UsernameEntry.get() =='' or passwordEntry.get() == '':
        messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            con = mysql.connector.connect(host='localhost',user='root', password='')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from login2 where email =%s and password = %s'
        mycursor.execute(query,(UsernameEntry.get(),passwordEntry.get()))
        row = mycursor.fetchone()

        if row is None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:

            messagebox.showinfo('Welcome', 'Login is Successful')
            login_windom.destroy()
            root = Tk()
            obj = jobs(root)
            root.mainloop()


            login_windom.destroy()




def signup_page():
    login_windom.destroy()
    import resume_user



def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if UsernameEntry.get() == 'Username':
        UsernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0,END)

# GUI Part
login_windom=Tk()
login_windom.geometry('1550x800+0+0')
login_windom.resizable(0,0)
login_windom.title('Login Page')

bgImage = ImageTk.PhotoImage(file='img_2.png')
bgLabel = Label(login_windom,image=bgImage)
bgLabel.place(x=180, y=100)

heading = Label(login_windom,text='USER LOGIN',font=('times new roman',30,'bold'), fg='black')
heading.place(x=1005,y=120)

UsernameEntry = Entry(login_windom,width=25,font=('Microsoft Yahei UI LIGHT',15,'bold'),fg='black')
UsernameEntry.place(x=1015,y=200)
UsernameEntry.insert(0,'Email')

UsernameEntry.bind('<FocusIn>',user_enter)

frame1 = Frame(login_windom,width=305,height=2,bg='black')
frame1.place(x=1015,y=230)

passwordEntry = Entry(login_windom,width=25,font=('Microsoft Yahei UI LIGHT',15,'bold'),bd=0,fg='black')
passwordEntry.place(x=1015,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2 = Frame(login_windom,width=305,height=2,bg='black')
frame2.place(x=1015,y=290)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_windom,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=1290,y=260)

loginButton = Button(login_windom,text='Login',font=('Microsoft Yahei UI LIGHT',20,'bold'),fg='black',bg='cornflower blue',
activeforeground='white',activebackground='cornflower blue',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=1015,y=350)

signupLabel = Label(login_windom,text='Dont have an account?',font=('Microsoft Yahei UI LIGHT',18,'bold'),fg='black')
signupLabel.place(x=1015,y=450)

newaccountButton = Button(login_windom,text='Create new one',font=('Microsoft Yahei UI LIGHT',14,'bold'),fg='blue',
activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=1015,y=480)

login_windom.mainloop()