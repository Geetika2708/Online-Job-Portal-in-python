# %%
from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import ImageTk
from tkinter import messagebox
import os


class jobs:
    def __init__(self, root):
        self.root = root
        self.root.title("Jobs Registration")
        self.root.geometry("1545x800+0+0")

        title = Label(self.root, text="Online Job Registration", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="yellow", fg="red")
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
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=600)

        m_title = Label(Manage_Frame, text="Jobs manage register", bg="crimson", fg="white",
                        font=("times new roman", 18, "bold"))
        m_title.grid(row=0, columnspan=2, pady=5)

        lbl_Name = Label(Manage_Frame, text="ID :", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_Name.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame, textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Name.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_Email.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.Email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_Email.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender :", bg="crimson", fg="white",
                           font=("times new roman", 15, "bold"))
        lbl_Gender.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        combo_Gender = ttk.Combobox(Manage_Frame, textvariable=self.Gender_var, font=("times new roman", 14, "bold"),
                                    state='readonly')
        combo_Gender['values'] = ("Male", "Female")
        combo_Gender.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Contact = Label(Manage_Frame, text="Contact :", bg="crimson", fg="white",
                            font=("times new roman", 15, "bold"))
        lbl_Contact.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame, textvariable=self.Contact_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_Contact.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_id = Label(Manage_Frame, text="Job ID :", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_id.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_id = Entry(Manage_Frame, textvariable=self.id_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_id.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address :", bg="crimson", fg="white",
                            font=("times new roman", 15, "bold"))
        lbl_Address.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame, width=26, height=3, font=("times new roman", 12))
        self.txt_Address.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Job = Label(Manage_Frame, text="Job :", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_Job.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_Job = Entry(Manage_Frame, textvariable=self.Job_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_Job.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        lbl_Qualifi = Label(Manage_Frame, text="Qualification:", bg="crimson", fg="white",
                            font=("times new roman", 15, "bold"))
        lbl_Qualifi.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        txt_Qualifi = Entry(Manage_Frame, textvariable=self.Qualifi_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_Qualifi.grid(row=8, column=1, pady=10, padx=20, sticky="w")

        # =========button frame======
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=50, y=510, width=300)

        Regbtn = Button(btn_Frame, text="quit", width=10, command=self.quit).grid(row=0, column=0, padx=10,
                                                                                              pady=5)
        Updatebtn = Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10,
                                                                                              pady=5)
        Clearbtn = Button(btn_Frame, text="select", width=10, command=self.fetch_d).grid(row=0, column=2, padx=10, pady=5)
        backbtn = Button(btn_Frame, text="back", width=10, command=self.fetch_de).grid(row=1, column=1, padx=10, pady=5)



        # =========detail frame======
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=600)

        lbl_Search = Label(Detail_Frame, text="Search by :", bg="crimson", fg="white",
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
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
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
        os.system('python Mainpage.py')

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select jobtitle,email,gender,qual,jobid,address,job,lastdate from Jobregister2 where status = 'approved' ")
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

    def quit(self):
        self.root.destroy()
        import Main_page



    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cursor = con.cursor()
        cursor.execute(
            "update login set username=%s,email=%s,qual=%s,address=%s,jobid=%s,Job=%s,qualification=%s where id=%s",
            (
             self.Email_var.get(),
             self.Gender_var.get(),
             self.Contact_var.get(),
             self.txt_Address.get('1.0', END),
             self.id_var.get(),
             self.Job_var.get(),
             self.Qualifi_var.get(),
             self.Name_var.get()
             ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def get_fields(self, username):
        con = mysql.connector.connect(host='localhost', user='root', password='', database='userdata')
        mycursor = con.cursor()
        query = 'SELECT fields FROM login WHERE username=%s'
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
        cursor.execute("SELECT username, contact, qualification,email,address FROM login WHERE id = %s", (self.Name_var.get(),))
        row = cursor.fetchone()

        if row is not None:
            self.Email_var.set(row[0])
            self.Contact_var.set(row[1])
            self.Qualifi_var.set(row[2])
            self.Gender_var.set(row[3])
            self.txt_Address.delete('1.0', END)
            self.txt_Address.insert(END, row[4])
        else:
            # Handle case when no matching record is found
            # For example, you can clear the fields
            self.Email_var.set("")
            self.Contact_var.set("")
            self.txt_Address.delete('1.0', END)
            self.Qualifi_var.set("")

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
            self.Qualifi_var.set("")

        con.close()

    def Search_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database='userdata')
        cur = con.cursor()
        cur.execute("select jobtitle,email,gender,qual,jobid,address,job,lastdate from Jobregister2 where " + str(self.Search_by.get()) + " LIKE '%" + str(
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
        query = 'select * from login2 where username =%s and password = %s'
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
login_windom.geometry('1545x780+0+0')
login_windom.title('Login Page')

bgImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(login_windom,image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_windom,text='USER LOGIN',font=('Microsoft Yahei UI LIGHT',23,'bold'),bg='white', fg='firebrick1')
heading.place(x=605,y=120)

UsernameEntry = Entry(login_windom,width=25,font=('Microsoft Yahei UI LIGHT',11,'bold'),bd=0,fg='firebrick1')
UsernameEntry.place(x=580,y=200)
UsernameEntry.insert(0,'Username')

UsernameEntry.bind('<FocusIn>',user_enter)

frame1 = Frame(login_windom,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)

passwordEntry = Entry(login_windom,width=25,font=('Microsoft Yahei UI LIGHT',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2 = Frame(login_windom,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_windom,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

loginButton = Button(login_windom,text='Login',font=('open sans',16,'bold'),fg='white',bg='firebrick1',
activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=578,y=350)

signupLabel = Label(login_windom,text='Dont have an account?',font=('open sans',9,'bold'),fg='firebrick1',
bg='white')
signupLabel.place(x=590,y=500)

newaccountButton = Button(login_windom,text='Create new one',font=('open sans',9,'bold underline'),fg='blue',bg='white',
activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)

login_windom.mainloop()

# %%
