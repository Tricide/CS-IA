class Component:
    def __init__(this, name, price, company, releaseDate, wattageUse, componentType):
        this.name = name
        this.price = price
        this.company = company
        this.releaseDate = releaseDate
        this.wattageUse = wattageUse
        this.componentType = componentType

    def changePrice(self, price):
        self.price = price

    def calculateRank(self):
        return
    

    

class CPU(Component):
    def __init__(self, name, price, company, releaseDate, wattageUse, componentType, socket, speed, cores):
        super.__init__()
        self.socket = socket
        self.speed = speed
        self.cores = cores
    
    def calculateRank(self):
        return (self.cores + self.speed)
    

        
class GPU(Component):
    def __init__(self, name, price, company, releaseDate, wattageUse, componentType, vRAM, speed, bus):
        super.__init__()
        self.vRAM = vRAM
        self.speed = speed
        self.bus = bus
        
    def calculateRank(self):
        return (self.speed + self.vRAM/4)
        
class RAM(Component):
    def __init__(self, name, price, company, releaseDate, wattageUse, componentType, size, rate):
        super.__init__()
        self.size = size
        self.rate = rate
    def calculateRank(self):
        return (self.size + self.rate/1600)
        

class PSU(Component):
    def __init__(self, name, price, company, releaseDate, componentType, wattage, rating):
        Component.__init__(self, name, price, company, releaseDate, None, componentType)
        self.wattage = wattage
        self.rating = rating
    def calculateRank(self):
        return self.wattage

class Motherboard(Component):
    def __init__(self, name, price, company, releaseDate, wattageUse, componentType, socketType, formFactor, chipset, ramSpace, ram, internet, audiochip, usb2, usb3, sata3, pcie4):
        super.__init__()
        self.socketType = socketType
        self.formFactor = formFactor
        self.chipset = chipset
        self.ramSpace = ramSpace
        self.ram = ram
        self.internet = internet
        self.audiochip = audiochip
        self.usb2 = usb2
        self.usb3 = usb3
        self.sata3 = sata3
        self.pcie4 = pcie4

    def calculateRank(self):
        return self.price

class Storage(Component):
    def __init__(self, name, price, company, releaseDate, wattageUse, componentType, size, speed, port, memoryType):
        super.__init__()
        self.size = size
        self.speed = speed
        self.port = port
        self.memoryType = memoryType
    
    def calculateRank(self):
        return self.size+self.speed

