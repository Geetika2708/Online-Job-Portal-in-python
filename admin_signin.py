from tkinter import *
from PIL import ImageTk
import subprocess
from tkinter import messagebox
import mysql.connector

# Functionality Part
def forget_pass():
    def change_password():
        if user_Entry.get() == '' or newpass_Entry.get() =='' or confirmpass_Entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required', parent=window)
        elif newpass_Entry.get() != confirmpass_Entry.get():
            messagebox.showerror('Error','Password amd confirm password are not matching', parent=window)
        else:
            con = mysql.connector.connect(host='localhost',user='root', password='', database='userdata')
            mycursor = con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query,(user_Entry.get()))
            row = mycursor.fetchone()
            if row ==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query = 'update data set password=%s where username=%s'
                mycursor.execute(query,(newpass_Entry.get(), user_Entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, Please login with new password', parent=window)
                window.destroy()

    window = Toplevel()
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bgLabel = Label(window, image=bgPic)
    bgLabel.grid()

    heading_label = Label(window, text='RESET PASSWORD', font=('arial','18','bold'), bg ='white', fg='magenta2')
    heading_label.place(x=480, y=60)

    userLabel = Label(window, text='Username', font=('arial',12, 'bold'), bg ='white', fg = 'orchid1')
    userLabel.place(x=470, y=130)

    user_Entry = Entry(window, width=25, fg='magenta2', font=('arial',11,'bold'), bd=0)
    user_Entry.place(x=470, y=160)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)

    passwordLabel = Label(window, text='New Password', font=('arial','12','bold'), bg ='white', fg='orchid1')
    passwordLabel.place(x=470, y=210)

    newpass_Entry = Entry(window, width=25, fg='magenta2', font=('arial',11,'bold'), bd=0)
    newpass_Entry.place(x=470, y=240)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

    confirmpassLabel = Label(window, text='Confirm Password', font=('arial','11','bold'), bg ='white', fg='orchid1')
    confirmpassLabel.place(x=470, y=290)

    confirmpass_Entry = Entry(window, width=25, fg='magenta2', font=('arial',11,'bold'), bd=0)
    confirmpass_Entry.place(x=470, y=320)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

    submitButton = Button(window, text='Submit', bd=0, bg='magenta2', fg='white', font=('Open Sans','16','bold'),
                                width=19, cursor='hand2', activebackground='magenta2', activeforeground='white',
                                command=change_password)
    submitButton.place(x=470, y=390)



    window.mainloop()

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
        query = 'select * from data where username =%s and password = %s'
        mycursor.execute(query,(UsernameEntry.get(),passwordEntry.get()))
        row = mycursor.fetchone()

        if row is None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            role = row[3]  # Assuming the role is stored in the 4th column of the database table
            messagebox.showinfo('Welcome', 'Login is Successful')

            # Open a new window based on the user's role
            if role == 'JobSeeker':
                jobrec()
            elif role == 'JobRecruiter':
                jobreg()
            elif role == 'Admin':
                Main_page()
            else:
                messagebox.showerror('Error', 'Unknown role')

            login_windom.destroy()




def signup_page():
    login_windom.destroy()
    import sign_up

def Main_page():
    login_windom.destroy()
    import Mainpage

def jobreg():
    login_windom.destroy()
    import jobrecruiter

def jobrec():
    login_windom.destroy()
    import job_reg


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
UsernameEntry.insert(0,'Username')

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

login_windom.mainloop()