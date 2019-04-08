#############################
# 1 #    Functions
#############################

# Creating a Function :

def my_function1():
    print("Hello from a function")


my_function1()  # Calling the function


# with parameter

def my_function(fname):
    print(" Indian Team : " + fname)


my_function("Saurav")
my_function("Sachin")
my_function("Yuvaraj")


# Default Parameter Value

def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Return Values

def my_function(x):
    return 5 * x


z = my_function(3)
print(z)

print(my_function(3))
print(my_function(5))
print(my_function(9))


def getPerson():
    name = "Sachin"
    age = "45"
    country = "India"
    return name, age, country


personName, personAge, personCountry = getPerson()

print(personName)
print(personAge)
print(personCountry)


#############################
# 2 #    Recursion :
#                    It means a defined function can call itself.
#############################


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

""" 
O/P :
Recursion Example Results
1
3
6
10
15
21
"""

"""

def tri_recursion(k):
  if(k>0):
    result = k + tri_recursion(k+1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

------------------------------------------

o/p : 

Recursion Example Results
Traceback (most recent call last):
  File "D:/DESKTOP/python/Functions.py", line 70, in <module>
    tri_recursion(6)
  File "D:/DESKTOP/python/Functions.py", line 63, in tri_recursion
    result = k + tri_recursion(k+1)
  File "D:/DESKTOP/python/Functions.py", line 63, in tri_recursion
    result = k + tri_recursion(k+1)
  File "D:/DESKTOP/python/Functions.py", line 63, in tri_recursion
    result = k + tri_recursion(k+1)
  [Previous line repeated 995 more times]
  File "D:/DESKTOP/python/Functions.py", line 62, in tri_recursion
    if(k>0):
RecursionError: maximum recursion depth exceeded in comparison

"""

#############################
# 3 #    Lambda Function :
#                    It means a defined function can call itself.
#                    A lambda function is a small anonymous function.
#                    A lambda function can take any number of arguments, but can only have one expression.
#                    Use lambda functions when an anonymous function is required for a short period of time.
#############################

# Syntax :    lambda arguments : expression

x = lambda a: a + 10
print(x(5))  # O/P : 15

x = lambda a, b: a * b
print(x(5, 6))  # O/P : 30

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))  # O/P : 13


# Usages:

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))  # O/P : 22
print(mytripler(11))  # O/P : 33
