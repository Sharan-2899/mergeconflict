class Mobile:
    def __init__(self,brand,variant,color):
        self.brand = brand         
        self.variant = variant
        self.color = color

    def show_info(self):
        print(f"{self.brand} with {self.variant}{","}{self.color} color")

iphone = Mobile("iphone", "128Gb","rosegold")
motorola = Mobile("motorola", "256Gb","comet blue")

iphone.show_info()
motorola.show_info()


# Class and Object
class Mobile():
    display_length=None
    color=None
    price=None
    Ram=None
    def on(self):
        print("phone is switched on")

phone1 = Mobile()
phone1.on()  

#ATM

class Atm:
    def balance(self, amount):
        self.amount = 10000
        return f"your current balance is : {self.amount}"

    def greet(self):
        print("welcome")

    def deposit(self, x):
        self.greet() 
        self.amount = self.amount + x
        return self.amount
    
    def withdraw(self, y):
        self.greet()
        self.amount = self.amount - y
        return self.amount


archie = Atm()
print(archie.balance(10000))
print(archie.deposit(2000))
print(archie.withdraw(500))







    