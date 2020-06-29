# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:44:24 2020

@author: vishal
"""



myfile=open("abc.txt", "a+")
myfile.write("Python Exercises\n")
myfile.write("Java Exercises")
myfile=open("abc.txt")
print(myfile.read())
