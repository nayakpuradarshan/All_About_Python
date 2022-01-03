
# Oops concept
# Class : Class is a blueprint of creating a new objects.
# Object : An object is simply a collection of data (variables) and methods (functions) that act on those data.






# Polymorphism
# Poly Means many and morph means form that means manyform (One think can take many form!)

# Types of Polymorphism
# 1) Duck typing    2) Operation Overloading 3) Method Overloading 4) Method Overriding


# 1) Duck Typing And Dynamic Typing

# check the execute method which we have provided in the PyCharm and MyCharm both class
# it's doen't matter that we have decide to define it into the any class this is the duck typing.

'''
class PyCharm:

    # it's a duck 
    def execute(self):
        print("Compiling")
        print("Running")

class MyCharm:

    # it a duck
    def execute(self):
        print("Spell Check")
        print("Velidation Check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self, ide):
        ide.execute()

Type_IDE = MyCharm()

lap1 = Laptop()
lap1.code(Type_IDE)
'''


# Operator Overloading in Polymorphism

# In general we have __add__() method in the python
# And when i try to add s1 with s2 object it's not allow me to do that
# Because python knows what is __add__() method and how it's work but my Student class don't know
# So i have added __add_() method in the my Student class which is known as Operation Overloading

"""
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        total = Student(m1, m2)
        return total



s1 = Student(58, 69)
s2 = Student(60, 65)

total = s1 + s2

print(total.m2)
"""

# Method overloading and Method Overriding

# Method Overloading : If you have a class and in that class if you have two methods with the same name or
# Arguments or parameters it called method overloading.
"""
EX :

class Student:
    def average(a, b):
        pass
    def average(a, b, c):
        pass
"""

"""
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a + b+ c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a

        return s


s1 = Student(58, 69)
print(s1.sum(5, 9))
"""

# Method Overriding : You have two methods with the same name and same number of parameter or arguments it's
# called method overriding.

"""
class A:

    def show(self):
        print("In A show")

class B(A):

    def show(self):
        print("In B show")

a1 = B()
a1.show()
"""




# creating a class and object
# Attributes > Variable
# Behaviour > Methods (Function)

"""
# Constructor in inheritance and MRO(Method resolution order)
class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1 working!")

    def feature2(self):
        print("feature 2 working!")

class B():

    def __init__(self):
        # super().__init__() This will print super class
        print("In B init")

    def feature3(self):
        print("Feature 3 working!")

    def feature4(self):
        print("feature 4 working!")

class C(A, B):

    def __init__(self):
        super().__init__()
        super().__init__()
        print("In C init")


a2 = C()
"""







# Inheritance
# Type of inheritance : 1) Single Level 2) Multiple Inheritance 3) MultiLevel Inheritance

"""
# Single Level
class A:
    def feature1(self):
        print("Feature 1 working!")

    def feature2(self):
        print("feature 2 working!")

class B(A):
    def feature3(self):
        print("Feature 3 working!")

    def feature4(self):
        print("feature 4 working!")
"""

"""
# Miltilevel Inheritance
class A:
    def feature1(self):
        print("Feature 1 working!")

    def feature2(self):
        print("feature 2 working!")

class B(A):
    def feature3(self):
        print("Feature 3 working!")

    def feature4(self):
        print("feature 4 working!")

class C(B):
    def feature5(self):
        print("Feature 5 working!")

    def feature6(self):
        print("feature 6 working!")
"""

"""
# Miltiple Inheritance
class A:
    def feature1(self):
        print("Feature 1 working!")

    def feature2(self):
        print("feature 2 working!")

class B():
    def feature3(self):
        print("Feature 3 working!")

    def feature4(self):
        print("feature 4 working!")

class C(A, B):
    def feature5(self):
        print("Feature 5 working!")

    def feature6(self):
        print("feature 6 working!")
"""







"""
# Inner class in python
class Student():

    #Consturctor
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    #Method
    def show(self):
        return print(s1.name, s1.rollno)

    class Laptop():

        def __init__(self, brand, ram, cpu):
            self.brand = brand
            self.ram = ram
            self.cpu = cpu

        def show2(self):
            print(lap1.brand, lap1.ram, lap1.cpu)

s1 = Student("Darshan", 12)
s1.show()

lap1 = Student.Laptop("HP", "8GB", "i5")
lap1.show2()
"""








'''
# Types of methods in python
# 1) instance 2) class 3) static

# Types of the instance methods
# 1)Accessor Methods 2) Mutators Methods
class Student:

    # static variable
    school = "telusko"

    # Constructor
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # method (average)
    def average(self):
        return (self.m1 + self.m2 + self.m3)/3

    # getters(accecers) (it's get the values)
    def get_m1(self):
        return self.m1

    # setters(mutators) (it's set the values)
    def set_m1(self, value):
        self.m1 = value

    # class method
    @classmethod    # Decorator
    def info(cls):
        return cls.school

    # Static method
    @staticmethod
    def data():
        print("Hey, i am a robot here!")



# crating variabel and assign value to it
s1 = Student(34, 67, 32)
s2 = Student(22, 32, 12)

# Calling a class method
print(Student.info())

# Calling a static method
Student.data()

# printing values of the s1 and s2
print("average of the s1 is ",s1.average())
print("average of the s2 is ",s2.average())
'''







'''
# Types of variable !) Instance 2) static(class)
class Car:

    wheels = 2.2            # class variabel

    def __init__(self):
        self.mil = 10       # Instance variable
        self.com = "BMW"    # Instance variable


cus1 = Car()
cus2 = Car()

Car.wheels = 3.3            # changing the value of the static variabel(class variabel)


cus2.mil = 7                # Changing the value of the instance variabel


print(cus1.mil, cus1.com, cus1.wheels)
print(cus2.mil, cus2.com, cus2.wheels)
'''



# Computer class to understand init and objects
# create variabel inside of the object
'''
class Computer:

    # __init__ method is called it self
    def __init__(self):
        self.name = "Darshan"
        self.age = 25

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == self.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

c2.age = 30

if c1.compare(c2):
    print("They are same !")

print("Your name is", c1.name)
print("Your age is", c1.age)
'''



'''
class Computer:

    def config(self):
        print("i5, 16gb, 1TB")


com1 = Computer()

# Actual Sintax
Computer.config(com1)
# People use this sintax
com1.config()
'''

# Constructor or __init__ method in class

'''
class Computer:

    # Over Constructor
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(f"Your computers cpu is {self.cpu} and ram is {self.ram}")

com1 = Computer("i5", 16)
com2 = Computer("Ryzen 5", 8)

com1.config()
'''

# crate a class inside the other class

'''
class Cdvector:
    pass

class Threedvector(Cdvector):
    pass
'''

# guess the special number number

'''
class Employee:
    def __init__(self, name):
        self.name = name

E1=Employee("abc")
print(E1.name)
'''