# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:22:22 2024

@author: Student
"""

import math
a= float(input("Nhap a= "))
b= float(input("Nhap b= "))
a1= math.sqrt(a)
b1= math.sqrt(b)
a2= math.sqrt(math.sqrt(a))
b2= math.sqrt(math.sqrt(b))
ab= math.sqrt(math.sqrt(a*b))
print(" Gia tri cua bieu thuc la: ", ((a1- b1)/(a2 - b2))-((a1 + ab)/(a2+ b2)))