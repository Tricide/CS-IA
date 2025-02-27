import components
import user
import csv
class Datasheet:
    def __init__(self, dataSheet):
        self.data = []
        ###opens data
        self.sheetName = 'databases/' + dataSheet
        
        self.data = self.convertToDictFromCSV()
        
        self.convertToClass()
        


    def convertToClass(self):
        c = lambda i,s : self.data[i][s]
        if 'cores' in self.data[0].keys():
            for i in range(len(self.data)):
                self.data[i] = components.CPU(c( i, 'name'), c( i, 'price'), c( i, 'company'), c( i, 'releaseDate'), c( i, 'wattageUse'), c( i, 'componentType'), c( i, 'socket'), c( i, 'speed'), c( i, 'cores'))
        elif 'vRAM' in self.data[0].keys():
            for i in range (len(self.data)):
                self.data[i] = components.GPU(c( i, 'name'), c( i, 'price'), c( i, 'company'), c( i, 'releaseDate'), c( i, 'wattageUse'), c( i, 'componentType'), c( i, 'vRAM'), c( i, 'speed'), c( i, 'bus'))
        elif 'rate' in self.data[0].keys():
            for i in range(len(self.data)):
                self.data[i] = components.RAM(c( i, 'name'), c( i, 'price'), c( i, 'company'), c( i, 'releaseDate'), c( i, 'wattageUse'), c( i, 'componentType'), c( i, 'size'), c( i, 'rate'))
        elif 'wattage' in self.data[0].keys():
            for i in range(len(self.data)):
                self.data[i] = components.PSU(c( i, 'name'), c( i, 'price'), c( i, 'company'), c( i, 'releaseDate'), c( i, 'wattageUse'), c( i, 'componentType'), c( i, 'wattage'), c( i, 'rating'))
        elif 'chipset' in self.data[0].keys():
            for i in range(len(self.data)):
                self.data[i] = components.Motherboard(c( i, 'name'), c( i, 'price'), c( i, 'company'), c( i, 'releaseDate'), c( i, 'wattageUse'), c( i, 'componentType'), c( i, 'socketType'), c( i, 'formFactor'), c( i, 'chipset'), c( i, 'ramSpace'), c( i, 'ram'), c( i, 'internet'), c( i, 'audiochip'), c( i, 'usb2'), c( i, 'usb3'), c( i, 'sata3'), c( i, 'pcie4'))
        elif 'memoryType' in self.data[0].keys():
            for i in range(len(self.data)):
                self.data[i] = components.Storage(c( i, 'name'), c( i, 'price'), c( i, 'company'), c( i, 'releaseDate'), c( i, 'wattageUse'), c( i, 'componentType'), c( i, 'size'), c( i, 'speed'), c( i , 'port'), c( i , 'memoryType'))
        elif 'username' in self.data[0].keys():
            for i in range(len(self.data)):
                self.data[i] = user.User(c(i, 'username'), c(i, 'password'))

    def convertToDict(self):
        temp = []
        for i in range(len(self.data)):
            temp.append(vars(self.data[i]))
        return temp
    
    def convertToDictFromCSV(self):
        temp = []
        with open(self.sheetName, 'r') as file:
            for i in csv.DictReader(file):
                temp.append(dict(i))
        return temp
    
    def updateDataSheet(self):
        with open(self.sheetName, 'w', newline='') as file:
            newData = self.convertToDict()
            w = csv.DictWriter(file , newData[0].keys())
            w.writeheader()
            w.writerows(newData)
    
    def yieldNames(self):
        temp = []
        for i in range(len(self.data)):
            temp.append(self.data[i].name)
        
        return temp
    
    def findObject(self, name):
        temp = None
        for o in self.data:
            if (o.name == name):
                temp = o
        return temp
