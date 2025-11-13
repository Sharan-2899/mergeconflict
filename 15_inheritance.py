# Inheritance is an OOP concept where a child class (or subclass) can acquire the properties and methods of a parent class (or superclass).
# It allows code reusability, extensibility, and helps maintain clean, modular code.

'''
syntax

class Parent:
    # parent class
    pass

class Child(Parent):
    # child class inheriting Parent
    pass

'''
# single inheritance

class Parent:
    name=None
    age=None
    dateofbirth=None

class Child(Parent):
    age=None
    section=None

x=Child()
x.age=22
print(x.age) 

#  Multilevel inheritance

class GrandParent:
    def __init__(self):
        print("GrandParent init called")

class Parent(GrandParent):
    def __init__(self):
        super().__init__()   # calls GrandParent
        print("Parent init called")

class Child(Parent):
    def __init__(self):
        super().__init__()   # calls Parent (which then calls GrandParent)
        print("Child init called")

obj = Child()


# Multilevel

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        print(f"Car Model: {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery
        print(f"Battery Capacity: {self.battery} kWh")

obj = ElectricCar("Tesla", "Model S", 100)

# 
