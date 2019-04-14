#############################
#
# 21# Try Except :
#                   -   The try block lets you test a block of code for errors.
#                   -   The except block lets you handle the error.
#                   -   The finally block lets you execute code, regardless of the result
#                       of the try- and except blocks.
#############################


try:
    print(7 / 2)
except:
    print("An exception occurred")

# O/P : 3.5

try:
    print(7 / 0)
except:
    print("An exception occurred")

# O/P : An exception occurred

try:
    print(x / y)
except ArgError:
    print("Invalid Devider value")
except:
    print("An exception occurred")

"""
Till now O/P :

Traceback (most recent call last):
  File "D:/DESKTOP/python/Tryexception.py", line 25, in <module>
    print(x / y)
NameError: name 'x' is not defined

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:/DESKTOP/python/Tryexception.py", line 26, in <module>
    except ArgError:
NameError: name 'ArgError' is not defined

3.5
An exception occurred

Process finished with exit code 1

"""
