#############################
# 1 #  Python Indentations
#############################

print("Hello, World!")  # O/P : Hello, World!

if 5 > 2:
    print("Five is greater than two!")  # O/P : Five is greater than two!

"""         

if 5 > 2:
print("Five is greater than two!")

O/P :

It will give error
File "Hello.py", line 13
    print("Five is greater than two!")
        ^
IndentationError: expected an indented block

"""

#############################
# 2 #   Creating Variables :
#           - A variable name must start with a letter(upper or lower case) or the underscore character
#           - A variable name cannot start with a number
#           - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#           - Variable names are case-sensitive (age, Age and AGE are three different variables)
#           - Variable names preferably should use Camel casing
#                 e.g. daysInYear, daysInMonth
#           - Datatypes :
#                -  integers (numbers),
#                -  floating point numbers,
#                -  complex numbers (imaginary)
#                -  booleans (true or false) and
#                -  strings (text).
#############################

x = 5
y = "John"
print(x)  # O/P = 5
print(y)  # O/P = John

# x is of type int
x = "Sally"  # x is now of type str
print(x)  # O/P = Sally

#############################
# 3 #    Output Variables
#############################

x = "Python is"
y = "awesome"
print("I just want to say" + x + y)  # O/P = I just want to sayPython isawesome
print("I just want to say " + x + " " + y)  # O/P = I just want to say Python is awesome

a = 3
b = 4
print(a + b)  # O/P = 7

# print(x+a)       #  It will throw error


#############################
# 4 #   Python Numbers :
#           int     : Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
#           float   : Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#           complex : Complex numbers are written with a "j" as the imaginary part:
#############################

# int
x = 1
y = 35656222554887711
z = -3255522

# float   # Float can also be scientific numbers with an "e" to indicate the power of 10.
p = 1.0
q = 1.41
r = -35.59

s = 35e3
t = 12E4
u = -87.7e100

# complex <real part + imaginary part>
l = 1j
m = 3 + 5j
n = -5j

# To verify the type of any object in Python, use the type() function:
print(type(x))  # O/P : <class 'int'>
print(type(p))  # O/P : <class 'float'>
print(type(m))  # O/P : <class 'complex'>

# multiple initialization :
a, b, c, d = 1, 2, 3, 4
x, y, z = 1, 4.8, "Hi"
print(x, y, z)  # O/P : 1 4.8 Hi

#############################
# 5 #    Python Casting
#           int()   -   constructs an integer number from an integer literal, a float literal
#                       (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
#           float() -   constructs a float number from an integer literal, a float literal or a string literal
#                       (providing the string represents a float or an integer)
#           str()   -   constructs a string from a wide variety of data types, including strings, integer literals and float literals
#############################

x = int(1)  # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

x = float(1)  # x will be 1.0
y = float(2.8)  # y will be 2.8
z = float("3")  # z will be 3.0
w = float("4.2")  # w will be 4.2

x = str("s1")  # x will be 's1'
y = str(2)  # y will be '2'
z = str(3.0)  # z will be '3.0'

#############################
# 6 #    Python Strings
#############################

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])  # O/P : e

# Substring. Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])  # O/P : llo

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())  # # O/P : "Hello, World!"

# The len() method returns the length of a string:
a = "Hello, World!"
print(len(a))  # O/P : 13

# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())  # O/P : hello, world!

# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())  # O/P : HELLO, WORLD!

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))  # O/P : Jello, World!

b = "Hello, World!"
print(b.replace("World", "Universe"))  # O/P : Hello, Universe!

s = "Hello World World World"
s = s.replace("World", "Universe", 1)  # The parameter (1) indicates that the string should be replaced only once.
print(s)  # O/P : Hello Universe World World

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))  # O/P :  ['Hello', ' World!']

# splitting word into characters
word = "Easy"
x = list(word)
print(x)  # O/P : ['E', 'a', 's', 'y']

# The find() method returns index if word s found else -1
s = "That I ever did see. Dusty as the handle on the door"
index = s.find("Dusty")
print(index)  # O/P : 21

index = s.find("Dusty", 0, 15)  # You can add optional starting index and end index: find(query, start, end)
print(index)  # O/P : -1

# "in" keyword
if "Dusty" in s:
    print("Word found")  # O/P : Word found

###
#   Command-line String Input
###

print("Enter your name:")
x = input()
print("Hello, ", x)

# O/P : Enter your name: <John>
#       Hello,   John

num = input('Give me a number? ')
print('You said: ' + str(num))

# O/P : Give me a number? <7>
#       You said: 7

###
#   Print Formatting
###

# Combine numbers and text
s = "My lucky number is %d, what is yours?" % 7
print(s)  # O/P : My lucky number is 7, what is yours?

s = "My lucky number is %f, what is yours?" % 7.7
print(s)  # O/P : My lucky number is 7.700000, what is yours?

# alternative method of combining numbers and text
s = "My lucky number is " + str(7) + ", what is yours?"
print(s)  # O/P : My lucky number is 7, what is yours?

# join
firstName = "Sachin"
lastName = "Tendulkar"

sequence = (firstName, lastName)  # defining sequence
fullName = " ".join(sequence)
print(fullName)  # O/P : Sachin Tendulkar

words = ["How", "are", "you", "doing", "?"]
sentence = ' '.join(words)
print(sentence)  # O/P : How are you doing ?

#############################
# 7 #    Python Operators
#               Arithmetic operators
#               Assignment operators
#               Comparison operators
#               Logical operators
#               Identity operators
#               Membership operators
#               Bitwise operators
#               Ternary operators
#############################

###
#   Arithmetic operators
###

x = 4
y = 7

print(x + y)  # O/P : 11
print(x - y)  # O/P : -3
print(y - x)  # O/P : 3
print(x * y)  # O/P : 28
print(x / y)  # O/P : 0.5714285714285714
print(x % y)  # O/P : 4
print(y % x)  # O/P : 3
print(x ** y)  # O/P : 16384     ( Exponentiation : x to the power y )
print(x // y)  # O/P : 0         ( Floor Division : x/y and prints quotient part )
print(y // x)  # O/P : 1

###
#   Assignment operators
###

x = 5
print(x)  # O/P : 5

x += 3  # x = x+3
print(x)  # O/P : 8

x -= 3  # x = x - 3
print(x)  # O/P : 5

x *= 3  # x = x * 3
print(x)  # O/P : 15

x /= 5  # x = x / 3
print(x)  # O/P : 3.0

x %= 3  # x = x % 3
print(x)  # O/P : 0.0

x = 15
x //= 3  # x = x // 3
print(x)  # O/P : 5

x **= 3  # x = x ** 3
print(x)  # O/P : 125

###
#   Comparison Operators
#
#       ==	    Equal	                    x == y
#       !=	    Not equal	                x != y
#       >	    Greater than	            x > y
#       <	    Less than	                x < y
#       >=	    Greater than or equal to	x >= y
#       <=	    Less than or equal to	    x <= y
###

a = 4
b = 5
print(a == b)  # O/P : False
print(a != b)  # O/P : True
print(a > b)  # O/P : False
print(a < b)  # O/P : True
print(a >= b)  # O/P : False
print(a <= b)  # O/P : True

###
#   Logical Operators
#
#       and   :	 Returns True if both statements are true	                x < 5 and  x < 10
#       or	  :  Returns True if one of the statements is true	            x < 5 or x < 4
#       not	  :  Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
###

p = 2
q = 3
r = 4

print((p < q) and (q < r))  # O/P : True
print(not (p < q) and (q < r))  # O/P : False
print((p < q) or (q < r))  # O/P : True

###
#   Identity Operators
#
#        is 	:   Returns true if both variables are the same object	        x is y
#        is not	:   Returns true if both variables are not the same object	    x is not y
###

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)  # O/P :  True   (because z is the same object as x)

print(x is y)  # O/P :  False  (because x is not the same object as y, even if they have thew same content)

# to demonstrate the difference betweeen "is" and "==":
print(x == y)  # O/P :  True   (because x is equal to y, but not the same object)
print(x == z)  # O/P :  True

###
#    Membership Operators
#
#        in 	:   Returns True if a sequence with the specified value is present in the object	        x in y
#        not in	:   Returns True if a sequence with the specified value is not present in the object	    x not in y
###

x = ["apple", "banana"]

print("banana" in x)  # O/P :  True   (because a sequence with the value "banana" is in the list)
print("banana" not in x)  # O/P :  False  (because a sequence with the value "banana" is not in the list)

###
#    Bitwise Operators : Bitwise operators are used to compare (binary) numbers:
#
#       & 	    AND	                    Sets each bit to 1 if both bits are 1
#       |	    OR	                    Sets each bit to 1 if one of two bits is 1
#       ^	    XOR	                    Sets each bit to 1 if only one of two bits is 1
#       ~ 	    NOT	                    Inverts all the bits
#       <<	    Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
#       >>	    Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
###

x = 125

# AND
x &= 10  # x = x & 10
print(x)  # O/P : 8

"""
          128 64  32  16  8 4 2 1
 x = 125  0   1   1   1   1 1 0 1     = 0111  1101
 y = 10   0   0   0   0   1 0 1 0     = 0000  1010

 x&y                                  = 0000  1000  = 8

"""

# OR

x = 125
x |= 10  # x = x | 10
print(x)  # O/P : 127

"""
          128 64  32  16  8 4 2 1
 x = 125  0   1   1   1   1 1 0 1     = 0111  1101
 y = 10   0   0   0   0   1 0 1 0     = 0000  1010

 x|y                                  = 0111  1111  = 127

"""

#  XOR

x = 125
x ^= 10  # x = x ^ 10
print(x)  # O/P : 119

"""
                128 64  32  16  8 4 2 1
 x = 0X 125     0   1   1   1   1 1 0 1  = 0111  1101
 y = 0X 10      0   0   0   0   1 0 1 0  = 0000  1010

 x|y                                     = 0111  0111  = 119

"""
print("------------")
# Zero fill left shift
x = 60
x <<= 2  # x = x << 2
print(x)  # O/P : 240

"""
                128 64  32  16  8 4 2 1
 x =    125  =  0   0   1   1   1 1 0 0  = 0011  1100
 
x<<2            1   1   1   1   0 0 0 0  = 1111  0000  = 240
                                     
"""

# Signed right shift
x = 60
x >>= 2  # x = x >> 2
print(x)  # O/P : 15

"""
                128 64  32  16  8 4 2 1
 x =    125  =  0   0   1   1   1 1 0 0  = 0011  1100
 
x<<2            0   0   0   0   1 1 1 1  = 0000 1111 = 15

"""

###
#    Ternary Operators : [on_true] if [expression] else [on_false]
###

a = 4
b = 7

op1 = "a" if a > b else "b"
op2 = "a" if a < b else "b"

print(op1)  # O/P : b
print(op2)  # O/P : a

# nested ternary
a = -0.7
b = 0.7
c = 7

op3 = "Less than zero" if a < 0 else "Between 0 and 1" if a >= 0 and a <= 1 else "Greater than one"
op4 = "Less than zero" if b < 0 else "Between 0 and 1" if b >= 0 and b <= 1 else "Greater than one"
op5 = "Less than zero" if c < 0 else "Between 0 and 1" if c >= 0 and c <= 1 else "Greater than one"

print(op3)  # O/P : Less than zero
print(op4)  # O/P : Between 0 and 1
print(op5)  # O/P : Greater than one

#############################
# 8 #    If ... Else
#
#############################

a = 33
b = 200

"""
if b > a:
print("b is greater than a")        # you will get an error

# If statement, without indentation (will raise an error):
"""

if b > a:
    print("b is greater than a")

# O/P :   b is greater than a

# Elif : "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# O/P : a and b are equal

# Else : It catches anything which isn't caught by the preceding conditions.

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# O/P : a is greater than b

# You can also have an else without the elif:

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# O/P :   b is not greater than a

# Short Hand If
if a > b: print("a is greater than b")  # O/P : a is greater than b

# Short Hand If ... Else
print("A") if a > b else print("B")  # O/P : A

print("A") if a > b else print("=") if a == b else print("B")
# O/P : A

# And : It's a logical operator, and is used to combine conditional statements:
a = 1
b = 2
c = 3
if a > b and c > a:
    print("Both conditions are True")
else:
    print("Both conditions are not True")

# O/P : Both conditions are not True

# Or : It's a logical operator, and is used to combine conditional statements:
if a > b or a < c:
    print("At least one of the conditions is True")

    # O/P :   At least one of the conditions is True

#############################
# 9 #    While Loops
#
#############################


# Print i as long as i is less than 6:

i = 1
while i < 6:
    print(i)
    i += 1  # Note: remember to increment i, or else the loop will continue forever.

"""
# O/P :

1
2
3
4
5

"""

# break Statement : With the break statement we can stop the loop even if the while condition is true:

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

"""
# O/P :
1
2
3

"""

# The continue Statement : With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

"""
# O/P :

1
2
4
5
6
"""
##############################
# 10 #    For Loops
#               It is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
##############################


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

"""
# O/P :
apple
banana
cherry
"""

Numbers = [1, 2, 3, 4, 5]
for x in Numbers:
    print(x)

"""
# O/P :
1
2
3
4
5
"""

for x in "banana":
    print(x)

"""
# O/P :
b
a
n
a
n
a
"""

# break Statement : With the break statement we can stop the loop before it has looped through all the items:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

"""
# O/P : 
apple
banana
"""

# The continue Statement : With the continue statement we can stop the current iteration of the loop, and continue with the next:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

"""
# O/P :
apple
cherry
"""

# The range() Function : The range() function returns a sequence of numbers,
#                         starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):  # It is not the values of 0 to 6, but the values 0 to 5.
    print(x)

"""
# O/P :
0
1
2
3
4
5
"""

for x in range(2, 6):  # values from 2 to 6 (but not including 6):
    print(x)

"""
# O/P :
2
3
4
5
"""

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value
# by adding a third parameter: range(2, 30, 3):

for x in range(2, 30, 3):  # Increment the sequence with 3 (default is 1):
    print(x)

"""
# O/P :
2
5
8
11
14
17
20
23
26
29
"""

# Else in For Loop :  The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# e.g.  Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

"""
# O/P :
0
1
2
3
4
5
Finally finished!
"""

#############################
# 11 #    Nested Loops
#
#############################

# The "inner loop" will be executed one time for each iteration of the "outer loop":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

"""
# O/P :
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
"""
