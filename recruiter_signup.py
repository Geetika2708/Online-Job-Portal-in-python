from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
import random
import re
def clear():
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    companyEntry.delete(0, END)
    check.set(0)

def validate_password(event):
    password = passwordEntry.get()
    if password and len(password) < 8:
        messagebox.showerror("Invalid Password", "Password should be at least 8 characters long")
        passwordEntry.delete(0, END)
        passwordEntry.focus_set()
        return
    if not re.search(r"[a-z]", password):
        messagebox.showerror("Invalid Password", "Password should contain at least one lowercase letter")
        passwordEntry.delete(0, END)
        passwordEntry.focus_set()
        return
    if not re.search(r"[A-Z]", password):
        messagebox.showerror("Invalid Password", "Password should contain at least one uppercase letter")
        passwordEntry.delete(0, END)
        passwordEntry.focus_set()
        return
    if not re.search(r"\W", password):
        messagebox.showerror("Invalid Password", "Password should contain at least one special character")
        passwordEntry.delete(0, END)
        passwordEntry.focus_set()
        return

def validate_username(event):
    username = usernameEntry.get()
    if username and len(username) < 5:
        messagebox.showerror("Invalid Username", "Username should be at least 5 characters long")
        usernameEntry.delete(0, END)
        usernameEntry.focus_set()
        return False
    if not username.isalnum():
        messagebox.showerror("Invalid Username", "Username should only contain alphanumeric characters")
        usernameEntry.delete(0, END)
        usernameEntry.focus_set()
        return False
    return True

def validate_company_name(event):
    company_name = companyEntry.get()
    if company_name and len(company_name) < 3:
        messagebox.showerror("Invalid Company Name", "Company name should have at least 3 characters")
        companyEntry.delete(0, END)
        companyEntry.focus_set()
        return False
    return True

def validate_job_name(event):
    job_name = jobEntry.get()
    if job_name and len(job_name) < 3:
        messagebox.showerror("Invalid Company Name", "Company name should have at least 3 characters")
        jobEntry.delete(0, END)
        jobEntry.focus_set()
        return False
    return True
def generate_unique_id():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='userdata')
    mycursor = con.cursor()
    while True:
        # Generate a random 6-digit ID
        id = random.randint(1000, 9999)
        query = 'SELECT * FROM jobregister2 WHERE id = %s'
        mycursor.execute(query, (id,))
        row = mycursor.fetchone()
        if row is None:
            break
    mycursor.close()
    con.close()
    return id

def connect_database():
    if usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '' or companyEntry.get() == '' or jobEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept the terms and conditions')
    else:
        id = idEntry.get()  # Get the ID from the entry field

        company_name = companyEntry.get()
        if len(company_name) < 3:
            messagebox.showerror("Invalid Company Name", "Company name should have at least 3 characters")
            companyEntry.delete(0, END)
            companyEntry.focus_set()
            return False

        job_name = jobEntry.get()
        if len(job_name) < 3:
            messagebox.showerror("Invalid Company Name", "Company name should have at least 3 characters")
            jobEntry.delete(0, END)
            jobEntry.focus_set()
            return False

        username = usernameEntry.get()
        if len(username) < 5:
            messagebox.showerror("Invalid Username", "Username should be at least 5 characters long")
            usernameEntry.delete(0, END)
            usernameEntry.focus_set()
            return False

        if not username.isalnum():
            messagebox.showerror("Invalid Username", "Username should only contain alphanumeric characters")
            usernameEntry.delete(0, END)
            usernameEntry.focus_set()
            return False

        password = passwordEntry.get()
        if len(password) < 8:
            messagebox.showerror("Invalid Password", "Password should be at least 8 characters long")
            passwordEntry.delete(0, END)
            passwordEntry.focus_set()
            return
        if not re.search(r"[a-z]", password):
            messagebox.showerror("Invalid Password", "Password should contain at least one lowercase letter")
            passwordEntry.delete(0, END)
            passwordEntry.focus_set()
            return
        if not re.search(r"[A-Z]", password):
            messagebox.showerror("Invalid Password", "Password should contain at least one uppercase letter")
            passwordEntry.delete(0, END)
            passwordEntry.focus_set()
            return
        if not re.search(r"\W", password):
            messagebox.showerror("Invalid Password", "Password should contain at least one special character")
            passwordEntry.delete(0, END)
            passwordEntry.focus_set()
            return

        con = mysql.connector.connect(host='localhost', user='root', password='', database='userdata')
        mycursor = None
        try:
            mycursor = con.cursor()
            # create table if it doesn't exist
            query = 'CREATE TABLE IF NOT EXISTS jobregister2(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20), role varchar(20))'
            mycursor.execute(query)
        except mysql.connector.Error as err:
            if mycursor:
                mycursor.close()
            if con:
                con.close()
            messagebox.showerror('Error', f'{err}')
            return
        try:
            query = 'SELECT * FROM jobregister2 WHERE username = %s'
            mycursor.execute(query, (usernameEntry.get(),))
            row = mycursor.fetchone()
            if row is not None:
                messagebox.showerror('Error', 'Username Already exists')
            else:
                query = 'INSERT INTO jobregister2(id, username, password,company,jobtitle) VALUES(%s, %s, %s,%s,%s)'
                mycursor.execute(query, (id, usernameEntry.get(), passwordEntry.get(),companyEntry.get(),jobEntry.get()))
                con.commit()
                messagebox.showinfo('Success', 'Registration is successful')
                clear()
                signup_window.destroy()
                import recruiter_signin
        except mysql.connector.Error as err:
            messagebox.showerror('Error', f'{err}')
        finally:
            if mycursor:
                mycursor.close()
            if con:
                con.close()
def signin():
    signup_window.destroy()
    import recruiter_signin
def login_page():
    signup_window.destroy()

    import recruiter_signin

signup_window = Tk()
signup_window.title('Signup Page')
signup_window.geometry("1550x800+0+0")

background = ImageTk.PhotoImage(file='img_6.png')
bgLabel = Label(signup_window, image=background)
bgLabel.place(x=120, y=120)
frame = Frame(signup_window, bg='white')
frame.place(x=1180, y=120)

heading = Label(frame, text='CREATE ACCOUNT', font=('times new roman',20,'bold'),bg='white',  fg='black')
heading.grid(row=0, column=0, padx=10, pady=10)

idLabel = Label(frame, text='ID', font=('times new roman', 14, 'bold'), bg='white', fg='black')
idLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))

idEntry = Entry(frame, width=30, font=('times new roman', 13, 'bold'), bg='white', fg='black')
idEntry.grid(row=2, column=0, sticky='w', padx=25)
idEntry.insert(0, generate_unique_id())  # Generate and insert the initial unique ID

usernameLabel = Label(frame, text='Username', font=('times new roman', 14, 'bold'), bg='white', fg='black')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))

usernameEntry = Entry(frame, width=30,font=('times new roman', 13, 'bold'), bg='white', fg='black')
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)
usernameEntry.bind('<FocusOut>', validate_username)

companyLabel = Label(frame, text='Company', font=('times new roman', 14, 'bold'), bg='white', fg='black')
companyLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))

companyEntry = Entry(frame, width=30, font=('times new roman', 13, 'bold'), bg='white', fg='black')
companyEntry.grid(row=6, column=0, sticky='w', padx=25)
companyEntry.bind('<FocusOut>', validate_company_name)

jobLabel = Label(frame, text='Job', font=('times new roman', 14, 'bold'), bg='white', fg='black')
jobLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))

jobEntry = Entry(frame, width=30,font=('times new roman', 13, 'bold'), bg='white', fg='black')
jobEntry.grid(row=8, column=0, sticky='w', padx=25)
jobEntry.bind('<FocusOut>',validate_job_name)


passwordLabel = Label(frame, text='Password', font=('times new roman', 14, 'bold'), bg='white', fg='black')
passwordLabel.grid(row=9, column=0, sticky='w', padx=25, pady=(10, 0))

passwordEntry = Entry(frame, width=30, font=('times new roman', 13, 'bold'), bg='white', fg='black')
passwordEntry.grid(row=10, column=0, sticky='w', padx=25)
passwordEntry.bind('<FocusOut>', validate_password)

confirmLabel = Label(frame, text='Confirm Password', font=('times new roman', 14, 'bold'), bg='white', fg='black')
confirmLabel.grid(row=11, column=0, sticky='w', padx=25, pady=(10, 0))

confirmEntry = Entry(frame, width=30, font=('times new roman', 13, 'bold'), bg='white', fg='black')
confirmEntry.grid(row=12, column=0, sticky='w', padx=25)

check = IntVar()
termsandconditions = Checkbutton(frame, text='I agree to the Terms and Conditions',
                                font=('times new roman', 13, 'bold'), bg='white', fg='black', activebackground='white', activeforeground='firebrick1',
                                 cursor='hand2', variable=check)
termsandconditions.grid(row=14, column=0, padx=15, pady=10)

signupButton = Button(frame, text='SignUP', font=('times new roman', 20, 'bold'), bg='brown', fg='black', activebackground='firebrick1', activeforeground='white', width=17, command=connect_database)
signupButton.grid(row=17, column=0, pady=10)

alreadyaccount = Label(frame, text="Don't have an account?",font=('times new roman', 16, 'bold'), bg='white', fg='black')
alreadyaccount.grid(row=18, column=0, sticky='w', padx=25, pady=10)
loginButton = Button(frame, text='Log in', font=('times new roman', 16, 'bold'), bg='white', fg='blue', bd=0, cursor='hand2', activebackground='white', activeforeground='blue', command=login_page)
loginButton.grid(row=19, column=0, sticky='w', padx=16, pady=10)
signup_window.mainloop()
