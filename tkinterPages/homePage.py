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

        submitButton = tk.Button()
        self.root.mainloop()


    def open_home(self):
        self.clear_frame()
        self.frame = Frame(self.root)
        self.root.title('Home')
        
        titleLabel = tk.Label(text = 'Rig Builder Homepage', font=('Arial', 16, 'bold'))
        titleLabel.pack()

        if (self.logIn):
            
            rigBuilderButton = tk.Button(text="Rig Builder")
            
            ordersButton= tk.Button(text="Orders")
            
            
        else:
            print('else')
            
            logInButton = tk.Button(text='Log In', command=self.open_login)
            logInButton.pack()
            
        self.root.mainloop()
