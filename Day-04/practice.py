import sys

class EmptyClass:
    pass

class Animal:
    def __init__(self, name):
        self.name = name 
    def info(self):
        print(f'the name of the animal is: {self.name}')
        return self.name

dog = Animal("dog")
print(dog.info() + "\n")
print(sys.getsizeof(EmptyClass))
print(sys.getsizeof(dog))
print(sys.getsizeof(Animal))

# Encapsulation in python

class Person: 
    __balance = 0 

    def __init__(self, name, balance):
        self.name = name,
        self.__balance = balance

    def deposit(self,amount):
        if(amount > 0 ):
            self.__balance += amount
            print(f'Deposited: {amount}, to {self.name} New Balance: {self.__balance}')
        else:
            print('Invalid amount')

    def withdraw(self, amount):
        if(amount > self.__balance):
            print('Insufficient funds')
            return self.__balance
        else:
            self.__balance -= amount
            print(f'Withdrawn: {amount}, New Balance: {self.__balance}')
            return self.__balance
    
    def get_balance(self):
        return self.__balance
    

myaccount = Person("haris", 1000)

print(myaccount.get_balance())
myaccount.deposit(500)
myaccount.withdraw(1000000) 
print(myaccount.get_balance())


# Inheritance in python
# single inheritance
class Student:
    def __init__(this, name, age):
        this.name = name, 
        this.age = age
    
class Marks(Student):
    def __init__(this, name, age,marks):
        super().__init__(name, age)
        this.marks = marks
    def student_info(this):
        print(f'Student Name: {this.name}, Age: {this.age}, Marks: {this.marks}')

student_one = Marks("mukul", 20, 1e9+7 )
student_one.student_info()

# multiple inheritance

class Flyer:
    def fly(self):
        return "Flying high..."

class Swimmer:
    def swim(self):
        return "Swimming deep..."

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack..."

donald = Duck()
print(donald.fly())    # Flying high!
print(donald.swim())   # Swimming deep!
print(donald.quack())  # Quack!


# polymorphism in python
# method overloading
class Calculatr:
    def multiply(self, a = 1, b = 1, *args):
        result = a * b
        for value in args:
            result *= value
        return result
    
calc = Calculatr()
print (calc.multiply())
print (calc.multiply(4))
print (calc.multiply(2,3))
print (calc.multiply(2,3,4,5))

# method overriding
class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"


animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())


import logging

# 1. Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# 2. Create a handler (File)
file_handler = logging.FileHandler("app_debug.log")

# 3. Create a formatter
formatter = logging.Formatter('%(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 4. Add handler to logger
logger.addHandler(file_handler)

# Use it
logger.info("The application has started successfully.")
logger.error("Could not connect to the database!")



