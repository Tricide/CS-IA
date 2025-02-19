import tkinter as tk
from tkinter import *
import tkinter.font as font

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
    
    def create_frame(self):
        self.frame = Frame(self.root)
    
    def open_login(self):
        self.clear_frame()
        self.create_frame()
        self.root.title('Log In')
        self.frame.pack( padx=20, pady=20)

        titleLabel = tk.Label(self.frame, text = 'Log In', font = ('Arial', 16, 'bold'))
        titleLabel.pack()

        usernameTextBox = tk.Entry(self.frame)
        usernameTextBox.pack()

        passwordTextBox = tk.Entry(self.frame)
        passwordTextBox.pack()

        submitButton = tk.Button(self.frame, text="Submit")
        submitButton.pack()
        self.root.mainloop()

    def open_signUp(self):
        self.clear_frame()
        self.create_frame()
        self.root.title('Sign Up')
        self.frame.pack( padx=20, pady=20)

        titleLabel = tk.Label(self.frame, text = 'Sign Up', font = ('Arial', 16, 'bold'))
        titleLabel.pack()

        nameTextBox = tk.Entry(self.frame)
        nameTextBox.pack()

        usernameTextBox = tk.Entry(self.frame)
        usernameTextBox.pack()

        passwordTextBox = tk.Entry(self.frame)
        passwordTextBox.pack()

        submitButton = tk.Button(self.frame, text = 'Submit')
        submitButton.pack()
        self.root.mainloop()

    def sign_Up(self, name, username, password):
        sigma='sigma'
    
    def log_in(self, username, password):
        if (True):
            potato = 'chicken'
    def log_out(self):
        self.logIn = False


    def open_home(self):
        self.clear_frame()
        self.create_frame()
        self.root.title('Home')
        self.frame.pack( padx=20, pady=20)
        
        titleLabel = tk.Label(self.frame, text = 'Rig Builder Homepage', font=('Arial', 16, 'bold'))
        titleLabel.pack()

        if (self.logIn):
            
            rigBuilderButton = tk.Button(self.frame, text="Rig Builder")
            rigBuilderButton.pack()
            ordersButton= tk.Button(self.frame, text="Orders")
            ordersButton.pack()

            logOutButton = tk.Button(text="Log Out")
            logOutButton.place(relx=1, rely=0, anchor='ne')
            logOutButton.pack()

            
            
        else:
            print('else')
            
            logInButton = tk.Button(self.frame, text='Log In', command=self.open_login)
            logInButton.place(relx=1, rely=0, anchor='ne')
            logInButton.pack()

            signUpButton = tk.Button(self.frame, text='Sign Up')
            signUpButton.place(relx=2, rely=0, anchor='ne')
            signUpButton.pack()


            
        self.root.mainloop()
    

