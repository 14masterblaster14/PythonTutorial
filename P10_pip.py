#############################
#   # PIP
#           - PIP is a package manager for Python packages.
#           - If you have Python version 3.4 or later, PIP is included by default.
#
#############################

#####
#  Check Python version (command prompt)
#####

#   python --version


#####
#  Check PIP version (command prompt)
#####

#   pip --version


#####
#  PIP Path (command prompt)
#####

#   C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts


#####
#  List out the packages installed
#####

#   C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list

"""
O/P :

Package         Version
-----------------------
camelcase       0.2
mysql-connector 2.1.6
pip             18.1
pymongo         3.6.1
setuptools      39.0.1
"""

#####
#  Download and install Package
#
#  All packages : https://pypi.org/
#####

# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install pytz

# for using it , you need to import package
# import pytz


#####
#  uninstall Package
######

# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall pytz


# e.g.

import camelcase

txt = "hello world, i am indian"
c = camelcase.CamelCase()
print(c.hump(txt))  # This method capitalizes the first letter of each word.

# O/P :   Hello World, I Am Indian
