from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk

import mysql.connector
import random

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
    qualificationEntry.delete(0, END)
    check.set(0)

def connect_database():
    if genderCombo.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '' or contactEntry.get() == '' or qualificationEntry.get() == '' or addressEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept the terms and conditions')
    else:
        id = idEntry.get()  # Get the ID from the entry field


        con = mysql.connector.connect(host='localhost', user='root', password='', database='userdata')
        mycursor = None
        try:
            mycursor = con.cursor()
            # create table if it doesn't exist
            query = 'CREATE TABLE IF NOT EXISTS login(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20), contact varchar(20), qualification varchar(50))'
            mycursor.execute(query)
        except mysql.connector.Error as err:
            if mycursor:
                mycursor.close()
            if con:
                con.close()
            messagebox.showerror('Error', f'{err}')
            return
        try:
            query = 'SELECT * FROM login WHERE username = %s'
            mycursor.execute(query, (usernameEntry.get(),))
            row = mycursor.fetchone()
            if row is not None:
                messagebox.showerror('Error', 'Username Already exists')
            else:

                query = 'INSERT INTO login(id, email, username, password, contact, qualification,address) VALUES(%s, %s, %s, %s, %s, %s,%s)'
                mycursor.execute(query, (id, genderCombo.get(), usernameEntry.get(), passwordEntry.get(), contactEntry.get(), qualificationEntry.get(),addressEntry.get()))
                con.commit()
                messagebox.showinfo('Success', 'Registration is successful')
                clear()
                signup_window.destroy()
                import signin
        except mysql.connector.Error as err:
            messagebox.showerror('Error', f'{err}')
        finally:
            if mycursor:
                mycursor.close()
            if con:
                con.close()

def login_page():
    signup_window.destroy()
    import signin

signup_window = Tk()
signup_window.title('Signup Page')
signup_window.resizable(False, False)

background = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(signup_window, image=background)
bgLabel.grid()
frame = Frame(signup_window, bg='white')
frame.place(x=554, y=10)

idLabel = Label(frame, text='ID', font=('Microsoft Yahei UI LIGHT', 10, 'bold'), bg='white', fg='firebrick1')
idLabel.grid(row=0, column=0, sticky='w', padx=25, pady=(10, 0))

idEntry = Entry(frame, width=30, font=('Microsoft Yahei UI LIGHT', 10, 'bold'), fg='white', bg='firebrick1')
idEntry.grid(row=1,column=0, sticky='w', padx=25)
idEntry.insert(0, generate_unique_id())  # Generate and insert the initial unique ID

genderLabel = Label(frame, text='Gender', font=('Microsoft Yahei UI LIGHT', 10, 'bold'), bg='white', fg='firebrick1')
genderLabel.grid(row=2, column=0, sticky='w', padx=25, pady=(10, 0))

genderCombo = ttk.Combobox(frame, values=['Male', 'Female', 'Others'], font=('Microsoft Yahei UI LIGHT', 10, 'bold'))
genderCombo.grid(row=3, column=0, sticky='w', padx=25)


usernameLabel = Label(frame, text='Email', font=('Microsoft Yahei UI LIGHT', 10, 'bold'), bg='white', fg='firebrick1')
usernameLabel.grid(row=4, column=0, sticky='w', padx=25, pady=(10, 0))

usernameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI LIGHT', 10, 'bold'), fg='white', bg='firebrick1')
usernameEntry.grid(row=5, column=0, sticky='w', padx=25)

passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI LIGHT', 10, 'bold'), bg='white', fg='firebrick1')
passwordLabel.grid(row=6, column=0, sticky='w', padx=25, pady=(10, 0))

passwordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI LIGHT', 10, 'bold'), fg='white', bg='firebrick1')
passwordEntry.grid(row=7, column=0, sticky='w', padx=25)

confirmLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI LIGHT', 10, 'bold'), bg='white', fg='firebrick1')
confirmLabel.grid(row=8, column=0, sticky='w', padx=25, pady=(10, 0))

confirmEntry = Entry(frame, width=30, font=('Microsoft Yahei UI LIGHT', 10, 'bold'), fg='white', bg='firebrick1')
confirmEntry.grid(row=9, column=0, sticky='w', padx=25)

contactLabel = Label(frame, text='Contact', font=('Microsoft Yahei UI LIGHT', 10, 'bold'), bg='white', fg='firebrick1')
contactLabel.grid(row=10, column=0, sticky='w', padx=25, pady=(10, 0))

contactEntry = Entry(frame, width=30, font=('Microsoft Yahei UI LIGHT', 10, 'bold'), fg='white', bg='firebrick1')
contactEntry.grid(row=11, column=0, sticky='w', padx=25)

qualificationLabel = Label(frame, text='Qualification', font=('Microsoft Yahei UI LIGHT', 10, 'bold'), bg='white', fg='firebrick1')
qualificationLabel.grid(row=12, column=0, sticky='w', padx=25, pady=(10, 0))

qualificationEntry = Entry(frame, width=30, font=('Microsoft Yahei UI LIGHT', 10, 'bold'), fg='white', bg='firebrick1')
qualificationEntry.grid(row=13, column=0, sticky='w', padx=25)

addressLabel = Label(frame, text='Address', font=('Microsoft Yahei UI LIGHT', 10, 'bold'), bg='white', fg='firebrick1')
addressLabel.grid(row=14, column=0, sticky='w', padx=25, pady=(10, 0))

addressEntry = Entry(frame, width=30, font=('Microsoft Yahei UI LIGHT', 10, 'bold'), fg='white', bg='firebrick1')
addressEntry.grid(row=15, column=0, sticky='w', padx=25)

check = IntVar()
checkButton = Checkbutton(frame, text='I agree to the terms and conditions', variable=check, bg='white', fg='firebrick1', font=('Microsoft Yahei UI LIGHT', 10, 'bold'))
checkButton.grid(row=16, column=0, sticky='w', padx=25, pady=(20, 0))

signupButton = Button(frame, text='Signup', font=('Microsoft Yahei UI LIGHT', 10, 'bold'), fg='white', bg='firebrick1', width=20, command=connect_database)
signupButton.grid(row=17, column=0, pady=(20, 10))

loginLabel = Label(signup_window, text='Already have an account?', font=('Microsoft Yahei UI LIGHT', 10, 'bold'), bg='white', fg='firebrick1')
loginLabel.place(x=554, y=520)

loginButton = Button(signup_window, text='Login', font=('Microsoft Yahei UI LIGHT', 10, 'bold'), fg='white', bg='firebrick1', width=15, command=login_page)
loginButton.place(x=680, y=520)

signup_window.mainloop()
