#############################
# 15 # Iterators :
#                   -   Iterator is an object that contains a countable number of values.
#                   -   Iterator implements the iterator protocol,
#                       which consist of the methods iter__() and __next__().
#
#    # Iterables :
#                   -   Lists, tuples, dictionaries, and sets are all iterable objects.
#                   -   They are iterable containers which you can get an iterator from.
#                   -   All these objects have a iter() method which is used to get an iterator:
#
#############################

my_tuple = ("Apple", "Dell", "IBM")
my_iter = iter(my_tuple)

print(next(my_iter))  # Apple
print(next(my_iter))  # Dell
print(next(my_iter))  # IBM

"""
 print(next(my_iter))        # Error

O/P :

Traceback (most recent call last):
  File "D:/DESKTOP/python/Iterators.py", line 19, in <module>
    print(next(my_iter))
StopIteration
"""

my_string = "India"  # String
my_iter = iter(my_string)

print(next(my_iter))  # I
print(next(my_iter))  # n
print(next(my_iter))  # d
print(next(my_iter))  # i
print(next(my_iter))  # a

# Looping

for x in my_tuple:
    print(x)

"""
O/P :
Apple
Dell
IBM

"""

for x in my_string:
    print(x)

"""
O/P :
I
n
d
i
a
"""


###
#   Create an Iterator class :  Need to implement the methods __iter__() and __next__()
#
#   The __iter__() : you can do operations (initializing etc.),
#                    but must always return the iterator object itself.
#
#   The __next__() : It also allows you to do operations, and must return the next item in the sequence.
###


class Numbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 7:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


my_numbers = Numbers()
my_iter = iter(my_numbers)

for x in my_iter:
    print(x)

"""
O/P :
1
2
3
4
5
6
7
"""
