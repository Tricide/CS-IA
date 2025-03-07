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
        self.open_home()


    def open_home(self):
        self.clear_frame()
        self.create_frame()
        self.root.title('Home')
        self.frame.pack( padx=20, pady=20)
        
        titleLabel = tk.Label(self.frame, text = 'Rig Builder Homepage', font=('Arial', 16, 'bold'))
        titleLabel.pack()

        rigBuilderButton = tk.Button(self.frame, text="Rig Builder", command=self.rigBuilderPage)
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
        cpulist = ["    "] + cpudata.data
        gpudata = dataSheet.Datasheet("gpuDataBase.csv")
        gpulist = ["    "] + gpudata.data
        mobodata = dataSheet.Datasheet("moboDataBase.csv")
        mobolist = ["    "] + mobodata.data
        memdata = dataSheet.Datasheet("memoryDataBase.csv")
        memlist = ["    "] + memdata.data
        storagedata = dataSheet.Datasheet("storageDataBase.csv")
        storagelist = ["    "] + storagedata.data
        psudata = dataSheet.Datasheet("psuDataBase.csv")
        psulist = ["    "] + psudata.data
        

        ##prepares all the dropdown menus
        cpuValue = tk.StringVar(self.frame)
        cpuValue.set("CPU Options")
        cpuDropDown = tk.OptionMenu(self.frame, cpuValue, *[component.name for component in cpulist])
        cpuDropDown.grid(row=1, column=0, sticky=W, pady=2)
        
        gpuValue = tk.StringVar(self.frame)
        gpuValue.set("GPU Options")
        gpuDropDown = tk.OptionMenu(self.frame, gpuValue, *[component.name for component in gpulist])
        gpuDropDown.grid(row=2, column=0, sticky=W, pady=2)
        
        moboValue = tk.StringVar(self.frame)
        moboValue.set("Motherboard Options")
        moboDropDown = tk.OptionMenu(self.frame, moboValue, *[component.name for component in mobolist])
        moboDropDown.grid(row=3, column=0, sticky=W, pady=2)
        
        memValue = tk.StringVar(self.frame)
        memValue.set("Memory Options")
        memDropDown = tk.OptionMenu(self.frame, memValue, *[component.name for component in memlist])
        memDropDown.grid(row=4, column=0, sticky=W, pady=2)
        
        storageValue = tk.StringVar(self.frame)
        storageValue.set("Storage Options")
        storageDropDown = tk.OptionMenu(self.frame, storageValue, *[component.name for component in storagelist])
        storageDropDown.grid(row=5, column=0, sticky=W, pady=2)
        
        psuValue = tk.StringVar(self.frame)
        psuValue.set("PSU Options")
        psuDropDown = tk.OptionMenu(self.frame, psuValue, *[component.name for component in psulist])
        psuDropDown.grid(row=6, column=0, sticky=W, pady=2)

        ##option dropdowns
        
        types = ['regular', "gaming", 'business']
        
        preference = ['lowest price', 'cost-effective']
        ##prepares all the labels

        cpuLabel = tk.Label(self.frame, text="CPU:")
        gpuLabel = tk.Label(self.frame, text="GPU:")
        moboLabel = tk.Label(self.frame, text="Motherboard:")
        memLabel = tk.Label(self.frame, text="Memory:")
        storageLabel = tk.Label(self.frame, text="Storage:")
        psuLabel = tk.Label(self.frame, text="PSU:")
        totalLabel = tk.Label(self.frame, text="Price:")
        
        



    def updateStatusLabels(self,label,data):
        text = label.cget("text") + "\n"

        
    def genericPage(self, title):
        self.clear_frame()
        self.create_frame()
        self.root.title(title)
        self.frame.pack(padx=20, pady=20)

        if (self.logIn == True):
            logOutButton = tk.Button(self.frame, text="Log Out", command=self.log_out)
            logOutButton.place(x=50,y=50)

        else:
            logInButton = tk.Button(self.frame, text="Log In", command=self.open_login)
            logInButton.place(x=50,y=50)
            signInButton = tk.Button(self.frame, text="Sign up", command=self.open_signUp)
            signInButton.place(x=80,y=80)
            
        returnHomeButton = tk.Button(self.frame, text="Return Home", command=self.open_home)
        returnHomeButton.place(x=80,y=80)


        
        
        
        
        
        
    

