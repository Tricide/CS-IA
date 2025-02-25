import tkinter as tk
from tkinter import *
import tkinter.font as font
import tkinter.messagebox as mb
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
        users = dataSheet.Datasheet('usernamePassword.csv')
        for user in users.data:
            if (user.username == username and user.password == password):
                self.logIn = True
                self.open_home()
            else:
                mb.showWarning(title='Failed Attempt', message='bad username or password')
                
    def log_out(self):
        self.logIn = False


    def open_home(self):
        self.clear_frame()
        self.create_frame()
        self.root.title('Home')
        self.frame.pack( padx=20, pady=20)
        
        titleLabel = tk.Label(self.frame, text = 'Rig Builder Homepage', font=('Arial', 16, 'bold'))
        titleLabel.pack()

        rigBuilderButton = tk.Button(self.frame, text="Rig Builder", command=self.rigBuilderPage())
        rigBuilderButton.pack()
            
        if (self.logIn):
            
            ordersButton= tk.Button(self.frame, text="Orders")
            ordersButton.pack()

            logOutButton = tk.Button(text="Log Out")
            logOutButton.place(relx=1, rely=0, anchor='ne')
            logOutButton.pack()

            
            
        else:
            
            logInButton = tk.Button(self.frame, text='Log In', command=self.open_login)
            logInButton.place(relx=1, rely=0, anchor='ne')
            logInButton.pack()

            signUpButton = tk.Button(self.frame, text='Sign Up')
            signUpButton.place(relx=2, rely=0, anchor='ne')
            signUpButton.pack()


            
        self.root.mainloop()
    
    def rigBuilderPage(self):
        self.clear_frame()
        self.create_frame()
        self.root.title("Rig Builder")
        self.frame.pack(padx=20, pady=20)
        
        ##yield data
        cpudata = dataSheet.Datasheet("cpuDataBase.csv")
        cpulist=cpudata.yieldNames()
        gpudata = dataSheet.Datasheet("gpuDataBase.csv")
        gpulist=gpudata.yieldNames()
        mobodata = dataSheet.Datasheet("moboDataBase.csv")
        mobolist = mobodata.yieldNames()
        memdata = dataSheet.Datasheet("memoryDataBase.csv")
        memlist = memdata.yieldNames()
        storagedata = dataSheet.Datasheet("storageDataBase.csv")
        storagelist = storagedata.yieldNames()
        psudata = dataSheet.Datasheet("psuDataBase.csv")
        psulist = psudata.yieldNames()
        
        cpuValue = tk.StringVar(self.frame)
        cpuValue.set("CPU Options")
        cpuDropDown = tk.optionMenu(self.frame, cpuValue, *cpulist)
        cpuDropDown.grid(row=0, column=0, sticky=W, pady=2)
        
        gpuValue = tk.StringVar(self.frame)
        gpuValue.set("CPU Options")
        gpuDropDown = tk.optionMenu(self.frame, gpuValue, *gpulist)
        gpuDropDown.grid(row=1, column=0, sticky=W, pady=2)
        
        moboValue = tk.StringVar(self.frame)
        moboValue.set("CPU Options")
        moboDropDown = tk.optionMenu(self.frame, moboValue, *mobolist)
        moboDropDown.grid(row=2, column=0, sticky=W, pady=2)
        
        memValue = tk.StringVar(self.frame)
        memValue.set("CPU Options")
        memDropDown = tk.optionMenu(self.frame, memValue, *memlist)
        memDropDown.grid(row=3, column=0, sticky=W, pady=2)
        
        storageValue = tk.StringVar(self.frame)
        storageValue.set("CPU Options")
        storageDropDown = tk.optionMenu(self.frame, storageValue, *storagelist)
        storageDropDown.grid(row=4, column=0, sticky=W, pady=2)
        
        psuValue = tk.StringVar(self.frame)
        psuValue.set("CPU Options")
        psuDropDown = tk.optionMenu(self.frame, psuValue, *psulist)
        psuDropDown.grid(row=5, column=0, sticky=W, pady=2)
        
        
        
        
        
        
        
        
    

