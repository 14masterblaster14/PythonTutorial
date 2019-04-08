#############################
# 1 #    Class :
#                - No protected and private variables, but can define
#                      protected with _x
#                      private with __x
#                - variables don't have limits
#############################


class MyClass:
    x = 5  # property

    def display(self, object_name):  # methods , It has first parameter as self
        print("This is display method, called by ", object_name)

    # Static Method :
    @staticmethod
    def static_method():
        x = 1  # We can't change property at class level,compiler will ignore it. We can change in local scope.
        print("This ia static method")
        print("Value of x :- ", x)

    # Class Method (Decorator):
    @classmethod
    def class_method(cls):
        print("This ia class method")
        cls.x = 2  # We can change class property.
        print("Value of x :- ", cls.x)


# Object:

object1 = MyClass()
print(" Accessing  property :- ", object1.x)
print(" Accessing method :- ")
object1.display("object1")

# You can access it with class and need not to create object for it, but can access with object as well
MyClass.static_method()
object1.static_method()
print(object1.x)

#  A class method is a method that’s shared among all objects.
#  To call a class method, put the class as the first argument.
#  You can use class method with both objects and the class.
#  But you cannot change the property with object as it belongs to the class and can be changed with class only
object1.class_method()
MyClass.class_method()
print(object1.x)

print("----------------------")
print(object1.x)  # 2
print(MyClass.x)  # 2

object1.x = 7
print(object1.x)  # 7
print(MyClass.x)  # 2

MyClass.x = 9
print(object1.x)  # 7
print(MyClass.x)  # 9

# e.g. class method and static method

from datetime import date


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # a class method to create a Person object by birth year.

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

        # a static method to check if a Person is adult or not.

    @staticmethod
    def isAdult(age):
        return age > 18


animal1 = Animal('mayank', 21)
animal2 = Animal.fromBirthYear('mayank', 1996)

print("Animal1 age : ", animal1.age)
print("Animal2 age : ", animal2.age)

# print the result
print(Animal.isAdult(22))


#
#  The __init__() Function :
#                              It is called automatically every time the class is being used to create a new object.
#

class Person:
    def __init__(self, name, age):  # The self / anyname parameter is a reference to the class instance itself,
        # and it is used to access variables that belongs to the class.
        self.userId = name + "" + "7"
        self.userPassword = "None"
        self.name = name
        self.age = age
        self.person_function()

    def person_function(self):
        print("Hello my name is : " + self.name)

    def setPassword(self, password):
        self.userPassword = password

    def getPassword(self):
        return self.userPassword


person = Person("Saurav", 47)
print(person.userId)
print(person.name)
print(person.age)

person.setPassword("$pswd")
print(person.getPassword())

person.age = 50  # Modify Object Properties
print(person.age)

del person.age  # Delete Object Properties
# print(person.age)

del person  # Delete Objects


#############################
# a #    Inheritance
#############################

# Parent Class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("Person Name is - " + self.firstname, self.lastname)

    def printAddress(self, city):
        print("Persons city is - " + city)


# Use the Person class to create an object, and then execute the printname method:
x = Person("Sachin", "Tendulkar")
x.printname()


# Child Class

class Student(Person):
    pass  # Use the pass keyword when you do not want to add any other properties or methods to the class.


y = Student("Saurav", "Ganguly")
y.printname()


class Employee(Person):
    # When you add the __init__() funcion, the child class will no longer inherit the parent's __init__() function.
    # The child's __init__() function overrides the inheritance of the parent's __init__() function.
    def __init__(self, fname, lname, age):
        # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
        # Person.__init__(self, fname, lname)
        # self.employee_firstname = fname
        # self.employee_lastname = lname

        super().__init__(fname, lname)
        self.employee_age = age
        self.graduationyear = 2019

    def welcomenote(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

    def printHobby(self):
        print("He is interested in Cricket :) ")

    def printname(self):  # Method Overriding
        print("Employee Name is - " + self.firstname, self.lastname)


"""
# Method Overloading, but python doesn't support

    def printAddress(self, city, pincode):          
        print("Persons city is - " + city)
        print("Persons city pincode is - " + pincode)
"""

z = Employee("Veeru", "Sehwag", "52")
z.welcomenote()
z.printHobby()
z.printname()


# Multiple Inheritance

class Abc:

    def __init__(self, _a):
        self.a = _a

    b = None
    c = 21

    def abcDispplay(self):
        print("Display ABC")


class Def:

    def __init__(self, _d):
        self.d = _d

    e = None
    f = 14

    def defDispplay(self):
        print("Display DEF")


class Xyz(Abc, Def):

    def __init__(self, _a, _d, _x):
        self.x = _x
        Abc.__init__(self, _a)
        Def.__init__(self, _d)

    def xyzDisplay(self):
        print("Display XYZ")


myObject = Xyz(1, 2, 3)

print("a = ", myObject.a)
print("b = ", myObject.b)
print("c = ", myObject.c)
myObject.abcDispplay()

print("d = ", myObject.d)
print("e = ", myObject.e)
print("f = ", myObject.f)
myObject.defDispplay()

print("x = ", myObject.x)
myObject.xyzDisplay()


# e.g.

class Person:
    # defining constructor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

        # defining class methods

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)

        # end of class definition


# defining another class
class Student:  # Person is the
    def __init__(self, studentId):
        self.studentId = studentId

    def getId(self):
        return self.studentId


class Resident(Person, Student):  # extends both Person and Student class
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        Student.__init__(self, id)
        # super().__init__(personName, personAge)

    # Create an object of the subclass


resident1 = Resident('John', 30, '102')
resident1.showName()
print(resident1.getId())


# Multilevel Inheritance

class Pqr:

    def __init__(self, _p):
        self.p = _p

    _q = None
    __r = 21

    def pqrDispplay(self):
        print("Display PQR")


class Stu(Pqr):

    def __init__(self, _s, _p):
        super().__init__(_p)
        self.s = _s

    _t = None
    __u = 14

    def stuDispplay(self):
        print("Display STU")


class Vw(Stu):

    def __init__(self, _v, _s, _p):
        super().__init__(_s, _p)
        self.v = _v

    def vwDisplay(self):
        print("Display VW")


myObject = Vw(1, 2, 3)
myObject.vwDisplay()
print("v - ", myObject.v)

myObject.pqrDispplay()
print("p - ", myObject.p)
print("_q - ", myObject._q)
# print("__r - ", myObject.__r)           # Can't access private variable

myObject.stuDispplay()
print("s - ", myObject.s)
print("_t - ", myObject._t)
# print("__u - ", myObject.__u)           # Can't access private variable
