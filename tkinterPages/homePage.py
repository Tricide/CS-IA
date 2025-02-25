import tkinter as tk
from tkinter import *
import tkinter.font as font
import dataSheet
class GUITkinter():
    ### initiate what will be constant throughout all the frames
    def __init__(self, logIn=False):
        self.root = Tk()
        self.root.title('RigBuilder')
        self.root.geometry('1000x750')
        self.frame = Frame(self.root)
        self.logIn = logIn


    def exit_window(self):
        self.root.destroy()
    
    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.pack_forget()
        self.frame.destroy()
    
    def open_login(self):
        self.clear_frame()
        self.frame = Frame(self.root)
        self.root.title('Log In')
        self.frame.pack()

        titleLabel = tk.Label(text = 'Log In', font = ('Arial', 16, 'bold'))
        titleLabel.pack()

        usernameTextBox = tk.Entry()
        usernameTextBox.pack()

        passwordTextBox = tk.Entry()
        passwordTextBox.pack()

        submitButton = tk.Button(text="Submit")
        submitButton.pack()
        self.root.mainloop()

    def open_signUp(self):
        self.clear_frame()
        self.frame = Frame(self.root)
        self.root.title('Sign Up')
        self.frame.pack()

        titleLabel = tk.Label(text = 'Sign Up', font = ('Arial', 16, 'bold'))
        titleLabel.pack()

        nameTextBox = tk.Entry()
        nameTextBox.pack()

        usernameTextBox = tk.Entry()
        usernameTextBox.pack()

        passwordTextBox = tk.Entry()
        passwordTextBox.pack()

        submitButton = tk.Button(text = 'Submit')
        submitButton.pack()
        self.root.mainloop()

    def sign_Up(self, name, username, password):
        sigma='sigma'
    
    def log_in(self, username, password):
        usernameData = dataSheet.Datasheet('usernamePassword.csv')
        if (usernameData.data[username] == password):
            self.logIn=True
            self.open_home()
        
        else:
            message = tk.messagebox.showwarning(title='Stoopid', message="Incorrect password")

            
    def log_out(self):
        self.logIn = False
        self.open_home()


    def open_home(self):
        self.clear_frame()
        self.frame = Frame(self.root)
        self.root.title('Home')
        
        titleLabel = tk.Label(text = 'Rig Builder Homepage', font=('Arial', 16, 'bold'))
        titleLabel.pack()

        if (self.logIn):
            
            rigBuilderButton = tk.Button(text="Rig Builder")
            rigBuilderButton.pack()

            ordersButton= tk.Button(text="Orders")
            ordersButton.pack()

            logOutButton = tk.Button(text="Log Out")
            logOutButton.place(relx=1, rely=0, anchor='ne')
            logOutButton.pack()

            
            
        else:
            print('else')
            
            logInButton = tk.Button(text='Log In', command=self.open_login)
            logInButton.place(relx=1, rely=0, anchor='ne')
            logInButton.pack()

            signUpButton = tk.Button(text='Sign Up')
            signUpButton.place(relx=2, rely=0, anchor='ne')
            signUpButton.pack()


            
        self.root.mainloop()
    
        
    

