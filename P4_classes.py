#############################
# 14 #    Class :
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
        x = 1   # We can't change property at class level,compiler will ignore it.
                # We can change in local scope.
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
print(" Accessing  property :- ", object1.x)  # O/P :  Accessing  property :-  5
print(" Accessing method :- ")
object1.display("object1")
#                        O/P :  Accessing method :-
#                               This is display method, called by  object1

# You can access it with class and need not to create object for it, but can access with object as well.
MyClass.static_method()
#                        O/P :  This ia static method
#                               Value of x :-  1
object1.static_method()
#                        O/P :  This ia static method
#                               Value of x :-  1
print(object1.x)  # O/P : 5

#  A class method is a method that’s shared among all objects.
#  To call a class method, put the class as the first argument.
#  You can use class method with both objects and the class.
#  But you cannot change the property with object as it belongs to the class
#  and can be changed with class only

object1.class_method()
#                       O/P :   This ia class method
#                               Value of x :-  2
MyClass.class_method()
#                       O/P :   This ia class method
#                               Value of x :-  2
print(object1.x)  # O/P : 2

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

print("Animal1 age : ", animal1.age)  # O/P : Animal1 age :  21
print("Animal2 age : ", animal2.age)  # O/P : Animal2 age :  23

# print the result
print(Animal.isAdult(22))  # True

#
#  The __init__() Function :
#               It is called automatically every time the class is being used to create a new object.
#

class Person:
    def __init__(self, name, age):
        # The self / anyname parameter is a reference to the class instance itself,
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

person = Person("Saurav", 47)  # O/P : Hello my name is : Saurav
print(person.userId)  # O/P : Saurav7
print(person.name)  # O/P : Saurav
print(person.age)  # O/P : 47

person.setPassword("$pswd")
print(person.getPassword())  # O/P : $pswd

person.age = 50  # Modify Object Properties
print(person.age)  # O/P : 50

del person.age  # Delete Object Properties
# print(person.age)

del person  # Delete Objects

#############################
# a #    Inheritance
#############################

##
# Parent Class
##
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
x.printname()  # O/P : Person Name is - Sachin Tendulkar


##
# Child Class
##

class Student(Person):
    pass
    # Use the pass keyword when you do not want to add any other properties or methods to the class.

y = Student("Saurav", "Ganguly")
y.printname()  # O/P : Person Name is - Saurav Ganguly


class Employee(Person):
    # When you add the __init__() funcion, the child class will no longer inherit
    # the parent's __init__() function.
    # The child's __init__() function overrides the inheritance of the parent's __init__() function.
    def __init__(self, fname, lname, age):
        # To keep the inheritance of the parent's __init__() function,
        # add a call to the parent's __init__() function:
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
z.welcomenote()  # O/P : Welcome Veeru Sehwag to the class of 2019
z.printHobby()  # O/P : He is interested in Cricket :)
z.printname()  # O/P : Employee Name is - Veeru Sehwag


##
# Multiple Inheritance
##

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

print("a = ", myObject.a)  # O/P : 1
print("b = ", myObject.b)  # O/P : None
print("c = ", myObject.c)  # O/P : 21
myObject.abcDispplay()  # O/P : Display ABC

print("d = ", myObject.d)  # O/P : 2
print("e = ", myObject.e)  # O/P : None
print("f = ", myObject.f)  # O/P : 14
myObject.defDispplay()  # O/P : Display DEF

print("x = ", myObject.x)  # O/P : x = 3
myObject.xyzDisplay()  # O/P : Display XYZ

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
resident1.showName()  # O/P : John
print(resident1.getId())  # O/P : 102


##
# Multilevel Inheritance
##
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
myObject.vwDisplay()        # O/P : Display VW
print("v - ", myObject.v)   # O/P : v -  1

myObject.pqrDispplay()      # O/P : Display PQR
print("p - ", myObject.p)   # O/P : p -  3
print("_q - ", myObject._q)         # O/P : _q -  None
# print("__r - ", myObject.__r)     # Can't access private variable

myObject.stuDispplay()          # O/P : Display STU
print("s - ", myObject.s)       # O/P : s -  2
print("_t - ", myObject._t)  # O/P : _t -  None
# print("__u - ", myObject.__u)     # Can't access private variable
