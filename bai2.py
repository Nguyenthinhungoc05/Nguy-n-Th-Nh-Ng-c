# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:54:45 2024

@author: Student
"""

var1=10
print("gia tri var1= ", var1,"\n\tKieu= ", type(var1))
var2= float(var1)
print("gia tri var2= ", var2,"\n\tKieu= ", type(var2))
var3= 3+ 4j
print("gia tri var3= ", var1, "\n\tKieu= ",type(var3))
var4= complex(var2)
print("gia tri var4= ", var4,"\n\tKieu= ",type(var4))

import math
a= int(input("nhap so nguyen a= "))
b= int(input("nhap so nguyen b= "))
tong= a + b
print("tong = ", a + b)
hieu= a - b
print("hieu= ", a -b)
tich= a*b
print("tich= ", a * b)
thuong= a/b
print("thuong= ", a/b )
chia_lay_du= a % b
print("chia lay du= ", a % b)
chia_lay_nguyen= a // b
print("chia lay nguyen= ", a // b)
round(chia_lay_nguyen,3)
