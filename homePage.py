import tkinter as tk
from tkinter import *
import tkinter.font as font
import tkinter.messagebox as mb
import dataSheet
import components
import ribBuilder

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
        
        ##preparation for yieldData
        generic = components.Component()
        ##yield data
        cpudata = dataSheet.Datasheet("cpuDataBase.csv")
        cpulist = [generic] + cpudata.data
        gpudata = dataSheet.Datasheet("gpuDataBase.csv")
        gpulist = [generic] + gpudata.data
        mobodata = dataSheet.Datasheet("moboDataBase.csv")
        mobolist = [generic] + mobodata.data
        memdata = dataSheet.Datasheet("memoryDataBase.csv")
        memlist = [generic] + memdata.data
        storagedata = dataSheet.Datasheet("storageDataBase.csv")
        storagelist = [generic] + storagedata.data
        psudata = dataSheet.Datasheet("psuDataBase.csv")
        psulist = [generic] + psudata.data
        

        ##prepares all labels
        ##prepares all the labels
        labels=[]
        totalLabel = tk.Label(self.frame, text="Price:")
        labels.append(totalLabel)
        cpuLabel = tk.Label(self.frame, text="CPU:")
        cpuLabel.grid(row=1, column=1)
        labels.append(cpuLabel)
        gpuLabel = tk.Label(self.frame, text="GPU:")
        gpuLabel.grid(row=2, column=1)
        labels.append(gpuLabel)
        moboLabel = tk.Label(self.frame, text="Motherboard:")
        moboLabel.grid(row=3,column=1)
        labels.append(moboLabel)
        memLabel = tk.Label(self.frame, text="Memory:")
        memLabel.grid(row=4,column=1)
        labels.append(memLabel)
        storageLabel = tk.Label(self.frame, text="Storage:")
        storageLabel.grid(row=5, column=1)
        labels.append(storageLabel)
        psuLabel = tk.Label(self.frame, text="PSU:")
        psuLabel.grid(row=6,column=1)
        labels.append(psuLabel)
        
        totalLabel.grid(row=7,column=1)
        
        
        
        ##prepares all the dropdown menus
        cpuValue = tk.StringVar(self.frame)
        cpuValue.set("CPU Options")
        cpuDropDown = tk.OptionMenu(self.frame, cpuValue, *[component.name for component in cpulist], command=lambda x:self.updateStatusLabels(cpuLabel, x, "CPU"))
        cpuDropDown.grid(row=1, column=0, sticky=W, pady=2)
        
        gpuValue = tk.StringVar(self.frame)
        gpuValue.set("GPU Options")
        gpuDropDown = tk.OptionMenu(self.frame, gpuValue, *[component.name for component in gpulist], command=lambda x:self.updateStatusLabels(gpuLabel, x, "GPU"))
        gpuDropDown.grid(row=2, column=0, sticky=W, pady=2)
        
        moboValue = tk.StringVar(self.frame)
        moboValue.set("Motherboard Options")
        moboDropDown = tk.OptionMenu(self.frame, moboValue, *[component.name for component in mobolist], command=lambda x:self.updateStatusLabels(moboLabel, x, "Mobo"))
        moboDropDown.grid(row=3, column=0, sticky=W, pady=2)
        
        memValue = tk.StringVar(self.frame)
        memValue.set("Memory Options")
        memDropDown = tk.OptionMenu(self.frame, memValue, *[component.name for component in memlist], command=lambda x:self.updateStatusLabels(memLabel, x, "Memory"))
        memDropDown.grid(row=4, column=0, sticky=W, pady=2)
        
        storageValue = tk.StringVar(self.frame)
        storageValue.set("Storage Options")
        storageDropDown = tk.OptionMenu(self.frame, storageValue, *[component.name for component in storagelist], command=lambda x:self.updateStatusLabels(storageLabel, x, "storage"))
        storageDropDown.grid(row=5, column=0, sticky=W, pady=2)
        
        psuValue = tk.StringVar(self.frame)
        psuValue.set("PSU Options")
        psuDropDown = tk.OptionMenu(self.frame, psuValue, *[component.name for component in psulist], command=lambda x:self.updateStatusLabels(psuLabel, x, "PSU"))
        psuDropDown.grid(row=6, column=0, sticky=W, pady=2)

        ##top bar
        price_value = tk.IntVar()
        priceTextBar = tk.Entry(self.frame, textvariable=price_value)
        priceTextBar.grid(row=0, column=0, sticky=W, pady=2)


        types = ["gaming", 'business', 'computing']
        typeValues = tk.StringVar()
        typeOptions = tk.OptionMenu(self.frame, typeValues, *types)
        typeOptions.grid(row=0, column=1, sticky=W, pady=2)
        
        powerVsMoney = ["Power", "Cost-efficiency"]
        powerValues = tk.StringVar()
        powerOptions = tk.OptionMenu(self.frame, powerValues, *powerVsMoney)
        powerOptions.grid(row=0,column=2,pady=2,sticky=W)
        
        #submit button
        submitButton = tk.Button(self.frame, text='submit', command=lambda:self.processRequest([cpuValue.get(), gpuValue.get(), moboValue.get(), memValue.get(), storageValue.get(),psuValue.get()], price_value.get(), typeValues.get(),powerValues.get(), labels))
        submitButton.grid(row=7,column=0, sticky=S, pady=2)

        


        
        



    def updateStatusLabels(self,label,component, type):
        ##finds the associated object
        tempObject = None
        if component=='':
            label.config(text=type+":")
            return
        if (type=="CPU"):
            temp = dataSheet.Datasheet("cpuDataBase.csv")
            for o in temp.data:
                if o.name == component:
                    tempObject = o
        elif (type=="GPU"):
            temp = dataSheet.Datasheet("gpuDataBase.csv")
            for o in temp.data:
                if o.name == component:
                    tempObject = o
        elif (type=="Mobo"):
            temp = dataSheet.Datasheet("moboDataBase.csv")
            for o in temp.data:
                if o.name == component:
                    tempObject = o
        elif (type=="Memory"):
            temp = dataSheet.Datasheet("memoryDataBase.csv")
            for o in temp.data:
                if o.name == component:
                    tempObject = o
        elif (type=="storage"):
            temp = dataSheet.Datasheet("storageDataBase.csv")
            for o in temp.data:
                if o.name == component:
                    tempObject = o
        elif (type=="PSU"):
            temp = dataSheet.Datasheet("psuDataBase.csv")
            for o in temp.data:
                if o.name == component:
                    tempObject = o
                    
        
        label.config(text=self.generateLabel(tempObject))

        
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

    def generateLabel(self, component:components.Component):
        if (component.componentType == "CPU"):
            return "CPU: %s \n\t$%s,%sGHz,%s Cores" %(component.name, component.price, component.speed, component.cores)
        if (component.componentType == "GPU"):
            return "GPU: %s \n\t$%s,%sGHz,%s GB vRAM" %(component.name, component.price, component.speed, component.vRAM)
        if (component.componentType == "Mobo"):
            return "Motherboard: %s \n\t$%s,%s,%s,%s" %(component.name, component.price, component.chipset, component.formFactor, component.socketType)
        if (component.componentType == "Memory"):
            return "Memory: %s \n\t$%s,%sGHz" %(component.name, component.price, component.rate)
        if (component.componentType == "storage"):
            return "Storage: %s \n\t$%s,%sGB,%s" %(component.name, component.price, component.size, component.speed)
        if (component.componentType == "PSU"):
            return "PSU: %s \n\t$%s,%sW,%s" %(component.name, component.price, component.wattage, component.rating)
    
    def processRequest(self, inputList:list, budget, cType, mType, labels):
        print('Process Request: entered')
        rig = ribBuilder.rigBuilder(budget, cType, mType, inputList)
        print('Process REquest: initialization complete')
        rig.algorithm()
        print('Process Request: algorithm finished')
        print(rig.computer)
        print(rig.computer[0].name)
        print('Process Request: terminated')
        total=0
        for i in range(len(rig.computer)):
            labels[i+1].config(text=self.generateLabel(rig.computer[i]))
            total = total + int(rig.computer[i].price)
        labels[0].config(text="Price: $%s"%(total))
            