# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:23:13 2020

@author: vishal
"""
  
file1 = open('abc.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
for line in Lines: 
    print("Line{}: {}".format(count, line.strip())) 
    count=count+1