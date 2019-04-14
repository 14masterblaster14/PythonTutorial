##############################
#
# 16 # Usage of Modules :
#                       -   Need to import
#                       -   Module name should start with lower case
##############################


# Generate random numbers
import random

# Create a random floating point number i.e. between 0 and 1, [0.0, 1.0]. and print it.
print(random.random())  # O/P : 0.3539700489123593

# pick a random whole number between 0 and 10.
print(random.randrange(0, 10))  # O/P : 0

# pick a random floating point number between 0 and 10.
print(random.uniform(0, 10))  # O/P : 7.400656418774303

#####
# Custom modules
#####
import mymodule

a = mymodule.greetings("Sachin")  # O/P : Hello, Sachin
b = mymodule.cricketplayer["name"]
print("Player Name - ", b)  # O/P : Player Name -  Sachin

#####
# Alias
#####

import mymodule as mylib

c = mylib.cricketplayer["age"]
print("Player Age - ", c)  # O/P : Player Age -  45

#####
# Built in modules
#####

import platform

d = platform.system()
print("Your machines platform is - ", d)  # O/P : Your machines platform is -  Windows

# The dir() function: Lists all the defined functions / variable names belonging to the platform module
e = dir(platform)
# print(e)

"""
O/P :

['DEV_NULL', '_UNIXCONFDIR', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__'
, '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__'
, '__spec__', '__version__', '_comparable_version', '_component_re', '_default_architecture'
, '_dist_try_harder', '_follow_symlinks', '_ironpython26_sys_version_parser', 
'_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_linux_distribution', 
'_lsb_release_version', '_mac_ver_xml', '_node', '_norm_version', '_parse_release_file', '_platform'
, '_platform_cache', '_pypy_sys_version_parser', '_release_filename', '_release_version'
, '_supported_dists', '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file'
, '_syscmd_uname', '_syscmd_ver', '_uname_cache', '_ver_output', '_ver_stages', 'architecture'
, 'collections', 'dist', 'java_ver', 'libc_ver', 'linux_distribution', 'mac_ver', 'machine', 'node',
 'os', 'platform', 'popen', 'processor', 'python_branch', 'python_build', 'python_compiler'
 , 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're'
 , 'release', 'subprocess', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version',
  'warnings', 'win32_ver']
"""

f = dir(mylib)
print(f)

"""
O/P:

['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__'
, '__spec__', 'cricketplayer', 'greetings']
"""

#####
#   We can import only directory
#   When importing using the "from" keyword, do not use the module name when referring
#   to elements in the module.
#####

from mymodule import badmintonplayer

print(badmintonplayer["name"])  # O/P : Sania

####
#  Python Modules :
####

"""
Python Modules
Python Package
Python time
Python datetime
Python timeit
Python decimal
Python fractions
Python sleep
Python collections
Python Counter
Python OrderedDict
Python namedtuple
Python tarfile
Python zipfile
Python GZip
Python IO
Python tempfile
Python lxml
Python XML Parser
Python HTML Parser
Python HTTP Client
Python CSV Read Write
Python Parse JSON
Python MySQL Example
Python SQLite
Python Socket Programming
Python Multiprocessing example
Python threading module
Python Daemon Thread
Python subprocess
Python argparse
Python getopt
Python itertools
Python os module
Python sys module
Python struct pack unpack
Python System Command
Python unittest
Python hashlib
Python logging
Python ftp
Python functools
Python flask tutorial
Python pickle example
Python NumPy Tutorial
Python Matrix
Python Math
Python SimpleHttpServer
Python Signal Processing
Python urllib
Python shutil
Python getpass
Python ConfigParser
Python AST
Python Inspect
Python Theano
Python Matplotlib
Python Plotly
Python SciPy
Python TensorFlow
Python Keras
Python Scikit
Python Seaborn
Python StatsModels
Python Gensim
Python NetworkX
Python Bokeh
"""
