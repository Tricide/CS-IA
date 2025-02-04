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
    

class CPU(Component):
    def __init__(self, name, price, company, releaseDate, wattageUse, componentType, socket, speed, tier):
        Component.__init__(self, name, price, company, releaseDate, wattageUse, componentType)
        self.socket = socket
        self.speed = speed
        
class GPU(Component):
    def __init__(self, name, price, company, releaseDate, wattageUse, componentType, vRAM, speed, bus, tier):
        Component.__init__(self, name, price, company, releaseDate, wattageUse, componentType)
        self.vRAM = vRAM
        self.speed = speed
        self.bus = bus
        
class RAM(Component):
    def __init__(self, name, price, company, releaseDate, wattageUse, componentType, size, rate):
        Component.__init__(self, name, price, company, releaseDate, wattageUse, componentType)
        self.size = size
        self.rate = rate

class PSU(Component):
    def __init__(self, name, price, company, releaseDate, componentType, wattage, rating):
        Component.__init__(self, name, price, company, releaseDate, None, componentType)
        self.wattage = wattage
        self.rating = rating

class Motherboard(Component):
    def __init__(self, name, price, company, releaseDate, wattageUse, componentType, socketType, formFactor, chipset, ramSpace, ram, internet, audiochip, usb2, usb3, sata3, pcie4):
        Component.__init__(self, name, price, company, releaseDate, wattageUse, componentType)
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

class Storage(Component):
    def __init__(self, name, price, company, releaseDate, wattageUse, componentType, size, speed, port, memoryType):
        Component.__init__(self, name, price, company, releaseDate, wattageUse, componentType)
        self.size = size
        self.speed = speed
        self.port = port
        self.memoryType = memoryType

