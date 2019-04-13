#############################
# 12 #    Python Collections : The most basic data structure in Python is the sequence.
#                       Ordered     Changeable              Indexed         Duplicates
#        List       :   ordered     Yes                     Indexed         Allowed
#        Tuple      :   ordered     No                      Indexed         Allowed
#        Set        :   unordered   Yes                     Unindexed       Not Allowed
#        Dictionary :   unordered   Yes                     Indexed         Not Allowed
#############################


###
#   List :  A list is a collection which is ordered and changeable.
#           It allows duplicate members.
#           In Python lists are written with square brackets.
#
# Note : Python does not have built-in support for Arrays, but Python Lists can be used instead.
###

emptyList = []
print(emptyList)  # O/P : []

thislist = ["apple", "banana", "cherry"]
print(thislist)  # O/P : ['apple', 'banana', 'cherry']

# The list() Constructor
mylist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(mylist)  # O/P : ['apple', 'banana', 'cherry']

# Access Items
print(thislist[1])  # O/P : banana

# Change Item Value
thislist[1] = "blackcurrant"
print(thislist)  # O/P :['apple', 'blackcurrant', 'cherry']

# Loop Through a List
for x in thislist:
    print(x)

#   O/P :   apple
#           blackcurrant
#           cherry

# Check if Item Exists
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")  # O/P : Yes, 'apple' is in the fruits list

# List Length
print(len(thislist))  # O/P : 3

# Add Items
thislist.append("orange")
print(thislist)  # O/P : ['apple', 'blackcurrant', 'cherry', 'orange']

# Insert an item at specific position:
thislist.insert(2, "Mango")
print(thislist)  # O/P : ['apple', 'blackcurrant', 'Mango', 'cherry', 'orange']

# Remove Item
thislist.remove("Mango")
print(thislist)  # O/P : ['apple', 'blackcurrant', 'cherry', 'orange']

# The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()
print(thislist)  # O/P : ['apple', 'blackcurrant', 'cherry']

# List functions:

myList = [9, 4, 8, 2, 0, 6, 5, 7, 1, 5, 3]

print(sum(myList))  # O/P : 50

print(min(myList))  # O/P : 0

print(max(myList))  # O/P : 9

print(myList[0])  # O/P : 9

print(myList[-1])  # O/P : 3   (because its a sequence)
print(myList[-3])  # O/P : 1   (because its a sequence)

print(myList[4:])  # O/P : [0, 6, 5, 7, 1, 5, 3]   (Slicing)

reverseList = myList[::-1]
print(reverseList)  # O/P : [3, 5, 1, 7, 5, 6, 0, 2, 8, 4, 9]

myList.sort()  # do not need to use a return variable when doing this, because lists are objects
print(myList)  # O/P : [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

# reverseList = list(reversed(myList))      # function reversed() which takes a list as parameter.
# But, the function does not return a list object but an iterator.
# The method list() converts the output of reversed() and converts it to a list object.

reverseList = myList[::-1]  # Elegant way
print(reverseList)  # O/P : [9, 8, 7, 6, 5, 5, 4, 3, 2, 1, 0]

# range

x = list(range(10))  # starts counting from zero but excluding 10
print(x)  # O/P : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = list(range(1, 10))  # starts counting from 1 but excluding 10
print(x)  # O/P : [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(1, 12, 3):  # A third parameter defines the step size, by default its one.
    print(i)

# O/P :     1
#           4
#           7
#           10

# The del keyword removes the specified index:
print(thislist)  # O/P :  ['apple', 'blackcurrant', 'cherry']
del thislist[0]
print(thislist)  # O/P :  ['blackcurrant', 'cherry']

# The del keyword can also delete the list completely:
del thislist
# print(thislist)      # O/P :    NameError: name 'thislist' is not defined

# The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # O/P : []

###
# Python does not have built-in support for Arrays, but Python Lists can be used instead.
###

cars = ["Ford", "Tata", "BMW", "TOYOTA"]
print(cars[0])  # O/P : Ford
cars[0] = "Mahindra"

x = len(cars)
print(x)  # O/P : 4

for x in cars: print(x)

# O/P : Mahindra
#       Tata
#       BMW
#       TOYOTA

# append()	Adds an element at the end of the list
cars.append(["Mahindra", "Merc"])
print(cars)  # O/P : ['Mahindra', 'Tata', 'BMW', 'TOYOTA', ['Mahindra', 'Merc']]
cars.append("Audi")
cars.append("Audi")
print(cars)  # O/P : ['Mahindra', 'Tata', 'BMW', 'TOYOTA', ['Mahindra', 'Merc'], 'Audi','Audi']

# extend()	Add the elements of a list (or any iterable), to the end of the current list
cars.extend("VolksWagon")
print(cars)
# O/P :['Mahindra', 'Tata', 'BMW', 'TOYOTA', ['Mahindra', 'Merc'], 'Audi', 'Audi', 'V',
#           'o', 'l', 'k', 's', 'W', 'a', 'g', 'o', 'n']
cars.extend(["VolksWagon", "Skoda"])
print(cars)
# O/P :['Mahindra', 'Tata', 'BMW', 'TOYOTA', ['Mahindra', 'Merc'], 'Audi', 'Audi', 'V',
#           'o', 'l', 'k', 's', 'W', 'a', 'g', 'o', 'n', 'VolksWagon', 'Skoda']

# pop()	Removes the element at the specified position
x = cars.pop(7)
print(x)  # O/P : V
print(cars)
# O/P : ['Mahindra', 'Tata', 'BMW', 'TOYOTA', ['Mahindra', 'Merc'], 'Audi', 'Audi',
#           'o', 'l', 'k', 's', 'W', 'a', 'g', 'o', 'n', 'VolksWagon', 'Skoda']

# remove()	Removes the item with the specified value
cars.remove("o")
cars.remove("l")
cars.remove("k")
cars.remove("s")
cars.remove("W")
cars.remove("a")
cars.remove("g")
cars.remove("o")
cars.remove("n")
print(cars)
# O/P : ['Mahindra', 'Tata', 'BMW', 'TOYOTA', ['Mahindra', 'Merc'], 'Audi', 'Audi', 'VolksWagon', 'Skoda']

# copy()	Returns a copy of the list
myCars = cars.copy()
print(myCars)
# O/P : ['Mahindra', 'Tata', 'BMW', 'TOYOTA', ['Mahindra', 'Merc'], 'Audi', 'Audi', 'VolksWagon', 'Skoda']


# count()	Returns the number of elements with the specified value
print(myCars.count("Mahindra"))  # O/P : 1
print(myCars.count("Audi"))  # o/P : 2

# index()	Returns the index of the first element with the specified value
print((myCars.index("TOYOTA")))  # O/P : 3

# insert()	Adds an element at the specified position
myCars.insert(3, "HM")
print(myCars)
# O/P : ['Mahindra', 'Tata', 'BMW', 'HM', 'TOYOTA', ['Mahindra', 'Merc'], 'Audi', 'Audi', 'VolksWagon', 'Skoda']

# reverse()	Reverses the order of the list
myCars.reverse()
print(myCars)
# O/P : ['Skoda', 'VolksWagon', 'Audi', 'Audi', ['Mahindra', 'Merc'], 'TOYOTA', 'HM', 'BMW', 'Tata', 'Mahindra']

###
#   Tuples :    A tuple is a collection which is ordered and unchangeable.
#               In Python tuples are written with round brackets.
###

thistuple = ("apple", "banana", "cherry")
print(thistuple)  # O/P : ('apple', 'banana', 'cherry')

# The tuple() Constructor : Using the tuple() method to make a tuple:
mytuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(mytuple)  # O/P : ('apple', 'banana', 'cherry')

# Access Tuple Items
print(thistuple[1])  # O/P : banana

# Change Tuple Values : but u Can't :)
# thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)  # O/P : ('apple', 'banana', 'cherry')

# Loop Through a Tuple
for x in thistuple:
    print(x)
#   O/P :   apple
#           banana
#           cherry

# Check if Item Exists
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
# O/P : Yes, 'apple' is in the fruits tuple

# Tuple Length
print(thistuple)  # O/P : ('apple', 'banana', 'cherry')
print(len(thistuple))  # O/P : 3

# count()	Returns the number of times a specified value occurs in a tuple
tuple = (1, 2, 3, 4, 1)
print(tuple.count(1))  # O/P : 2

# index()	Searches the tuple for a specified value and returns the position of where it was found.
#           if the same element is present more than once, the first/smallest position is returned
print(tuple.index(1, 0, 3))  # O/P : 0
print(tuple.index(3, 0, 4))  # O/P : 2

###
#  Sets :    A set is a collection which is unordered and unindexed.
#            In Python sets are written with curly brackets.
#
###

thisset = {"apple", "banana", "cherry"}
print(thisset)  # O/P : {'apple', 'banana', 'cherry'}

# The set() Constructor
myset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(myset)  # O/P : {'apple', 'banana', 'cherry'}

# Access Items
for x in thisset:
    print(x)
# O/P : apple
#       banana
#       cherry

# in
print("banana" in thisset)  # O/P : True

# add()
thisset.add("orange")
print(thisset)  # O/P : {'orange', 'apple', 'banana', 'cherry'}

# update() Update the set with the union of this set and others
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)  # O/P : {'banana', 'mango', 'orange', 'apple', 'cherry', 'grapes'}

# Length of a Set
print(len(thisset))  # O/P : 6

# Remove Item by remove
# If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")
print(thisset)  # O/P : {'mango', 'orange', 'apple', 'cherry', 'grapes'}

# Remove Item by discard
# If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("mango")
print(thisset)  # O/P : {'orange', 'apple', 'cherry', 'grapes'}

# pop()
# You can also use the pop(), method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed.
# The return value of the pop() method is the removed item.

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)  # O/P : apple
print(thisset)  # O/P : {'banana', 'cherry'}

# clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)  # O/P : set()

# copy()	Returns a copy of the set
print(myset)  # O/P : {'cherry', 'apple', 'banana'}
thisset = myset.copy()
print(thisset)  # O/P : {'cherry', 'apple', 'banana'}

# del
del thisset
# print(thisset)          # O/P : NameError: name 'thisset' is not defined

thisset = {"apple", "banana", "cherry", "mango"}
myset = {'cherry', 'apple', 'banana'}

# difference()	Returns a set containing the difference between two or more sets
x = thisset.difference(myset)
print(x)  # O/P : {'mango'}
y = myset.difference(thisset)
print(y)  # O/P : set()

# difference_update()	Removes the items in this set that are also included in another, specified set.
thisset = {"apple", "banana", "cherry", "mango"}
myset = {'cherry', 'apple', 'banana'}

myset.difference_update(thisset)
print(myset)  # O/P : set()

thisset = {"apple", "banana", "cherry", "mango"}
myset = {'cherry', 'apple', 'banana'}

thisset.difference_update(myset)
print(thisset)  # O/P : {'mango'}

# intersection()	Returns a set, that is the intersection of two other sets
thisset = {"apple", "banana", "cherry", "mango"}
myset = {'cherry', 'apple', 'banana'}
x = thisset.intersection(myset)
print(x)  # O/P : {'banana', 'cherry', 'apple'}

# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
thisset.intersection_update(myset)
print(thisset)  # O/P : {'banana', 'cherry', 'apple'}

# isdisjoint()	Returns whether two sets have a intersection or not.
#               Sets are disjoint when their intersectioon is null
thisset = {"apple", "banana", "cherry", "mango"}
myset = {'cherry', 'apple', 'banana'}
urset = {"orange"}
print(urset.isdisjoint(myset))  # O/P : True
print(myset.isdisjoint(thisset))  # O/P : False

# issubset()	Returns whether another set contains this set or not
print(myset.issubset(thisset))  # O/P : True
print(thisset.issubset(myset))  # O/P : False

# issuperset()	Returns whether this set contains another set or not
print(myset.issuperset(thisset))  # O/P : False
print(thisset.issuperset(myset))  # O/P : True

thisset = {"apple", "banana", "cherry", "mango"}
myset = {'cherry', 'apple', 'banana'}
urset = {"orange"}

# symmetric_difference()	Returns a set with the symmetric differences of two sets
p = urset.symmetric_difference(myset)
print(p)  # O/P : {'banana', 'orange', 'apple', 'cherry'}

print(urset)  # O/P : {'orange'}
print(myset)  # O/P : {'cherry', 'apple', 'banana'}
print(thisset)  # O/P : {'cherry', 'mango', 'apple', 'banana'}

# symmetric_difference_update()	inserts the symmetric differences from this set and another to this set
urset.symmetric_difference_update(myset)
print(urset)  # O/P : {'banana', 'orange', 'apple', 'cherry'}
print(myset)  # O/P : {'banana', 'apple', 'cherry'}
thisset.symmetric_difference_update(urset)
print(thisset)  # O/P : {'mango', 'orange'}
print(urset)  # O/P : {'banana', 'orange', 'apple', 'cherry'}

thisset = {"apple", "banana", "cherry", "mango"}
myset = {'cherry', 'apple', 'banana'}
urset = {"orange"}

# union()	Return a set containing the union of sets
m = urset.union(myset)
print(m)  # O/P : {'orange', 'cherry', 'banana', 'apple'}
n = urset.union(myset).union(thisset)
print(n)  # O/P : {'banana', 'mango', 'cherry', 'orange', 'apple'}

###
#  Dictionaries :
#              - A dictionary is a collection which is unordered, changeable and indexed.
#              - In Python dictionaries are written with curly brackets, and they have keys and values.
#
###

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)  # O/P : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# The dict() Constructor
#            note that keywords are not string literals
#            note the use of equals rather than colon for the assignment
mydict = dict(brand="Ford", model="Mustang", year=1964)
print(mydict)  # O/P : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Accessing Items :
#   You can access the items of a dictionary by referring to its key name, inside square brackets:
#   get()
x = thisdict["model"]
print(x)  # O/P : Mustang
Y = thisdict.get("model")
print(Y)  # O/P : Mustang

# Change Values
# Change the "year" to 2018:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict.get("year"))  # O/P : 2018
# Loop Through a Dictionary

for x in thisdict:
    print(thisdict[x])
# O/P : Ford
#       Mustang
#       2018

for x in thisdict.values():
    print(x)
# O/P : Ford
#       Mustang
#       2018

for x, y in thisdict.items():
    print(x, y)
# O/P : brand Ford
#       model Mustang
#       year 2018

#  Check if Key Exists : in
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# O/P : Yes, 'model' is one of the keys in the thisdict dictionary

# Dictionary Length
print(len(thisdict))  # O/P : 3

# Adding Items
thisdict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict1["color"] = "red"
print(thisdict1)  # O/P : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Removing Items
# The pop() method removes the item with the specified key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)  # O/P : {'brand': 'Ford', 'year': 1964}

# The popitem() method removes the last inserted item
# (in versions before 3.7, a random item is removed instead):

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)  # O/P : {'brand': 'Ford', 'model': 'Mustang'}

# del : The del keyword removes the item with the specified key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)  # O/P : {'brand': 'Ford', 'year': 1964}

# The del keyword can also delete the dictionary completely:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
# print(thisdict)  # this will cause an error because "thisdict" no longer exists.
# O/P : NameError: name 'thisdict' is not defined

# The clear() keyword empties the dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)  # O/P : {}

# copy()	    Returns a copy of the dictionary
urdicts = thisdict1.copy()
print(urdicts)  # O/P : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
print("------------")
# fromkeys()	Returns a dictionary with the specified keys and values
x = ("Key1", "Key2", "Key3", "Key4", "Key5")
y = (4)

mydict = dict.fromkeys(x, y)
urdict = dict.fromkeys(x)
print(mydict)  # O/P : {'Key1': 4, 'Key2': 4, 'Key3': 4, 'Key4': 4, 'Key5': 4}
print(urdict)  # O/P : {'Key1': None, 'Key2': None, 'Key3': None, 'Key4': None, 'Key5': None}

# items()	    Returns a list containing the a tuple for each key value pair
m = mydict.items()
print(m)  # O/P : dict_items([('Key1', 4), ('Key2', 4), ('Key3', 4), ('Key4', 4), ('Key5', 4)])

# keys()	    Returns a list containing the dictionary's keys
n = mydict.keys()
print(n)  # O/P : dict_keys(['Key1', 'Key2', 'Key3', 'Key4', 'Key5'])

# values()	    Returns a list of all the values in the dictionary
r = mydict.values()
print(r)  # O/P : dict_values([4,4,4,4,4])

# setdefault()	Returns the value of the specified key.
#               If the key does not exist: insert the key, with the specified value
p = mydict.setdefault("Key4", "d")
q = mydict.setdefault("Key7", "d")
print(p)  # O/P : 4
print(q)  # O/P : d

# update()	    Updates the dictionary with the specified key-value pairs
print(urdicts)   # O/P : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
urdicts.update({"model": "EcoSport"})
print(urdicts)  # O/P : {'brand': 'Ford', 'model': 'EcoSport', 'year': 1964, 'color': 'red'}
