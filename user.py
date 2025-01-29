#####contains all users and their orders


##Order
class Order():
    orderNumber = 0
    def __init__(self, user, price, computer):
        self.user = user
        self.price = price
        self.computer = computer
        orderNumber += 1
    

class User():
    def __init__(self, name, username, cart):
        self.name = name
        self.username = username
        self.cart = cart
    
    def changeName(self, name):
        self.name = name
        return True
    


    