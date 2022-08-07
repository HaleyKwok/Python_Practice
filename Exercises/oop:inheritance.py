class Vehicle:
    def general_use(self):
        print("The general use of the vehicle is transportation.")
class Car(Vehicle):
    def __init__(self):
        print("The car is a vehicle.")
        self.general_use()
class Truck(Vehicle):
    def __init__(self):
        print("The truck is a vehicle.")
        self.general_use()
class Bus(Vehicle):
    def __init__(self):
        print("The bus is a vehicle.")
        self.general_use()
class Motorcycle(Vehicle):
    def __init__(self):
        print("The motorcycle is a vehicle.")
        self.general_use()
class Bicycle(Vehicle):
    def __init__(self):
        print("The bicycle is a vehicle.")
        self.general_use()

c = Car()
t = Truck()
b = Bus()
m = Motorcycle()
B = Bicycle()

print('------------------------------------------')

class Vehicle:
    def general_use(self):
        print("general use: transportation.")

class Car(Vehicle):
    def __int__(self):
        print("I'm a car.")
        self.wheel = 4
        self.has_roof = True
    def specific_use(self):
        print("specific use: 1. communte to work; 2. vacation with family.")
    
class Motorcycle(Vehicle):
    def __init__(self):
        print("I'm a motorcycle.")
        self.wheel = 2
        self.has_roof = False
    def specific_use(self):
        print("specific use: 1. hit the road; 2. racing.")

# c = Car()
# c.general_use()
# c.specific_use()
# print(c.wheel)
# print(c.has_roof)

m = Motorcycle()
m.general_use()
m.specific_use()
print(m.wheel)
print(m.has_roof)

# I'm a motorcycle.
# general use: transportation.
# specific use: 1. hit the road; 2. racing.
# 2
# False

print('------------------------------------------')

class Animal: 
    def __init__(self, habitat):
        self.habitat = habitat
    def print_habitat(self):
        print(self.habitat)
    def sound(self):
        print('Some animal sound.')

class Dog(Animal):
    def __init__(self, habitat):
        super().__init__(habitat) # call the super class constructor
    def sound(self):
        print('Woof! Woof!')

d = Dog('land')
d.print_habitat()
d.sound()



# class Animal: 
#     def __int__(self, habitat):
#         self.habitat = habitat
#     def print_habitat(self):
#         print(self.habitat)
#     def sound(self):
#         print('Some animal sound.')

# class Dog(Animal):
#     def __int__(self):
#         super().__init__('land') # Attribute ERROR! # super() is a function that calls the parent class constructor.
#         print('I am a dog.')
#     def sound(self):
#         print('Woof!')

# class Cat(Animal):
#     def __int__(self):
#         super().__init__('land')
#         print('I am a cat.')
#     def sound(self):
#         print('Meow!')

# class Bird(Animal):
#     def __int__(self):
#         super().__init__('air')
#         print('I am a bird.')
#     def sound(self):
#         print('Chirp!')

# class Fish(Animal):
#     def __int__(self):
#         super().__init__('water')
#         print('I am a fish.')
#     def sound(self):
#         print('Splash!')

# try:
#     d = Dog()    
#     d.print_habitat()
#     d.sound()
#     c = Cat()
#     c.print_habitat()
#     c.sound()
#     b = Bird()
#     b.print_habitat()
#     b.sound()
#     f = Fish()
#     f.print_habitat()
#     f.sound()

# except Exception as e:
#     print(e)