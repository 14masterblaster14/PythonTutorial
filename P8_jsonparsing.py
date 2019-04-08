#############################
#
#   # JSON Parsing :
#                       -   JSON is a syntax for storing and exchanging data.
#                       -   JSON is text, written with JavaScript object notation.
#                       -   Python has a built-in package called json, which can be used to work with JSON data.
#
#############################

import json

# import temperature_logger_response

# Some JSON
x = '{"name":"Saurav Ganguly", "age":35, "city":"Kolkata"}'

# parse x json
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"])  # O/P : Saurav Ganguly

###
#   Convert from Python to JSON :
#                                   - We can convert Python objects of the following types, into JSON strings.
#                                   - When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
#
#       Python	        JSON
#
#       dict	        Object
#       list	        Array
#       tuple	        Array
#       str	            String
#       int	            Number
#       float	        Number
#       True	        true
#       False	        false
#       None	        null
#
###

# a Python object (dict):
a = {
    "name": "Sachin Tendulkar",
    "age": 45,
    "city": "Mumbai"
}

# convert into JSON:
b = json.dumps(a)

# the result is a JSON string:
print(b)

"""
O/P :

{"name": "Sachin Tendulkar", "age": 45, "city": "Mumbai"}
"""

# dict
print(json.dumps({"name": "John", "age": 30}))  # O/P : {"name": "John", "age": 30}

# list
print(json.dumps(["apple", "bananas"]))  # O/P : ["apple", "bananas"]

# tuple
print(json.dumps(("apple", "bananas")))  # O/P : ["apple", "bananas"]

# string
print(json.dumps("hello"))  # O/P : "hello"

# int
print(json.dumps(42))  # O/P : 42

# float
print(json.dumps(31.76))  # O/P : 31.76

# true
print(json.dumps(True))  # O/P : true

# false
print(json.dumps(False))  # O/P : false

# none
print(json.dumps(None))  # O/P : null

# complex conversion

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

"""
O/P :

{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

"""

"""
json.dumps(x, indent=4, separators=(". ", " = "))


# Order the Result : sort_keys
# Use the sort_keys parameter to specify if the result should be sorted or not:

json.dumps(x, indent=4, sort_keys=True)

"""

####
# loading external json file i.e. temperature_logger_response.JSON
####

# read file
with open("D:\DESKTOP\python\logger_response.json") as json_file:
    data = json_file.read()

# parse file
obj = json.loads(data)
print(obj)
# fi = json.dumps ("D:\DESKTOP\python\temperature_logger_response.json'")
# x = fi.read()
# print(fi)
