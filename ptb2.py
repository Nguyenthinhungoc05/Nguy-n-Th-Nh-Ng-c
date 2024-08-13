# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:18:35 2024

@author: Nguyen Thi Nhu Ngoc
"""
import math
a= float(input("Nhap he so a "))
b= float(input("Nhap he so b "))
c= float(input("Nhap he so c "))
delta= b*b - 4*a*c
if a!=0 and delta <0:
    print("Phuong trinh vo nghiem ")
elif a!=0 and delta ==0:
    print("Phuong trinh co nghiem kep x1=x2= ",-b/2*a)
elif a!=0 and delta >0:
    print("Phuong trinh co 2 nghiem phan biet: ")
    print("x1= ", (-b + math.sqrt(delta))/2*a)
    print("x2= ", (-b - math.sqrt(delta))/2*a )
else:
    print("Khong xac dinh")
    