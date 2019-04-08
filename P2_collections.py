#############################
# 8 #    Python Collections
#
#        List is a collection which is ordered and changeable. Allows duplicate members.
#        Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#        Set is a collection which is unordered and unindexed. No duplicate members.
#        Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#############################


###
#   List :  A list is a collection which is ordered and changeable.
#           It allows duplicate members.
#           In Python lists are written with square brackets.
#
# Python does not have built-in support for Arrays, but Python Lists can be used instead.
###

emptyList = []
print(emptyList)

thislist = ["apple", "banana", "cherry"]
print(thislist)

# The list() Constructor
mylist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(mylist)

# Access Items
print(thislist[1])

# Change Item Value
thislist[1] = "blackcurrant"
print(thislist)

# Loop Through a List
for x in thislist:
    print(x)

# Check if Item Exists
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# List Length
print(len(thislist))

# Add Items
thislist.append("orange")
print(thislist)

# Insert an item at specific position:
thislist.insert(2, "Mango")
print(thislist)

# Remove Item
thislist.remove("Mango")
print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()
print(thislist)

# List functions:

print("----------------")
myList = [9, 4, 8, 2, 0, 6, 5, 7, 1, 5, 3]

print(sum(myList))

print(min(myList))

print(max(myList))

print(myList[0])

print(myList[-1])

reverseList = myList[::-1]
print(reverseList)

myList.sort()  # do not need to use a return variable when doing this, because lists are objects
print(myList)

# reverseList = list(reversed(myList))      # function reversed() which takes a list as parameter.
# But, the function does not return a list object but an iterator.
# The method list() converts the output of reversed() and converts it to a list object.

reverseList = myList[::-1]  # Elegant way
print(reverseList)

# range

x = list(range(100))  # starts counting from zero
print(x)

x = list(range(1, 101))
print(x)

for i in range(1, 12, 3):  # A third parameter defines the step size, by default its one.
    print(i)

# The del keyword removes the specified index:
print(thislist)
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely:
del thislist
# print(thislist)

# The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

###
# Python does not have built-in support for Arrays, but Python Lists can be used instead.
###

cars = ["Ford", "Tata", "BMW", "TOYOTA"]
print(cars[0])
cars[0] = "Mahindra"

x = len(cars)
print(x)

for x in cars: print(x)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


###
#   Tuples :    A tuple is a collection which is ordered and unchangeable.
#               In Python tuples are written with round brackets.
###

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# The tuple() Constructor : Using the tuple() method to make a tuple:
mytuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(mytuple)

# Access Tuple Items
print(thistuple[1])

# Change Tuple Values : but u Can't :)
# thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)

# Loop Through a Tuple
for x in thistuple:
    print(x)

# Check if Item Exists
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# Tuple Length
print(thistuple)
print(len(thistuple))

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

###
#  Sets :    A set is a collection which is unordered and unindexed.
#            In Python sets are written with curly brackets.
#            Once a set is created, you cannot change its items, but you can add new items.
#
###

thisset = {"apple", "banana", "cherry"}
print(thisset)

# The set() Constructor
myset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(myset)

# Access Items
for x in thisset:
    print(x)

# in
print("banana" in thisset)

# add()
thisset.add("orange")
print(thisset)

# update()
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

# Length of a Set
print(len(thisset))

# Remove Item by remove
# If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")
print(thisset)

# Remove Item by discard
# If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("mango")
print(thisset)

# pop()
# You can also use the pop(), method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed.
# The return value of the pop() method is the removed item.

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# del
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others


###
#  Dictionaries :
#                   - A dictionary is a collection which is unordered, changeable and indexed.
#                   - In Python dictionaries are written with curly brackets, and they have keys and values.
#
###

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# The dict() Constructor
#            note that keywords are not string literals
#            note the use of equals rather than colon for the assignment
mydict = dict(brand="Ford", model="Mustang", year=1964)

print(mydict)

# Accessing Items :
#   You can access the items of a dictionary by referring to its key name, inside square brackets:
#   get()
x = thisdict["model"]
print(x)
Y = thisdict.get("model")
print(Y)

# Change Values
# Change the "year" to 2018:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

# Loop Through a Dictionary

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x, y)

#  Check if Key Exists : in

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Dictionary Length
print(len(thisdict))

# Adding Items

thisdict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict1["color"] = "red"
print(thisdict1)

# Removing Items
# The pop() method removes the item with the specified key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

# del : The del keyword removes the item with the specified key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
print(thisdict)  # this will cause an error because "thisdict" no longer exists.

# The clear() keyword empties the dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and values
# get()	        Returns the value of the specified key
# items()	    Returns a list containing the a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary
