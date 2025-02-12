import components
import user
class Datasheet:
    def __init__(self, dataSheet):
        data = []
        ###opens data
        with open(dataSheet, "r") as csv_file:
            data = csv_file.read().split("\n")
            
        text = [data[i].split(",") for i in range (len(data))]
        
        for i in range(1, len(text)) :
            data.append({text[0][num]:text[i][num] for num in range(len(text[i]))})
        
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

    def update_Sheet(self):
        