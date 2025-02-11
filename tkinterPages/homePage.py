import tkinter as tk
from tkinter import *
import tkinter.font as font

class GUITkinter():
    def __init__(self, logIn=False):
        root = Tk()
        root.title('RigBuilder')
        root.geometry('1000x750')
        self.frame = Frame(root)
        self.logIn = logIn


    def exit_window():
        root.destroy()
    
    def clear_frame(self):
        self.frame.destroy()
    
    def open_login(self):
        self.clear_frame(self.frame)
        self.frame = Frame(self.root)
        self.frame.title('Log In')

        titleLabel = tk.Label(text = 'Log In', font = ('Arial', 16, 'bold'))
        titleLabel.pack()

        usernameTextBox = tk.Entry()
        usernameTextBox.pack()

        passwordTextBox = tk.Entry()
        passwordTextBox.pack()

        submitButton = tk.Button(command=placeeholderCommand)


    def open_home(self):
        self.clear_frame(self.frame)
        self.frame = Frame(self.root)
        self.frame.title('Home')
        
        titleLabel = tk.Label(text = 'Rig Builder Homepage', font=('Arial', 16, 'bold'))
        titleLabel.place(x=500, y=50)
        titleLabel.pack

        if (self.logIn):
            
            askdjlaskdja ='sigma'
        else: 
            logInButton = tk.Button(text='Log In', command=self.open_login)
