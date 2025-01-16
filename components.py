class Component:
    def __init__(this, price, company, releaseDate, wattageUse, type):
        this.price = price
        this.company = company
        this.releaseDate = releaseDate
        this.wattageUse = wattageUse
        this.type = type

    def changePrice(self, price):
        self.price = price
    

class CPU(Component):
    def __init__(self, price, company, releaseDate, wattageUse, type, socket, speed, tier):
        Component.__init__(self, price, company, releaseDate, wattageUse, type)
        self.socket = socket
        self.speed = speed
        
class GPU(Component):
    def __init__(self, price, company, releaseDate, wattageUse, type, vRAM, speed, bus, tier):
        Component.__init__(self, price, company, releaseDate, wattageUse, type)
        self.vRAM = vRAM
        self.speed = speed
        self.bus = bus
        
class RAM(Component):
    def __init__(self, price, company, releaseDate, wattageUse, type, size, rate):
        Component.__init__(self, price, company, releaseDate, wattageUse, type)
        self.size = size
        self.rate = rate