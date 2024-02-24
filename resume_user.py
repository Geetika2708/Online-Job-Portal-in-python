from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk
import re
from tkinter import filedialog
import mysql.connector
import random
from tkinter import *
import os
import string

def generate_unique_id():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='userdata')
    mycursor = con.cursor()
    while True:
        # Generate a random 6-digit ID
        id = random.randint(100000, 999999)
        query = 'SELECT * FROM login WHERE id = %s'
        mycursor.execute(query, (id,))
        row = mycursor.fetchone()
        if row is None:
            break
    mycursor.close()
    con.close()
    return id

def clear():
    idEntry.delete(0, END)
    genderCombo.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    contactEntry.delete(0, END)
    qualificationCombo.delete(0, END)
    resumeEntry.delete(0, END)
    check.set(0)

def browse_resume():
    resume_file = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    resumeEntry.delete(0, END)
    resumeEntry.insert(END, resume_file)

def validate_contact(event):
    contact = contactEntry.get()
    if contact and not re.match(r'^\d{10}$', contact):
        messagebox.showerror("Invalid Input", "Contact should be a 10-digit number")
        contactEntry.focus_set()


def toggle_password_visibility():
    if showPassword.get():
        passwordEntry.config(show='')
    else:
        passwordEntry.config(show='*')

def toggle_confirm_password_visibility():
    if showConfirmPassword.get():
        confirmEntry.config(show='')
    else:
        confirmEntry.config(show='*')

def validate_address(event):
    address = addressEntry.get('1.0', 'end-1c')
    if address and not all(char.isalnum() or char.isspace() for char in address):
        messagebox.showerror("Invalid Input", "Address should contain alphanumeric characters only")
        addressEntry.delete('1.0', END)
        addressEntry.focus_set()

def validate_email(event):
    email = usernameEntry.get()
    if email and not re.match(r'^[\w\.-]+@gmail\.com$', email):
        messagebox.showerror("Invalid Input", "Invalid email format")
        usernameEntry.focus_set()

def validate_password(event):
    password = passwordEntry.get()
    if password and len(password) < 8:
        messagebox.showerror("Invalid Input", "Password should be at least 8 characters long")
        passwordEntry.delete(0, END)
        passwordEntry.focus_set()

def validate_qualification(event):
    qualification = qualificationEntry.get()
    if qualification and len(qualification) < 3:
        messagebox.showerror("Invalid Input", "Qualification should be at least 3 characters long")
        qualificationEntry.delete(0, END)
        qualificationEntry.focus_set()

def connect_database():
    if genderCombo.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '' or contactEntry.get() == '' or qualificationCombo.get() == '' or addressEntry.get('1.0', 'end-1c') == '' or resumeEntry.get() == '':

        messagebox.showerror('Error', 'All fields are required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept the terms and conditions')
    else:
        id = idEntry.get()  # Get the ID from the entry field



        email = usernameEntry.get()
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            messagebox.showerror("Invalid Input", "Invalid email format")
            usernameEntry.focus_set()
            return

        address = addressEntry.get('1.0', 'end-1c')
        if address and not all(char.isalnum() or char.isspace() for char in address):
            messagebox.showerror("Invalid Input", "Address should contain alphanumeric characters only")
            addressEntry.delete('1.0', END)
            addressEntry.focus_set()

        password = passwordEntry.get()
        if len(password) < 8:
            messagebox.showerror("Invalid Input", "Password should be at least 8 characters long")
            passwordEntry.delete(0, END)
            passwordEntry.focus_set()
            return

        contact = contactEntry.get()
        if not re.match(r'^\d{10}$', contact):
            messagebox.showerror("Invalid Input", "Contact should be a 10-digit number")
            contactEntry.focus_set()
            return



        con = mysql.connector.connect(host='localhost', user='root', password='', database='userdata')
        mycursor = None
        try:
            mycursor = con.cursor()
            # create table if it doesn't exist
            query = 'CREATE TABLE IF NOT EXISTS login2(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20), contact varchar(20), qualification varchar(50))'
            mycursor.execute(query)
        except mysql.connector.Error as err:
            if mycursor:
                mycursor.close()
            if con:
                con.close()
            messagebox.showerror('Error', f'{err}')
            return
        try:
            query = 'SELECT * FROM login2 WHERE email = %s'
            mycursor.execute(query, (usernameEntry.get(),))
            row = mycursor.fetchone()
            if row is not None:
                messagebox.showerror('Error', 'Username Already exists')
            else:
                query = 'INSERT INTO login2(id, gender, email, password, contact, qualification,address, resume) VALUES(%s, %s, %s, %s, %s, %s,%s,%s)'
                mycursor.execute(query, (id, genderCombo.get(), usernameEntry.get(), passwordEntry.get(), contactEntry.get(), qualificationCombo.get(), addressEntry.get('1.0', 'end-1c'), resumeEntry.get()))

                con.commit()
                messagebox.showinfo('Success', 'Registration is successful')
                clear()
                signup_window.destroy()
                import new
        except mysql.connector.Error as err:
            messagebox.showerror('Error', f'{err}')
        finally:
            if mycursor:
                mycursor.close()
            if con:
                con.close()

def login_page():
    signup_window.destroy()
    import new

signup_window = Tk()
signup_window.title('Signup Page')
signup_window.geometry("1550x800+0+0")

background = ImageTk.PhotoImage(file='img_6.png')
bgLabel = Label(signup_window, image=background)
bgLabel.place(x=30, y=80)
frame = Frame(signup_window, bg='white')
frame.place(x=1050, y=80)

idLabel = Label(frame, text='ID',font=('times new roman', 14, 'bold'), bg='white', fg='black')
idLabel.grid(row=0, column=0, sticky='w', padx=25, pady=(10, 0))

idEntry = Entry(frame, width=30, font=('times new roman', 13, 'bold'), bg='white', fg='black')
idEntry.grid(row=1, column=0, sticky='w', padx=25)
idEntry.insert(0, generate_unique_id())  # Generate and insert the initial unique ID

genderLabel = Label(frame, text='Gender', font=('times new roman', 14, 'bold'), bg='white', fg='black')
genderLabel.grid(row=2, column=0, sticky='w', padx=25, pady=(10, 0))

genderCombo = ttk.Combobox(frame, values=['Male', 'Female'], font=('Microsoft Yahei UI LIGHT', 10, 'bold'))
genderCombo.grid(row=3, column=0, sticky='w', padx=25)

usernameLabel = Label(frame, text='Email', font=('times new roman', 14, 'bold'), bg='white', fg='black')
usernameLabel.grid(row=4, column=0, sticky='w', padx=25, pady=(10, 0))

usernameEntry = Entry(frame, width=30, font=('times new roman', 13, 'bold'), bg='white', fg='black')
usernameEntry.grid(row=5, column=0, sticky='w', padx=25)
usernameEntry.bind('<FocusOut>', validate_email)

passwordLabel = Label(frame, text='Password', font=('times new roman', 14, 'bold'), bg='white', fg='black')
passwordLabel.grid(row=6, column=0, sticky='w', padx=25, pady=(10, 0))

passwordEntry = Entry(frame, width=30, font=('times new roman', 13, 'bold'), bg='white', fg='black')
passwordEntry.grid(row=7, column=0, sticky='w', padx=25)
passwordEntry.bind('<FocusOut>', validate_password)

showPassword = BooleanVar()
showPassword.set(False)

eyeCheckbutton = Checkbutton(frame, variable=showPassword, command=toggle_password_visibility)
eyeCheckbutton.grid(row=7, column=1, sticky='w')


confirmLabel = Label(frame, text='Confirm Password', font=('times new roman', 14, 'bold'), bg='white', fg='black')
confirmLabel.grid(row=8, column=0, sticky='w', padx=25, pady=(10, 0))

confirmEntry = Entry(frame, width=30, font=('times new roman', 13, 'bold'), bg='white', fg='black')
confirmEntry.grid(row=9, column=0, sticky='w', padx=25)

showConfirmPassword = BooleanVar()
showConfirmPassword.set(False)

confirmEyeCheckbutton = Checkbutton(frame, variable=showConfirmPassword, command=toggle_confirm_password_visibility)
confirmEyeCheckbutton.grid(row=9, column=1, sticky='w')

contactLabel = Label(frame, text='Contact', font=('times new roman', 14, 'bold'), bg='white', fg='black')
contactLabel.grid(row=10, column=0, sticky='w', padx=25, pady=(10, 0))

contactEntry = Entry(frame, width=30, font=('times new roman', 13, 'bold'), bg='white', fg='black')
contactEntry.grid(row=11, column=0, sticky='w', padx=25)
contactEntry.bind('<FocusOut>', validate_contact)

qualificationLabel = Label(frame, text='Qualification', font=('times new roman', 14, 'bold'), bg='white', fg='black')
qualificationLabel.grid(row=12, column=0, sticky='w', padx=25, pady=(10, 0))

qualificationCombo = ttk.Combobox(frame, values=['BBA', 'BCA', 'MBA', 'MCA', 'B.Tech'], font=('Microsoft Yahei UI LIGHT', 10, 'bold'))
qualificationCombo.grid(row=13, column=0, sticky='w', padx=25)

addressLabel = Label(frame, text='Address', font=('times new roman', 14, 'bold'), bg='white', fg='black')
addressLabel.grid(row=14, column=0, sticky='w', padx=25, pady=(10, 0))

addressEntry = Text(frame, width=29, height=3, font=('times new roman', 13, 'bold'), bg='white', fg='black')
addressEntry.grid(row=15, column=0, sticky='w', padx=25)
addressEntry.bind('<FocusOut>', validate_address)

resumeLabel = Label(frame, text='Resume', font=('times new roman', 14, 'bold'), bg='white', fg='black')
resumeLabel.grid(row=16, column=0, sticky='w', padx=25, pady=(10, 0))

resumeEntry = Entry(frame, width=30, font=('times new roman', 13, 'bold'), bg='white', fg='black')
resumeEntry.grid(row=17, column=0, sticky='w', padx=25)

browseButton = ttk.Button(frame, text='Upload', style='TButton', command=browse_resume)
browseButton.grid(row=17, column=0, sticky='e', padx=25)

check = IntVar()
checkButton = Checkbutton(frame, text='I accept all terms and conditions', variable=check, onvalue=1, offvalue=0,
font=('times new roman', 14, 'bold'), bg='white', fg='black')
checkButton.grid(row=16, column=0, sticky='w', padx=25, pady=(10, 0))

signupButton = Button(frame, text='SIGNUP', font=('times new roman', 14, 'bold'), bg='white', fg='blue', relief=GROOVE, command=connect_database)
signupButton.grid(row=17, column=1, sticky='w', padx=25, pady=(10, 20))

loginButton = Button(frame, text='LOGIN', font=('times new roman', 14, 'bold'), bg='white', fg='blue', relief=GROOVE, command=login_page)
loginButton.grid(row=18, column=0, sticky='w', padx=25, pady=(0, 10))

signup_window.mainloop()