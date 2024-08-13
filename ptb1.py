# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:16:09 2024

@author: Student
"""

a = float(input("nhap a: "))
b = float(input("nhap b: "))
if a==0 and b==0:
    print("Phuong trinh co vo so nghiem")
elif a==0 and b!=0:
    print("Phuong trinh vo nghiem")
else:
    print("Phuong trinh co nghiem duy nhat",-b/a)
