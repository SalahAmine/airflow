#!/usr/bin/env python


#  importing modules from absolute path


import imp
import os


file_path=os.path.abspath(os.path.dirname(__file__))

print 'the absolute dir of this script is ' + file_path

file_name="myday.py"

file_full_path = os.path.join(file_path, file_name)
print 'this scrpit full path is ' + file_full_path
# foo = imp.load_source('module.name', 


# print foo.__dict__
